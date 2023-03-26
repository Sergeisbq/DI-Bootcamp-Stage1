import random
string = input('Type string: ')
firstchar = string[0]
lastchar = string[9]

if len(string) == 10:
    print(firstchar, lastchar)
elif len(string) < 10:
    print('string not long enough')
else:
    print('string too long')


for i in range(len(string)):
    new_str = list(string)
    random.shuffle(new_str)
    result = ''.join(new_str)
    print(result[:i+1])
