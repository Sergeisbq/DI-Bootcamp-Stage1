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
    print(string[:i+1])


new_list = list(string)
random.shuffle(new_list)
result = ''.join(new_list)
print(result)