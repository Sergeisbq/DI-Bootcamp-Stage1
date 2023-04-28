import os
import django
from faker import Faker
import datetime
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikestore.settings')
django.setup()

from rent.models import *

fake = Faker()

# if __name__ == '__main__':

#     print("Populating database")
#     for _ in range(50):
#         name = fake.name().split()
        
#         new_customer = Customer(first_name = name[0],
#                                 last_name = name[1],
#                                 email = fake.unique.ascii_email(),
#                                 phone_number = fake.phone_number(),
#                                 address = fake.address(),
#                                 city = fake.city(),
#                                 country = fake.country(),
#                                 )
        
#         new_customer.save()


vehicle_list = Vehicle.objects.all()
# for v in vehicle_list:
#     print(v.id)

customer_list = Customer.objects.all()
# for v in customer_list:
#     print(v.id)


if __name__ == '__main__':

    print("Populating RentalTable")
    for _ in range(100):
        l = {}
        fake_date = fake.date_between_dates(date_start=datetime.datetime(2022,4,1), date_end=datetime.datetime(2023,4,28))
        fake_date_2 = fake_date + datetime.timedelta(days = random.randint(1, 10))
        day = datetime.datetime(2023,4,28)
        if fake_date_2 > day.date():
            fake_date_2 = None
        l[fake_date] = fake_date_2
        
        for k,v in l.items():
            customer_1 = random.choice(customer_list)
            vehicle_1 = random.choice(vehicle_list)

        new_rental = Rental(rental_date = fake_date, #
                            return_date = fake_date_2, #
                            customer = customer_1, #
                            vehicle = vehicle_1,
                            )
        print(new_rental)

        # new_rental.save()

    
    

    