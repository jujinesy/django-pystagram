# codding: utf-8

from django.contrib import admin

# Register your models here.

from Photos.models import Photo

admin.site.register(Photo)