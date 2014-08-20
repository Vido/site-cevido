from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Photo(models.Model):
    name = models.CharField(max_length=64)
    original_image = models.ImageField(upload_to='photos')
    thumbnail = ImageSpecField(
        source='photos',
        processors=[ResizeToFill(100,50)],
        format='JPEG',
        options={'quality':80}
    )
    n_views = models.PositiveIntegerField(editable=False, default=0)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

