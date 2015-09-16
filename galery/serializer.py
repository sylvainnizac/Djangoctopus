# -*- coding: utf8 -*-
from rest_framework import serializers
from galery.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """
    standard serialization class, like for forms
    create() and update() methods already impemented
    """

    pic_path = serializers.URLField()

    class Meta:
        model = Photo
        fields = ('pic_path', )
