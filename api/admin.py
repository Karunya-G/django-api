from django.contrib import admin
from .models import *


@admin.register(Annote)
class AnnoteAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Imagess)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id','img_data']