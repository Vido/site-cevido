# -*- coding: utf-8 -*-

from django.db import models

from filer.fields.image import FilerImageField

from cevido import settings


class Owner(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=64)
    email = models.EmailField(blank=True, null=True)
    mobile_phone = models.CharField(
        max_length=20, blank=True, null=True)
    comercial_phone = models.CharField(
        max_length=20, blank=True, null=True)
    residential_phone = models.CharField(
        max_length=20, blank=True, null=True)
    extra_info = models.TextField(
        blank=True, null=True, verbose_name='Additional Information')

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


class City(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=64)
    state = models.CharField(max_length=2)

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "%s-%s" % (self.name, self.state.upper())


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
    category = models.CharField(max_length=1, choices=CATEGORY)

    address = models.CharField(max_length=512, null=False)
    number = models.CharField(max_length=10, null=True)
    neighborhood = models.CharField(max_length=512, null=True)
    city = models.ForeignKey(City)

    price = models.PositiveIntegerField()
    condo = models.PositiveIntegerField(default=0)
    rent = models.PositiveIntegerField(default=0)

    description = models.TextField(null=True)
    rooms = models.PositiveIntegerField(default=0)
    wc = models.PositiveIntegerField(default=0)
    garage = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10, default='m²')

    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    clicks = models.PositiveIntegerField(editable=False, default=0)

    # def save(self):
    #     if self.photo_gallery is None:
    #         # This comes from the initial fixtures
    #         self.photo_gallery_id = 1
    #     super(Property, self).save()

    def verbose_category(self):
        return dict(Property.CATEGORY)[self.category]

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        catg_name = [c for c in self.CATEGORY if c[0] == self.category]
        catg_name = catg_name[0][1] if catg_name else "/"
        return "%s %s" % (catg_name, self.address)

    @models.permalink
    def get_absolute_url(self):
        return ('real_estate.views.re_details', [str(self.pk)])

    @property
    def thumbnail(self):
        """ Returns the thumbnail url, or the default url. """
        default_image = 'generic_photo.png'
        photo_qs = Photo.objects.filter(fk_property=self)
        if photo_qs:
            return photo_qs[0].thumbnail.url
        return settings.STATIC_URL + default_image


class Photo(models.Model):
    image_file = FilerImageField()
    fk_property = models.ForeignKey(Property)

    @property
    def thumbnail(self):
        options = {'size': (140, 120), 'crop': True}
        return self.image_file.easy_thumbnails_thumbnailer.get_thumbnail(
            options)
