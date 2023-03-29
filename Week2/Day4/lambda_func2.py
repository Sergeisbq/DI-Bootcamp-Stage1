numbers = [1,2,3,4,5,6,7,8]

#1
multiply_2 = lambda num: num * 2
result_list = list(map(multiply_2, numbers))
print(result_list)

#2
result_list = list(map(lambda num: num * 2, numbers))
print(result_list)


##
words = ['dog', 'cat', 'ball']
result_list_2 = list(map(lambda i: i.capitalize(), words))
print(result_list_2)