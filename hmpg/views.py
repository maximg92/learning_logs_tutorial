from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page."""
    return render(request, 'hmpg/index.html')