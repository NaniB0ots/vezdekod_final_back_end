import PIL
from rest_framework.serializers import ModelSerializer
from . import models


class ImageSerializer(ModelSerializer):
    class Meta:
        model = models.Image
        fields = ('file',)

    def create(self, validated_data):
        image = PIL.Image.open(validated_data['file'])
        validated_data['height'] = image.height
        validated_data['width'] = image.width
        return super(ImageSerializer, self).create(validated_data)
