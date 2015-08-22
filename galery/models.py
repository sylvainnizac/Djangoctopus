from django.db import models

# Create your models here.


class CarouArt(models.Model):
    """
    This class defines the table of carousel articles.
    """
    titre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True)
    contenu = models.TextField(null=True)
    illustration = models.ForeignKey('Photo')
    faction = models.ForeignKey('Faction')

    def __str__(self):
        return self.titre


class Faction(models.Model):
    """
    This class defines the list of Factions
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Name


class Sectorial(models.Model):
    """
    This class defines the list of sectorials
    """
    name = models.CharField(max_length=100, unique=True)
    factions = models.ForeignKey('Faction')

    def __str__(self):
        return self.Name


class Fig(models.Model):
    """
    This class defines the exhaustive list of available figs
    """
    name = models.CharField(max_length=100, unique=True)
    faction = models.ForeignKey('Faction', default=1)
    sectorial = models.ForeignKey('Sectorial', null=True)
    prime_Hacker = models.BooleanField(default=False)
    prime_Airborn = models.BooleanField(default=False)
    prime_Medic = models.BooleanField(default=False)
    prime_Ingenieur = models.BooleanField(default=False)
    prime_Camo = models.BooleanField(default=False)

    def __str__(self):
        return self.Name


class Photo(models.Model):
    """
    This class define the list of available photos
    """
    pic_Path = models.FilePathField(path="/home/sylvain/site-web/data/img", match="*.*", recursive=True)
    faction = models.ForeignKey('Faction', default=1)
    sectorial = models.ForeignKey('Sectorial', null=True)
    fig = models.ForeignKey('Fig')

    def __str__(self):
        return self.PicPath
