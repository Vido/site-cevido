# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from filer.fields.image import FilerImageField
from easy_thumbnails.fields import ThumbnailerImageField


class Owner(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    comercial_phone = models.CharField(max_length=20, blank=True, null=True)
    residential_phone = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        if self.mobile_phone:
            return '%s (Cel: %s)' % (self.name, self.mobile_phone)
        elif self.comercial_phone:
            return '%s (TelCm: %s)' % (self.name, self.comercial_phone)
        elif self.residential_phone:
            return '%s (TelRs: %s)' % (self.name, self.residential_phone)

        return self.name


class Property(models.Model):

    CATEGORY = (
        ('T', 'Terreno'),
        ('H', 'Casa'),
        ('A', 'Apartamento'),
        ('C', 'Comercial'),
        ('X', 'Chacara'),
        ('S', 'Sitio'),
        ('F', 'Fazenda'),
    )

    owner = models.ForeignKey(Owner)
    address = models.TextField(null=False)
    category = models.CharField(max_length=1, choices=CATEGORY)

    price = models.PositiveIntegerField()
    condo = models.PositiveIntegerField(default=0)
    rent = models.PositiveIntegerField(default=0)

    rooms = models.PositiveIntegerField(default=0)
    wc = models.PositiveIntegerField(default=0)
    garage = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10, default='m²')

    city = models.TextField(null=True)
    neighborhood = models.TextField(null=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    clicks = models.PositiveIntegerField(editable=False, default=0)

    #def save(self):
    #    if self.photo_gallery is None:
    #        # This comes from the initial fixtures
    #        self.photo_gallery_id = 1
    #    super(Property, self).save()

    def verbose_category(self):
        return dict(Property.CATEGORY)[self.category]

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        catg_name = [c for c in self.CATEGORY if c[0] == self.category]

        catg_name = catg_name[0][1] if catg_name else "/"
        trunc_addr = self.address[:25]
        return "%s %s" % (catg_name, trunc_addr)


    @models.permalink
    def get_absolute_url(self):
        return ('real_estate.views.re_details', [str(self.pk)])

class Photo(models.Model):
    image_file = FilerImageField()
    fk_property = models.ForeignKey(Property)

    @property
    def thumbnail(self):
        options = {'size': (140, 120), 'crop': True}
        return self.image_file.easy_thumbnails_thumbnailer.get_thumbnail(options)

