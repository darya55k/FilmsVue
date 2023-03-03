from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CreateFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class CreateFilmIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class AuthoringSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Authoring
        fields = '__all__'


class CreateAuthoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authoring
    
        fields = '__all__'