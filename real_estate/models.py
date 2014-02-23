from django.db import models

from django.contrib.auth.models import User

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
    email = models.EmailField(unique=False, null=False)
    address = models.TextField(null=False)
    category = models.CharField(max_length=1, choices=CATEGORY)
    price = models.IntegerField()

    def __repr__(self):
        catg_name = [c for c in self.CATEGORY if c[0] == self.category]
        
        catg_name = catg_name[0][1] if catg_name else "/"
        trunc_addr = self.address[:25]
        return "%s %s" % (catg_name, trunc_addr)

