print('Hello world\n'*4)


print((99 ** 3)*8)


print(5 < 3)
print(3 == 3)
print(3 == "3")
# print("3" > 3)
print("Hello" == "hello")


computer_brand = "mac"
print("I have a " + computer_brand + " computer")


name = 'Sergei'
age = '32'
shoe_size = '43'
info = f"My name is {name}, I am {age} years old and my shoesize is {shoe_size}."
print(info)


a = 8
b = 6

if a > b:
    print('Hello World')


var = input('Provide number: ')
var_1 = int(var)
if var_1 % 2 == 0:
    print('even')
else:
    print('odd')


name = input('Type your name: ')
name_1 = str(name)
my_name = 'Sergei'
if name_1 == my_name:
    print("We are namesake")


height = input('Type your height in inches: ')
height_1 = float(height)
border = 145
border_1 = float(border)
height_2 = height_1 * 2.54
if height_2 > border_1:
    print('You are tall enough to ride')
else:
    print('You need to grow some more to ride')
