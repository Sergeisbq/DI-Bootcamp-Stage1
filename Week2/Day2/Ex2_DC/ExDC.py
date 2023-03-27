result = []
number = input("Type a number: ")
value = int(number)
length = input("Type a multiplier: ")
multiplier = int(length)
j = 0
i = int(j)

while i < multiplier:
  result.append(value * (i+1))
  i += 1
print(result)


somestr = input("Type a text: ")
newlist = list(somestr)
i = 0

while i < len(newlist) - 1:
    if newlist[i] == newlist[i+1]:
        del newlist[i]
    else:
        i += 1

print(newlist)


