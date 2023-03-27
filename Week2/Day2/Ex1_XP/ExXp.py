my_fav_numbers = {1,5,7,11}
my_fav_numbers.add(16)
my_fav_numbers.add(21)
my_fav_numbers.remove(21)
print(my_fav_numbers)
friend_fav_numbers = {2,4,6,8}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
del basket[0]
print(basket)
del basket[-1]
print(basket)
basket.append('Kiwi')
print(basket)
basket.index('Kiwi')
idx = basket.index('Kiwi')
basket.insert(idx-1, 'Apples')
print(basket)
counter = basket.count('Apples')
print(counter)
basket.clear()
print(basket)


a_list = []
for i in range(15, 55, 5):
    a = i/10
    print(a)


for num_even in range(1, 21):
    if num_even % 2 != 0:
        print(num_even)


while input("Username: ") != 'Sergei':
    input("Username: ")
    

str_fruits = input("Type your favorites fruits dividing them my space: ")
str_fruits_1 = str_fruits.split()
fruits_list = list(str_fruits_1)
print(fruits_list)
str_fruits_2 = input("Type fruit name: ")
str_fruits_3 = str_fruits_2.split()
fruits_list_2 = list(str_fruits_3)
a_set = set(fruits_list)
b_set = set(fruits_list_2)
c = b_set.intersection(a_set)
if c != 0: #Why it doesn't work with == True?
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')


counter = []
while True: 
  pizza_top = input("Type some toppings you'd like to add to pizza (when finish type 'quit'): ")
  if pizza_top == "quit":
    print(f"These toppings: {counter} are going to be in your pizza")
    print(f"Total prise is: {10 + len(counter) * 2.5}$")
    break
  else:
    counter.append(pizza_top)
    print(f" We'll add {pizza_top} to your pizza")


counter_2 = []
while True: 
  age_qest = input("How old are you? (when finish type 'quit'): ")
  if age_qest == "quit":
    print(counter_2)
    break
  else:
    counter_2.append(age_qest)


counter_2 = 0
while True: 
  age = input("How old are you? (when finish type 'quit'): ")
  if age == "quit":
    break
  age = int(age)
  if age >= 12:
    counter_2 = counter_2 + 15
  elif 3 <= age < 12:
    counter_2 = counter_2 + 10
  else:
    counter_2 = counter_2 + 0
print(f"{counter_2}$")


sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while sandwich_orders:
  sandwiches_inprogress = sandwich_orders.pop()
  finished_sandwiches.append(sandwiches_inprogress)
  print(f'I made your {sandwiches_inprogress}')


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

print('The deli has run out of pastrami')
while "Pastrami sandwich" in sandwich_orders:
  sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)


