import os
import django
from faker import Faker
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FilmProject.settings')
django.setup()

from films.models import Country, Category

fake = Faker()


cat_list = ['Drama',
'Comedy',
'Action',
'Fantasy',
'Horror',
'Romance',
'Western',
'Thriller']

# if __name__ == '__main__':
#     for _ in range(15):
#         print("Populating database, table 'Country'")

#         new_cat = Country(name = fake.country())
#         print(new_cat)
#         new_cat.save()


# if __name__ == '__main__':
#     for cat in cat_list:
#         print("Populating database, table 'Category'")

#         new_cat = Category(name = cat)
#         print(new_cat)
#         new_cat.save()