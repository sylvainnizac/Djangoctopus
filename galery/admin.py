# -*- coding: utf8 -*-
from django.contrib import admin
from galery.models import Faction, Sectorial, Fig, Photo, CarouArt, AutreIllu, Logo


class CarouArtAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'slug', 'contenu', 'illustration', 'faction', 'date')
    list_filter    = ('faction', 'date')
    date_hierarchy = 'date'
    ordering       = ('-date', )
    
    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {'fields': ('titre', 'slug', 'illustration', 'faction')}),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {'fields': ('contenu', )}),
    )
    
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article.
        S'il y a plus de 40 caractères, il faut ajouter des points de suspension.
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s...' % text
        else:
            return text

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'


class LogoAdmin(admin.ModelAdmin):
    list_display   = ('logo_path', 'faction', 'sectorial', 'display_carousel', 'citation')
    list_filter    = ('faction',)
    ordering       = ('faction', )

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {'fields': ('logo_path', 'faction', 'sectorial', 'display_carousel')}),
        # Fieldset 2 : citation associée au logo
        ('Citation', {'fields': ('citation', )}),
    )

    def apercu_citation(self, logo):
        """
        Retourne les 40 premiers caractères du contenu de l'article.
        S'il y a plus de 40 caractères, il faut ajouter des points de suspension.
        """
        text = logo.citation[0:40]
        if len(logo.citation) > 40:
            return '%s…' % text
        else:
            return text

    # En-tête de notre colonne
    apercu_citation.short_description = 'Aperçu de la citation'


# Register your models here.
admin.site.register(Faction)
admin.site.register(Sectorial)
admin.site.register(Fig)
admin.site.register(Photo)
admin.site.register(AutreIllu)
admin.site.register(Logo, LogoAdmin)
admin.site.register(CarouArt, CarouArtAdmin)
