# -*- coding: utf8 -*-
from django import forms
from blog.models import Comments

class NewCom(forms.ModelForm):
    """really, a description?"""
    def __init__(self, *args, **kwargs):
        # On passe la foreign_key en paramètre à partir de la view
        k = 'article'
        if k in kwargs:
            self.article = kwargs.pop('article')
        super(NewCom, self).__init__(*args, **kwargs)
        

        
    class Meta:
        model = Comments
        fields = ('pseudo', 'email', 'description')
