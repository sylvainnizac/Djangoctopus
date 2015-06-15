# -*- coding: utf8 -*-
from django import forms
from urlshortner.models import MiniURL

class AskToShort(forms.ModelForm):
    """really, a description?"""
    class Meta:
        model = MiniURL
        fields = ('longurl', 'pseudo')
