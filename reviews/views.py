from django.shortcuts import render


def index(request):
    # This is the view for the index page of the reviews app.
    name = request.GET.get("name") or "nobody"
    return render(request, "base.html", {"name": name})

def search(request):
    # this is the view for the search page of the reviews app.
    search_term = request.GET.get("q")
    return render(request, "search.html", {"search_text": search_term})