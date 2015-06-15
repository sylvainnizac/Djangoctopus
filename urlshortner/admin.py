# -*- coding: utf8 -*-
from django.contrib import admin
from urlshortner.models import MiniURL

class MiniURLAdmin(admin.ModelAdmin):
    list_display   = ('longurl', 'shorturl', 'nbacces', 'pseudo', 'date')
    list_filter    = ('pseudo',)
    date_hierarchy = 'date'
    ordering       = ('-nbacces', )
    search_fields  = ('shorturl', 'pseudo')
    
    fieldsets = (
        # Fieldset 1 : meta-info
       ('Général',
       {'fields': ('longurl', 'pseudo'), }),
    )

# Register your models here.
admin.site.register(MiniURL, MiniURLAdmin)
