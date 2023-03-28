numbers = []

for num in range(100):
    if num % 2 == 0:
        numbers.append(num)


        # what_to_add(2,4,6..) for number in range(100)
numbers = [num for num in range(100) if num % 2 == 0]
print(numbers)