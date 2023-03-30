from copy import deepcopy 

def player_input(player, play_field):
    print(f"Player '{player}'")
    pos=''
    while not pos:
        pos=input("Enter your coordinates for your move. (Format: line/column):")
        x,y=tuple(pos.split('/'))
        x=int(x)
        y=int(y)

        if x>3 or y>3:
            print('Coordinates cannot be greater than 3.\nPlease try again')
            pos=''
        if play_field[y-1][x-1]:
            print('Choose an empty position to move.\nPlease try again')
            pos=''
    play_field[y-1][x-1]=player
    print (f"X={x}  Y={y}")

def check_win(matrix:list) -> str:
    results = ''
    for i in range(0, len(matrix)):
        if (matrix[i][0] == matrix[i][1] == matrix[i][2] !=""):
            results = matrix[i][0]
            break
        else:       
            for y in range(0, len(matrix)): 
                if (matrix[0][y] == matrix[1][y] == matrix[2][y] !=""):
                    results = matrix[0][y]
                    break
                elif (matrix[0][0] == matrix[1][1] == matrix[2][2] !=""):
                    results = matrix[0][0]
                    break
                elif (matrix[2][0] == matrix[1][1] == matrix[0][2] !=""):
                    results = matrix[2][0]
                    break
                else:
                    results = "z"
    return(results)            

def display_board(data:list):
    data_2=deepcopy(data)
    for col in range(len(data_2[0])):
        for row in range(len(data_2)):
            if data_2[row][col] == '':
                data_2[row][col] = ' '
    print(f"""
+  _ _ _  +\n
+ |{data_2[0][0]}|{data_2[0][1]}|{data_2[0][2]}| +\n
+ |{data_2[1][0]}|{data_2[1][1]}|{data_2[1][2]}| +\n
+ |{data_2[2][0]}|{data_2[2][1]}|{data_2[2][2]}| +\n
+  - - -  +\n
"""
)

play_field=[['','',''],['','',''],['','','']]
w='z'
display_board(play_field)
player='x'
while w=='z' and ('' in [n for p in play_field for n in p]):
    player_input(player, play_field)
    res=check_win(play_field)
    if res in ['o','x']:
        print(f"The winner is {res}")
        break
    if player=='x':
       player='o'
    else:
        player='x'
    display_board(play_field)


        