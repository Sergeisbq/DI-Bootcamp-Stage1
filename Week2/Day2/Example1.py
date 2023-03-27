list1 = [5, 10, 15, 20, 25, 50, 20]
list1.index(20)
idx = list1.index(20)
list1[idx] = 200
print(list1)

a_tuple = (10, 20, 30, 40)
a = a_tuple[0]
b = a_tuple[1]
c = a_tuple[2]
d = a_tuple[3]
print(a)
print(b)
print(c)
print(d)

user_in = input('Number: ')
user_in_int = int(user_in)

mult_table_range = 10

# for num in range(mult_table_range):
#     print(user_in_int * num)

out = ""
for num in range(mult_table_range + 1):
    result = user_in_int * num
    out += f"{user_in_int} X {num} = {result}\n"
    print(out)

# for i in range(1, 10):
#     i += i
#     print(i)

# num = 1
# while num < 11:
#     print(num)