from django.shortcuts import render
from rest_app.forms import name_form
from django.contrib.auth.models import User, Group
from .models import NameModel
from rest_framework import viewsets
from rest_app.serializers import UserSerializer, GroupSerializer, NameSerializer

# Create your views here.
def index(request):
    print(request.method)
    if request.method == "POST":
        new_form = name_form(data=request.POST)

        print(new_form.is_valid())
        if new_form.is_valid():
            user = new_form.save(commit=False)
            user.save()
        else:
            print(new_form.errors)
    else:
        new_form = name_form()

    return render(request,'rest_app/index.html', {'new_form':new_form})

#Define viewsets for each of the serializer classes
#Django REST looks here when defining what to show
class NameViewSet(viewsets.ModelViewSet):
    queryset = NameModel.objects.all() #Define what objects are shown, all here.
    serializer_class = NameSerializer #Define the serializer class for this viewset

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
