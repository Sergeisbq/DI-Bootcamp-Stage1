import os
import django
from faker import Faker
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alg.settings')
django.setup()

from algapp.models import *

fake = Faker()


# Adding customers to db

list_of_allergens = ['celery', 'egg', 'fish', 'garlic', 'milk', 'mustard', 
                     'peanut', 'rice', 'sesame', 'soy', 'wallnut', 'honey', 
                     'almond', 'apple', 'orange', 'avocado', 'pepper', 'gluten',  
]

# if __name__ == '__main__':

#     print("Populating database, table 'Customer'")
#     for _ in range(5):
#         name = fake.name().split()
#         customer_algs = random.sample(list_of_allergens, 4)
#         new_customer = Customer(first_name = name[0],
#                                 last_name = name[1],
#                                 email = fake.unique.ascii_email(),
#                                 allergens = customer_algs
#                                 )
        # print(new_customer)
        # new_customer.save()


# algs = Customer.objects.all().values_list('allergens', flat=True)


### getting customers allergens from Customer table
algs = Customer.objects.all().filter(id='1').values('allergens')
algs_2 = list(algs[0].values())
# print(algs_2[0])

### getting dish ingridients from Dishes table
dish = Dishes.objects.all().filter(id='4').values('dish')
dish_2 = list(dish[0].values())
# print(dish_2[0])


### compairing customers allergens to dishes ingridients

list_of_ingr = dish_2[0]
print(sorted(list_of_ingr))
allergen = algs_2[0]
print(sorted(allergen))

for j in range(len(allergen)):
    if allergen[j] in list_of_ingr:
        print("No")
        print(allergen[j])
        break
    else:
        pass



### Adding dishes to db

# list_of_ingridients = ['celery', 'egg', 'fish', 'garlic', 'milk', 'mustard', 
#                      'peanut', 'rice', 'sesame', 'soy', 'wallnut', 'honey', 
#                      'almond', 'apple', 'orange', 'avocado', 'pepper', 'pear',
#                      'shrimp', 'lamb', 'beef', 'coconut', 'mushrooms', 'bacon',
#                      'chilie', 'mayonnaise', 'corn', 'onion', 'turkey', 'cheese',
#                      'pork', 'salt', 'sugar', 'chicken', 'tomato', 'potato', 
#                      'spinach', 'radish', 'leek', 'pumpkin', 'beans', 'zucchini',
#                      'cucumber', 'kiwi', 'mango', 'blueberry', 'olives', 'lemon',
# ]

# if __name__ == '__main__':

#     print("Populating database, table 'Dishes'")
#     for _ in range(30):
#         name_1 = fake.language_name().split()
#         dish_ings = random.sample(list_of_ingridients, 6)
#         new_dish = Dishes(name = name_1[0],
#                         dish = dish_ings,
#                         )
        # print(new_dish)
        # new_dish.save()


### Adding restaurants to db

# dishes_for_restaurant = Dishes.objects.all()
# dishes_to_add = random.sample(dishes_for_restaurant, 10)
# print(dishes_for_restaurant)



# if __name__ == '__main__':

#     print("Populating database, table 'Restaurant'")
#     for _ in range(10):
#         name_1 = fake.language_name()
        
#         new_restaurant = Restaurant(name = name_1,
#                                 address = fake.address(),
#                                 )
#         print(new_restaurant)
#         new_restaurant.save()


list_of_rests = Restaurant.objects.all().values_list('id', flat=True)
# print(type(list(list_of_rests)))
list_of_dishes = Dishes.objects.all().all().values_list('id', flat=True)
# print(list_of_dishes)

if __name__ == '__main__':

    print("Populating database, table 'Menu'")
    for _ in range(70):
        restaurant_id_to_add = random.choice(list_of_rests)
        dish_id_to_add = random.choice(list_of_dishes)
        # Menu.restaurant_id.add(*restaurant_id_to_add)
        # Menu.objects.create(restaurant_id = restaurant_id_to_add, dish_id = dish_id_to_add)
        
        new_menu = Menu()
        new_menu.save()
        new_menu.restaurant_id.add(restaurant_id_to_add)
        new_menu.dish_id.add(dish_id_to_add)

        print(new_menu)
        # new_menu.save()


### Adding allergens to db
# if __name__ == '__main__':

#     print("Populating database, table 'Allergens'")
#     for i in range(len(list_of_allergens)):
#         name_1 = list_of_allergens[i]

#         new_allergen = Allergens(name = name_1,
#                         )
#         print(new_allergen)
#         new_allergen.save()


    




    
    

    