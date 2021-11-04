import uuid

from django.db import models


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ImageField('Изображение', upload_to='%Y/%m/%d/')
    # height = models.FloatField('Высота')
    # width = models.FloatField('Ширина')

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
