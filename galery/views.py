from django.shortcuts import render

# Create your views here.

class Main_carousel(ListView):
    """
    This class allows to quickly call the article list. and return other useful data for the page
    """
    model=CarouArt
    context_object_name="articles"
    template_name="galery/carousel.html"
    paginate_by = 5
