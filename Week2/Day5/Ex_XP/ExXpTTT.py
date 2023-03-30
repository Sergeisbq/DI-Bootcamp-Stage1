data = [['x','o','o'],['x','x','x'],['o',' ',' ']]
print(data[0][1])
data_2 = [['','',''],['','',''],['','','']]

def matrix_convert(data):
    for col in range(len(data[0])):
        for row in range(len(data)):
            if data[row][col] == 'x' and data_2[row][col] == '':
                data_2[row][col] = data[row][col]
            elif data[row][col] == 'o' and data_2[row][col] == '':
                data_2[row][col] = data[row][col]
                print(f"""
+  _ _ _  +\n
+ |{data[0][0]}|{data[0][1]}|{data[0][2]}| +\n
+ |{data[1][0]}|{data[1][1]}|{data[1][2]}| +\n
+ |{data[2][0]}|{data[2][1]}|{data[2][2]}| +\n
+  - - -  +\n
"""
)

matrix_convert(data)

# print(f"""
# +  _ _ _  +\n
# + |{data[0][0]}|{data[0][1]}|{data[0][2]}| +\n
# + |{data[1][0]}|{data[1][1]}|{data[1][2]}| +\n
# + |{data[2][0]}|{data[2][1]}|{data[2][2]}| +\n
# +  - - -  +\n
# """
# )


