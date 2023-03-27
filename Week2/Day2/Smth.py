# p_top = input("Type some toppings you'd to add to pizza: ")
# while True: 
#   if p_top == "quit":
#     break
#   else:
#     print(p_top+"topping is added")


# counter = []
# while True: 
#   pizza_top = input("Type some toppings you'd like to add to pizza (when finish type 'quit'): ")
#   if pizza_top == "quit":
#     print(f"These toppings: {counter} are going to be in your pizza")
#     print(f"Total prise is: {10 + len(counter) * 2.5}$")
#     break
#   else:
#     counter.append(pizza_top)
#     print(f" We'll add {pizza_top} to your pizza")


# counter_2 = 0
# while True: 
#   age = input("How old are you? (when finish type 'quit'): ")
#   if age == "quit":
#     break
#   age = int(age)
#   if age >= 12:
#     counter_2 = counter_2 + 15
#   elif 3 <= age < 12:
#     counter_2 = counter_2 + 10
#   else:
#     counter_2 = counter_2 + 0
# print(f"{counter_2}$")




# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches = []

# while sandwich_orders:
#   sandwiches_inprogress = sandwich_orders.pop()
#   finished_sandwiches.append(sandwiches_inprogress)
#   print(f'I made your {sandwiches_inprogress}')

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# print('The deli has run out of pastrami')
# while "Pastrami sandwich" in sandwich_orders:
#   sandwich_orders.remove("Pastrami sandwich")
# print(sandwich_orders)

# result = []
# number = input("Type a number: ")
# value = int(number)
# length = input("Type a multiplier: ")
# multiplier = int(length)
# j = 0
# i = int(j)

# while i < multiplier:
#   result.append(value * (i+1))
#   i+=1
# print(result)



# for i in range(len(newlist)):
#     if [i] == [i+1]:
#         del newlist[i+1]
#         i += i
# print(newlist)

# somestr = input("Type a text: ")
# newlist = list(somestr)


# i = 0
# while i < len(newlist) - 1:
#     if newlist[i] == newlist[i+1]:
#         del newlist[i]
#     else:
#         i += i
# print(newlist)


somestr = input("Type a text: ")
newlist = list(somestr)
i = 0

while i < len(newlist) - 1:
    if newlist[i] == newlist[i+1]:
        del newlist[i]
    else:
        i += 1

print(newlist)

