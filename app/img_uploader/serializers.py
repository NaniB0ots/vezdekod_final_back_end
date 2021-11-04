from rest_framework.serializers import ModelSerializer
from . import models


class ImageSerializer(ModelSerializer):
    class Meta:
        model = models.Image
        fields = ('file',)
