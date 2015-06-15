from django.db import models

class Article(models.Model):
    """
    This class defines the table of blog articles.
    """
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True)
    auteur = models.CharField(max_length=50)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', default=0)
    
    def __str__(self):
        """ 
        this methode is designed to be used for administration and debbuging purpose
        """
        return self.titre
        
    def titleslug(self):
        """
        """
        return self.titre

class Categorie(models.Model):
    """
    This class defines the table of categories
    """
    nom = models.CharField(max_length=30)
    
    def __str__(self):
        """ 
        this methode is designed to be used for administration and debbuging purpose
        """
        return self.nom
