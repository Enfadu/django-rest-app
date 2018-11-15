from django.contrib.auth.models import User, Group
from .models import NameModel
from rest_framework import serializers

#Serializer to access the 'Users' database. This is Django's built in user database
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#Serializer to access Django's built-in 'Groups' database
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

#Serializer to access our own users database, populated using Faker()
class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NameModel #Point to the model
        fields = ('name','email') #Define the fields
                                  #This is required by REST to show results in the API view
