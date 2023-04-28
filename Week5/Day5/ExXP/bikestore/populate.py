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

rental_list = Rental.objects.all()
# for r in rental_list:
#     print(r.id)



### fake date 1
# for _ in range(0, 100):
    # fake_date = fake.date_between_dates(date_start=datetime(2021,4,1), date_end=datetime(2023,4,27))
    # if fake_date.day == 7 or fake_date.day == 15 or fake_date.day == 24:
    #     fake_date = None
    #     print(fake_date)

# print(random.choice(vehicle_list))
###

### fake date 2
# m = []
# for k in range(0, 100):
#     i = random.randint(0, 43)
    
#     if i not in m:
#         m.append(i)
#     else:
#         pass
        
# print(m)
### 

### fake date 1 + fake date 2
# for _ in range(0, 30):
#     fake_date = fake.date_between_dates(date_start=datetime(2021,4,1), date_end=datetime(2023,4,27))
       
#     fake_date_2 = fake.date_between_dates(date_start=fake_date, date_end=datetime(2023,4,28))
#     if fake_date_2.day == 7 or fake_date_2.day == 15 or fake_date_2.day == 24:
#         fake_date_2 = None

#     print(fake_date, fake_date_2)
###


h = []
m = []
k = {}
l = {}
vehicle_list = Vehicle.objects.all()
customer_list = Customer.objects.all()
customer_list_rental = Rental.objects.all()
new_rental_1 = {}
# customer_1 = random.choice(customer_list)
# print(customer_1)
# fake_date = fake.date_between_dates(date_start=datetime(2021,4,1), date_end=datetime(2023,4,27))
# fake_date_2 = fake.date_between_dates(date_start=fake_date, date_end=datetime(2023,4,28))

# if fake_date_2.day == 7 or fake_date_2.day == 15 or fake_date_2.day == 24:
#     fake_date_2 = None
# l[fake_date] = fake_date_2



# for _ in range(100):
#     for k,v in l.items():
#         customer_1 = random.randint(0, 50)
#         fake_date_3 = fake.date_between_dates(date_start=datetime(2021,4,1), date_end=datetime(2023,4,27))
#         fake_date_4 = fake.date_between_dates(date_start=fake_date, date_end=datetime(2023,4,28))
#         h.append(customer_1)
#         if customer_1 in h and k < fake_date_3 < v and k < fake_date_4 < v:
#             pass
#         else:
#             customer_2 = customer_1

#         # print(customer_2)



#     print(customer_2)

if __name__ == '__main__':

    print("Populating RentalTable")
    for _ in range(100):
        # name = fake.name().split()
        
        fake_date = fake.date_between_dates(date_start=datetime.datetime(2022,4,1), date_end=datetime.datetime(2023,4,28))
        fake_date_2 = fake_date + datetime.timedelta(days = random.randint(1, 10))
        day = datetime.datetime(2023,4,28)

        
        
        
        

        l[fake_date] = fake_date_2
        
        for k,v in l.items():
            customer_1 = random.choice(customer_list)
            vehicle_1 = random.choice(vehicle_list)
            fake_date_3 = fake.date_between_dates(date_start=datetime.datetime(2022,4,1), date_end=datetime.datetime(2023,4,27))
            fake_date_4 = fake.date_between_dates(date_start=fake_date_3, date_end=datetime.datetime(2023,4,28))
            h.append(customer_1)
            m.append(vehicle_1)
            
            # if v is None:
            #     pass
            # elif v is not None:
            # if customer_1 in h or vehicle_1 in m and k < fake_date_3 < v or k < fake_date_4 < v:
            #     pass
                

        if fake_date_2 > day.date():
            fake_date_2 = None
            # if v is None:
            #     pass
            # else:
            #     if vehicle_1 in m and k < fake_date_3 < v and k < fake_date_4 < v:
            #         pass
            #     else:
            #         vehicle_2 = vehicle_1

        

            
    # new_rental_1['rental_date'] = [fake_date],
    # new_rental_1['return_date'] = [fake_date_2]
    # new_rental_1['customer'] = [customer_2]
    # new_rental_1['vehicle'] = [vehicle_2]

    # print(new_rental_1)

            

        # for r in rental_list:
        #     vehicle_1 = random.randint(0, 43)
                
        #     if vehicle_1 in m and r.rental_date < fake_date < r.return_date and r.rental_date < fake_date_2 < r.return_date:
        #         pass
        #     else:
        #         vehicle_2 = vehicle_1
        #     m.append(vehicle_1)
        # print(m)


        

        # for p in rental_list:
        #     customer_1 = random.randint(0, 100)
                
        #     if customer_1 in h and p.rental_date < fake_date < p.return_date and p.rental_date < fake_date_2 < p.return_date:
        #         pass
        #     else:
        #         customer_2 = customer_1
        #     h.append(customer_1)
        # print(l)
        # for i in range(len(l)):
        #     for k,v in l.items():
                
        #         print(k, v)
                # print(v[i.date])
        # m = h[0]
        # n = fake.date_between_dates(date_start=h[0], date_end=h[1])
        # print(h[0], n, h[1])
        # print(h[0], n, h[1])
            
        


        
        # if fake_date_2 = None


        # print(customer_list)
        new_rental = Rental(rental_date = fake_date, #
                            return_date = fake_date_2, #
                            customer = customer_1, #
                            vehicle = vehicle_1,
                            )
        print(new_rental)


        new_rental.save()

    
    

    