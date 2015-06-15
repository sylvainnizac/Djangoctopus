# -*- coding: utf8 -*-
from django import forms
from urlshortner.models import MiniURL

class AskToShort(forms.ModelForm):
    """Formulaire de récupération de l'URL à raccourcir"""
    class Meta:
        model = MiniURL
        fields = ('longurl', 'pseudo')
