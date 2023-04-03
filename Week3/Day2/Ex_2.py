password = 1234

while True:
    try:
        user_pass = int(input('type password: '))
        if user_pass == password:
            break
                
    except ValueError:
        print('Do not use char or float numbers')


# logged_in = False
# while not logged_in:
#     if:
#         logged_in = True
