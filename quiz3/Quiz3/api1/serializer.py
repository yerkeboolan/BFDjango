from rest_framework import serializers
from Quiz3.Advert.models import Advert
from django.contrib.auth.models import User

class AdvertModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ['title', 'address', 'description', 'price', 'number_of_views']

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()