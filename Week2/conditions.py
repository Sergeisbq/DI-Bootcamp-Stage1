sun = 'up'

if 2 != 2 or sun == 'up':
    # or - at least 1 condition returns true
    print("Equal")

if 2 != 2 and sun == 'up':
    # and - all of the conditions returns true
    # identation (4 spaces)
    print("Equal")

apple = 'yellow'
winner = True

if apple == 'red' or winner == False:
    print('Red')
else:
    print('All is False')


if apple == 'red':
    print('Apple RED')
elif winner == True: # elif (else if) takes the previous if in account
    print('Winner True')
else:
    print('ALL IS FALSE')