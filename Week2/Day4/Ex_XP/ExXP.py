import random

#1
def display_message() -> str:
    return print("I'll learn - html, css, python, JavaScript")

display_message()


#2
def favorite_book(title) -> str:
    return print(f"One of my favorite books is {title}")

title = input("Type your favorite book: ")
favorite_book(title)


#3
def describe_city(city, country) -> str:
    return print(f"{city} is in {country}")

city = input("Type some city: ")
country = input("Type country where it located: ")
describe_city(city, country)


#4
def random_number(a) -> int | None:
    b = random.randint(1, 100)
    if 1 <= a < 100 and a != b:
        return print('They are different')
    elif a == b:
        return print('Success')
    else:
        return print('None')
    
random_number(5)


#5
def make_shirt(size: int, text: str):
    return print(f"The size of the shirt is {size}\nThe text is {text}")

make_shirt(38, 'Developer')


#6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician.title())
    
show_magicians(magician_names)

great_magicians = []
def make_great(magician_names):
    while magician_names:
        magician = magician_names.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        print(great_magician.title())

make_great(magician_names)


#7
def get_random_temp() -> int:
    season = int(input("Type current month number: "))
    if 1 <= season <= 2 or season == 12:
        i = random.randint(-10, 16)
    elif 3 <= season <= 5:
        i = random.randint(16, 23)
    elif 6 <= season <= 8:
        i = random.randint(32, 40)
    elif 9 <= season <= 11:
        i = random.randint(16, 23)
    else:
        return None
    return i

def main():

    t = float(get_random_temp())
    print(f'The temperature right now is {t} degrees Celsius.')
    if t < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif 0 <= t < 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= t < 23:
        print("It is the best temperature for walking")
    elif 23 <= t < 32:
        print("It is supposed to go to the beach")
    else:
        print("You should stay at home")
        
main()


