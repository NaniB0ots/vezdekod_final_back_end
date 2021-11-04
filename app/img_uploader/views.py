import base64
from io import BytesIO

from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from img_uploader.serializers import ImageSerializer
from . import models

from PIL import Image
import imagehash
import numpy as np


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

        # sql = 'SELECT *, BIT_COUNT(0xfefefed3e0a02000 ^ p_hash) as hamming_distance ' \
        #       'FROM img_uploader_image ' \
        #       'HAVING hamming_distance <= 10'

        try:
            instance = models.Image.objects.get(pk=pk)
        except (models.Image.DoesNotExist, ValidationError):
            return Response('Изображение не найдено', status=status.HTTP_404_NOT_FOUND)
        image: Image = Image.open(instance.file)

        image_hash = imagehash.whash(image)

        ratio = image.height / image.width
        print('ratio: ', ratio)
        for item in models.Image.objects.exclude(id=pk):

            bit_array = []
            bit_row = []
            i = 0
            for bit in item.p_hash.encode('utf-8'):
                i += 1
                bit_row.append(bit)
                if i == 8:
                    bit_array.append(bit_row)
                    bit_row = []
                    i = 0
            bit_array = np.array(bit_array)

            h_distance = (imagehash.ImageHash(bit_array) - image_hash)
            print('h_distance: ', h_distance)
            print(item)


            item_image = Image.open(item.file)
            ratio_item = item_image.height / item_image.width
            print('ratio_item: ', ratio_item)
            if h_distance < 10:
                pass

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
