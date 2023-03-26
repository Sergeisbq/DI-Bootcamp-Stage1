string = input('Type string: ')
num = int(string)
if 1 <= num <= 2 or num == 12:
    print('It is winter')
elif 3 <= num <= 5:
    print('It is spring')
elif 6 <= num <= 8:
    print('It is summer')
elif 9 <= num <= 11:
    print('It is autumn')
else:
    print('It is not about season:)')