from copy import deepcopy
data = [['','',''],['','',''],['','','']]

def matrix_convert(data):
    data_2 = deepcopy(data)
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
          


matrix_convert(data)
print(data)