# -*- coding: utf8 -*-
from django import forms
from blog.models import Comments

class NewCom(forms.ModelForm):
    """really, a description?"""
    class Meta:
        model = Comments
        fields = ('pseudo', 'email', 'description')
