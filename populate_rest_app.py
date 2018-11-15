import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RESTPRoject.settings')
#Set django settings

import django
django.setup()

import random
from rest_app.models import NameModel #import model to be used
from faker import Faker #import Faker library

#Create a new Faker instance
fakegen = Faker()


def populate(N=500): #N is number of entried to be created (default N=500)
    #Loop and create entried
    for entry in range(N):

        fake_url = fakegen.url() #url
        fake_date = fakegen.date() #date
        fake_company = fakegen.company() #company
        fake_name = fakegen.name() #Full legan name
        fake_email = fakegen.email() #email

        namemod = NameModel.objects.get_or_create(name=fake_name,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating...")
    populate(500) #Create 500 entries
    print("Population complete!")
