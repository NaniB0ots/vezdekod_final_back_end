import uuid

import PIL
import imagehash
from django.db import models


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ImageField('Изображение', upload_to='%Y/%m/%d/')
    p_hash = models.CharField(max_length=64, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.p_hash:
            image = PIL.Image.open(self.file)
            self.p_hash = imagehash.whash(image).hash.tostring().decode('UTF-8')
        return super(Image, self).save(*args, **kwargs)
