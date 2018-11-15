import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RESTPRoject.settings')

import django
django.setup()

import random
from rest_app.models import NameModel
from faker import Faker

fakegen = Faker()

def populate(N=500):
    for entry in range(N):

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_email = fakegen.email()

        namemod = NameModel.objects.get_or_create(name=fake_name,email=fake_email)[0]

if __name__ == '__main__':
    populate(500)
    print("Population complete!")
