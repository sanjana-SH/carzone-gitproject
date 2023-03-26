from django.contrib import admin
from . models import *
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    #to display the img in admin db
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px;"/>'.format(object.photo.url))

    #for changing the name from thumbnail to photo
    thumbnail.short_description = 'photo'



    # to display the table in admin db
    list_display = ('id','thumbnail','first_name','last_name','designation','created_date')
    list_display_links = ('id','thumbnail','first_name')
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)




admin.site.register(Team,TeamAdmin)
