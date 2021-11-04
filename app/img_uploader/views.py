from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from img_uploader.serializers import ImageSerializer


class UploadImageView(APIView):

    def post(self, request, format=None):
        print('Yes')
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowImageView(APIView):
    def get(self, request, pk):
        return Response(f'Дароу {pk}')
