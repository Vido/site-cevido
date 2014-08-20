from django.contrib import admin
from django.contrib.contenttypes import generic

from models import Photo

class ImagesInline(generic.GenericTabularInline):
    model = Photo
    max_num = 4
