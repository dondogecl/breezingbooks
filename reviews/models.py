from django.db import models
from django.contrib import auth


# Contributor model
class Contributor(models.Model):
    """Model for a person who contributed to a book (author, co-author, editor, etc.)"""
    first_names = models.CharField(max_length=100, help_text="Contributor First Names")
    last_names = models.CharField(max_length=100, help_text="Contributor Last Names")
    email = models.EmailField(help_text="Contributor Email address")

    def __str__(self):
        """String representation of the current object"""
        return self.first_names + " " + self.last_names
     

# BookContributor model (intermediate model)
class BookContributor(models.Model):
    """Intermediate model for the relationship between a book and its contributors"""
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUT', 'Author'
        CO_AUTHOR = 'COA', 'Co-Author'
        EDITOR = 'EDT', 'Editor'
        REVIEWER = 'REV', 'Reviewer'
        OTHER = 'OTH', 'Other'

    book = models.ForeignKey('Book', on_delete=models.CASCADE, help_text="Book")
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, help_text="Contributor")
    role = models.CharField(
        verbose_name="Contribution Role",
        choices = ContributionRole.choices,
        max_length = 20
    )



# Publisher model
class Publisher(models.Model):
    """ Model for the company responsible of publishing one or 
    more books"""
    name = models.CharField(max_length=100, help_text="Publisher Name")
    website = models.URLField(help_text="Publisher Website")
    email = models.EmailField(help_text="Publisher Email address")

    def __str__(self):
        """String representation of the current object"""
        return self.name


# Book model
class Book(models.Model):
    """Model for a published book"""
    title = models.CharField(max_length=200, help_text="Book Title")
    publication_date = models.DateField(help_text="Book Publication Date")
    isbn = models.CharField(max_length=13, help_text="Book ISBN")
    # relationships (FK)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, help_text="Book Publisher")
    contributors = models.ManyToManyField(Contributor, through='BookContributor', help_text="Book Contributors")

    def __str__(self):
        """String representation of the current object"""
        return self.title


# Review model
class Review(models.Model):
    """Model for a review of a book"""
    content = models.TextField(help_text="Review Content")
    rating = models.IntegerField(help_text="Review Rating")
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="Review Date Created")
    date_edited = models.DateTimeField(null=True,
                                       help_text="Review Date Edited")
    # Relationships (FK)
    creator = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE,
                                help_text="Review Creator")
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             help_text="Reviewed Book")