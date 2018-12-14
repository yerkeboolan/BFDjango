from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Advert.models Advert
from api1.serializer import AdvertModelSerializer


@api_view(['GET', 'POST'])
def get(self, request):
        adverts = Advert.objects.all()
        serializer = AdvertModelSerializer(adverts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def advert_detail(self, pk):
        try:
            return Advert.objects.get(id=pk)
        except Advert.DoesNotExist:
            raise Http404

        advert = self.get_object(pk)
        serializer= AdvertModelSerializer(advert)
        return Response(serializer.data)

        advert = self.get_object(pk)
        serializer = AdvertModelSerializer(instance=advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        advert = self.get_object(pk)
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
