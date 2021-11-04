import base64
from io import BytesIO

from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from img_uploader.serializers import ImageSerializer
from . import models

from PIL import Image


class UploadImageView(APIView):

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(instance.id, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowImageView(APIView):
    def get(self, request, pk: str):
        try:
            instance = models.Image.objects.get(pk=pk)
        except (models.Image.DoesNotExist, ValidationError):
            return Response('Изображение не найдено', status=status.HTTP_404_NOT_FOUND)
        image: Image = Image.open(instance.file)

        # масштабирование
        scale = request.GET.get('scale')
        if scale:
            try:
                scale = float(scale)
            except ValueError:
                return Response('Параметр scale должен быть числом', status=status.HTTP_400_BAD_REQUEST)

            fixed_width = int(image.width * scale)
            if fixed_width <= 0:
                fixed_width = 1
            width_percent = (fixed_width / float(image.size[0]))
            height_size = int((float(image.height) * float(width_percent)))
            if height_size <= 0:
                height_size = 1
            image = image.resize((fixed_width, height_size))

        buffered = BytesIO()
        image.save(buffered, format='JPEG')
        img_str = base64.b64encode(buffered.getvalue())

        return Response(img_str)
