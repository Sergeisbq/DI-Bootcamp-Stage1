# Create
a_list = []

b_list = [1,2,3,'a','b']

c_list = [1,2,3,'a', [5,6,'c', ['%']]]

a_string = 'ABC'

d_list = list(a_string) # -> ['A','B','C']

# Get/Retrieve
first_item = c_list[0]

last_item = c_list[-1]

between_items = c_list[1:4] # -> [2,3,'a']

c_list[-1][-1] # -> ['%']

c_list[-1][-1][0][0] # -> ['%']

c_list[-2:-1]

c_list[-2:]

# Update
b_list = [1,2,3,'a','b']

b_list.insert()

b_list.index('a')

idx = b_list.index('a')

b_list.insert(idx, '!')

b_list.insert(idx+1, '!')

b_list.append('c') # -> [1,2,3,'a','b','c']

# Delete
numbers = [5,2,7,3,8,0]
del numbers[-1]
numbers.pop(3)
del numbers[0]
deleted_item = numbers.pop()
deleted_item
# remove by index and save the removed item:
numbers.pop(3)
# remove by index without saving:
del numbers[4]
# remove by value:
numbers.remove(7)

sevens = [7,7,7,7,7,7,8]
while 7 in sevens:
    sevens.remove(7)


# Sorting
numbers = [5,2,7,3,8,0]
numbers.sort() # -> [0,2,3,5,7,8]
numbers.reverse() # -> [0,8,3,7,2,5]
numbers_sorted_asc = sorted(numbers)
numbers_sorted_desc = sorted(numbers, reverse=True)
