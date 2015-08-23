from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from galery.models import CarouArt, AutreIllu, Logo


class Main_carousel(ListView):
    """
    This class allows to quickly call the article list. and return other useful data for the page
    """
    model=CarouArt
    context_object_name="articles"
    template_name="galery/carousel.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """recover and modify the context data to add the list of categories"""
        context = super(Main_carousel, self).get_context_data(**kwargs)
        #add the new context data
        context['illus'] = AutreIllu.objects.filter(in_carousel=True)
        context['logos'] = Logo.objects.filter(display_carousel=True)
        return context
