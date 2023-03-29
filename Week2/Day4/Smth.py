import random

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