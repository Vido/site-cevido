from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from photologue.models import Gallery

# Create your models here.
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

    # Reference number
    #owner = models.ForeignKey(User)

    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)
    photo_gallery = models.OneToOneField(Gallery, primary_key=False)

    email = models.EmailField(unique=False, null=False)
    address = models.TextField(null=False)
    category = models.CharField(max_length=1, choices=CATEGORY)

    price = models.IntegerField()
    condo = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)

    rooms = models.IntegerField(default=0)
    wc = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)

    area = models.IntegerField(default=0)
    city = models.TextField(null=True)
    neighborhood = models.TextField(null=True)


    def __repr__(self):
        catg_name = [c for c in self.CATEGORY if c[0] == self.category]

        catg_name = catg_name[0][1] if catg_name else "/"
        trunc_addr = self.address[:25]
        return "%s %s" % (catg_name, trunc_addr)


    @models.permalink
    def get_absolute_url(self):
        return ('real_estate.views.re_details', [str(self.pk)])

