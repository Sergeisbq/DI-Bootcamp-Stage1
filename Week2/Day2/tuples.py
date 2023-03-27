# Create 
a_tuple = (1,2,3,4)
b_tupple = 1,2,3

# Get
personal_info = ('Yossi', 'Eik', 31, 'TLV')
personal_info[0]
personal_info[-1]

# Update
personal_info = ('Yossi', 'Eik', 31, 'TLV')
personal_info_list = list(personal_info)
personal_info_list[0] = 'Lea'
personal_info = tuple(personal_info_list)

# Delete - Not mutable, can't delete

# Dividing into multiple variables
func_output = 30, 100
type(func_output)
result1, result2 = 30, 100
first_name, last_name = input("First")
