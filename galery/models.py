# -*- coding: utf8 -*-
from django.db import models

# Create your models here.


class CarouArt(models.Model):
    """
    This class defines the table of carousel articles.
    """
    titre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
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
        return self.name


class Sectorial(models.Model):
    """
    This class defines the list of sectorials
    """
    name = models.CharField(max_length=100, unique=True)
    factions = models.ForeignKey('Faction')

    def __str__(self):
        return self.name


class Fig(models.Model):
    """
    This class defines the exhaustive list of available figs
    """
    name = models.CharField(max_length=100, unique=True)
    faction = models.ForeignKey('Faction', default=1)
    sectorial = models.ForeignKey('Sectorial')
    prime_Hacker = models.BooleanField(default=False)
    prime_Airborn = models.BooleanField(default=False)
    prime_Medic = models.BooleanField(default=False)
    prime_Ingenieur = models.BooleanField(default=False)
    prime_Camo = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    """
    This class define the list of available photos
    """
    pic_path = models.FilePathField(path="/var/www/public/data/img/galerie", recursive=True)
    faction = models.ForeignKey('Faction', default=1)
    sectorial = models.ForeignKey('Sectorial')
    fig = models.ForeignKey('Fig')

    def __str__(self):
        shpath = self.pic_path
        shtab = shpath.split("/")
        nshpath = "/" + "/".join(shtab[3:])

        return nshpath


class AutreIllu(models.Model):
    """
    This class defines the list of other illustrations
    """
    pic_path = models.FilePathField(path="/var/www/public/data/img/illus", recursive=True)
    in_carousel = models.BooleanField(default=False)
    faction = models.ForeignKey('Faction', default=1)

    def __str__(self):
        shpath = self.pic_path
        shtab = shpath.split("/")
        nshpath = "/" + "/".join(shtab[3:])

        return nshpath


class Logo(models.Model):
    """
    This class defines the list of logos
    """
    logo_path = models.FilePathField(path="/var/www/public/data/img/logos", recursive=True)
    display_carousel = models.BooleanField(default=False)
    faction = models.ForeignKey('Faction')
    sectorial = models.ForeignKey('Sectorial')
    citation = models.TextField(null=True)

    def __str__(self):
        shpath = self.logo_path
        shtab = shpath.split("/")
        nshpath = "/" + "/".join(shtab[3:])

        return nshpath
