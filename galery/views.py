from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from galery.models import CarouArt, AutreIllu, Logo, Faction, Sectorial, Photo, Fig
from galery.serializer import PhotoSerializer


class Main_carousel(ListView):
    """
    This class allows to quickly call the article list. and return other useful data for the page
    """
    model=CarouArt
    context_object_name="articles"
    template_name="galery/carousel.html"

    def get_queryset(self):
        """modify standard data recovery"""
        temp = CarouArt.objects.all().order_by('-date')
        return temp

    def get_context_data(self, **kwargs):
        """recover and modify the context data to add the list of categories"""
        context = super(Main_carousel, self).get_context_data(**kwargs)
        #add the new context data
        context['illus'] = AutreIllu.objects.filter(in_carousel=True)
        context['logos'] = Logo.objects.filter(display_carousel=True)
        return context

class Main_galery(ListView):
    """
    This class gathered all data for galery side bar
    """
    model=Faction
    context_object_name="factions"
    template_name="galery/galery.html"
    
    def get_queryset(self):
        """modify standard data recovery"""
        return Faction.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        """add sectorial and figs data"""
        context = super(Main_galery, self).get_context_data(**kwargs)
        factions = context['factions']
        total = []
        for f in factions:
            temp = [f, ]
            sector = Sectorial.objects.filter(factions = f).order_by('name')
            for s in sector:
                figus = Fig.objects.filter(sectorial = s).order_by('name')
                temp.append([s, figus])
            total.append(temp)
        context['sidemenus'] = total
        return context

def pics_list(request, faction = None, secto = None, fig = None):
    """
    List all pictures
    """
    if faction == None && secto == None && fig == None:
        pics = Photo.objects.all()
        serializer = PhotoSerializer(pics, many = True)
        return Response(serializer.data)
    elif faction != None:
        pics = Photo.objects.filter(faction = faction)
        serializer = PhotoSerializer(pics, many = True)
        return Response(serializer.data)
    elif secto != None:
        pics = Photo.objects.filter(sectorial = secto)
        serializer = PhotoSerializer(pics, many = True)
        return Response(serializer.data)
    elif fig != None:
        pics = Photo.objects.filter(fig = fig)
        serializer = PhotoSerializer(pics, many = True)
        return Response(serializer.data)
