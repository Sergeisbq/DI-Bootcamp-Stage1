
from func import addition as ad
import random
import string
from datetime import date, datetime, timedelta
from faker import Faker


ad(5, 3)

def randomize_compare() -> int:
    num2 = random.randint(1, 100)
    while True:
        num = int(input("Type number from 1 to 100: "))
        if num != num2:
            continue
        elif num == num2:
            print("They are the same")
            break


# randomize_compare()

print(''.join(random.choices(string.ascii_letters, k=5)))
print(date.today())

date1 = datetime(2023, 1, 1)
date2 = datetime.now()
diff = date2 - date1
print(diff)

date3 = date(1990, 12, 16)
diff2 = date.today() - date3
# diff3 = datetime.now - datetime(2023, 4, 4)
print(diff2)
seconds_bd = timedelta.total_seconds(date.today() - date3) / 60
print(seconds_bd)

date4 = date(2023, 4, 5)
diff3 = date4 - date.today()
print(diff3)

age_on_mars = seconds_bd * 11.862615
print(age_on_mars)


users=[]
fake=Faker()
for i in range(3):
    name=fake.name()
    addres=fake.address()
    language=fake.language_code()
    users.append({'name':name, 'addres':addres, 'language':language})
print (users)