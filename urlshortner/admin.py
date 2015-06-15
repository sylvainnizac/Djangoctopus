# -*- coding: utf8 -*-
from django.contrib import admin
from urlshortner.models import MiniURL

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'auteur', 'date', 'categorie', 'apercu_contenu')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields  = ('titre', 'contenu')
    
    prepopulated_fields = {"slug": ("titre",)}
    
        # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général',
       {'fields': ('titre', 'slug', 'auteur', 'categorie'), }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article',
        { 'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
        'fields': ('contenu', )}),
    )

# Register your models here.
admin.site.register(MiniURL)
