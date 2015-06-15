# -*- coding: utf8 -*-
from django.db import models
import random
import string

# Create your models here.

class MiniURL(models.Model):
    """
    This class defines the table to stock the short urls
    """
    shorturl = models.CharField(max_length=6, unique=True)
    longurl = models.URLField()
    pseudo = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de création")
    nbacces = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.longurl
        
    def save(self, *args, **kwargs):
        """modifying the save method to include one more data"""
        #pk is used for Primary Key, here the only unique field
        if self.pk is None:
            self.generer(6)
        #super allows to use the "mother" version of a method, ignoring the "daughter" version
        super(MiniURL, self).save(*args, **kwargs)
    
    def generer(self, nb_caracteres):
        """on génère une chaine aléatoire de 6 caractères"""
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
    
        self.shorturl = ''.join(aleatoire)
