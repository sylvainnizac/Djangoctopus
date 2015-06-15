from django.db import models
import random
import string

# Create your models here.

class MiniURL(models.Model):
    """
    This class defines the table to stock the short urls
    """
    shorturl = models.CharField(max_length=10)
    longurl = models.URLField()
    pseudo = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de création")
    nbacces = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.longurl
    
    def generer(nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
    
        return ''.join(aleatoire)
