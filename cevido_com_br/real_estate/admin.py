from django.contrib import admin

from real_estate.models import Owner
from real_estate.models import City
from real_estate.models import Property
from real_estate.models import Photo


class ImageInline(admin.StackedInline):
    model = Photo


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Owner)
admin.site.register(City)
admin.site.register(Property, PropertyAdmin)
