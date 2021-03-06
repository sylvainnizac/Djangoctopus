# -*- coding: utf8 -*-
from django import forms
from blog.models import Comment

class NewCom(forms.ModelForm):
    """really, a description?"""
    def __init__(self, *args, **kwargs):
        # On passe la foreign_key en paramètre à partir de la view
        k = 'article'
        if k in kwargs:
            self.article = kwargs.pop('article')
        super(NewCom, self).__init__(*args, **kwargs)
        
    def save(self, commit=True):
        # On sauve sans faire la requête SQL (commit=False) pour
        # pouvoir ajouter à l'instance la foreignkey
        super(NewCom, self).save(commit=False)
        # On ajoute à l'instance la foreignkey
        self.instance.article = self.article
        # On peut maintenant sauver
        super(NewCom, self).save(commit)
        
    class Meta:
        model = Comment
        fields = ('pseudo', 'email', 'description')
        widgets = {'pseudo': forms.TextInput(attrs={'placeholder': 'Ton pseudo'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Ton mail (optionnel)'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Ton commentaire'})}
        labels = {'pseudo': '', 'email': '', 'description': ''}
