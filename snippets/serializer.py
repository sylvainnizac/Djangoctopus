# -*- coding: utf8 -*-
from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    """
    standard serialization class, like for forms
    create() and update() methods already impemented
    """
    class Meta:
        model = Snippet
        fields =('id', 'title', 'description', 'code', 'linenos', 'language', 'style')