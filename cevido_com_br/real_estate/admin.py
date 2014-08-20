from django.contrib import admin

from real_estate.models import Property
from real_estate.models import Owner


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

admin.site.register(Owner)
admin.site.register(Property, PropertyAdmin)
