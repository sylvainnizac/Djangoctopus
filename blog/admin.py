# -*- coding: utf8 -*-
from django.contrib import admin
from blog.models import Categorie, Article, Comment

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
       {'fields': ('titre', 'slug', 'auteur', 'categorie')
       }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article',
        { 'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
        'fields': ('contenu', )
        }),
    )
    
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension. 
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s...' % text
        else:
            return text

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'

class CommentsAdmin(admin.ModelAdmin):
    list_display   = ('pseudo', 'email', 'article', 'apercu_description', 'date', 'commentaire_visible')
    list_filter    = ('pseudo', 'article', 'email', )
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields  = ('pseudo', 'email', 'article', )
    
        # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général',
       {'fields': ('pseudo', 'email'), }),
        # Fieldset 2 : contenu de l'article
        ('Commentaire',
        { 'description': 'Le formulaire n\'accepte pas les balises HTML.',
        'fields': ('description', )}),
        # Fieldset 3 : modération
        ('Modération',
        { 'fields': ('commentaire_visible', )}),
    )
    
    def apercu_description(self, commentaire):
        """ 
        Retourne les 40 premiers caractères du contenu du commentaire. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension. 
        """
        text = commentaire.description[0:40]
        if len(commentaire.description) > 40:
            return '%s...' % text
        else:
            return text

    # En-tête de notre colonne
    apercu_description.short_description = 'Aperçu du commentaire'

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentsAdmin)
