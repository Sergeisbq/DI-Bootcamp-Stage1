# num = int(input('Type number: '))


# devisors = []
# for i in range(1500, 2500):
#     if i % 5 == 0 or i % 7 == 0:
#         devisors.append(i)
#     else:
#         pass
# print(devisors)


# if sum(devisors) == num:
#     print('Success')
# else:
#     print('Not for this number')



#2
# sentence = input('Type sentence: ')

# sent = list(sentence.split(' '))

# sent.reverse()
# sent2 = ' '.join(sent)
# print(sent2)


# num1 = int(input('Type number: '))
# num2 = int(input('Type number: '))
# num3 = int(input('Type number: '))

# if num1 < num2 and num3 < num2:
#     print(num2)
# elif num2 < num1 and num3 < num1:
#     print(num1)
# elif num1 < num3 and num2 < num3:
#     print(num3)


# some_list = input('Type number: ')
# sent = list(some_list.split(','))
# sent2 = tuple(some_list.split(','))
# print(sent)
# print(sent2)

# from collections import defaultdict  
# nums = defaultdict(int)  
# nums['one'] = 1  
# nums['two'] = 2
# nums['three'] = 3 
# print(nums['four'])

# import re

# name = input('Type your name: ')

# nums = re.findall(" ", name)

# if len(nums) == 1:
#     print(True)

# nums = re.findall("[A-Z]", name)

# if len(nums) <= 2:
#     print(True)

# nums = re.findall("[a-zA-Z]", name)

# nums2 = str(''.join(nums))
# nums3 = nums2.isalpha()
# print(nums3)

# param1 = tuple(input("Type your name, age and score: "))
# param2 = tuple(input("Type your name, age and score: "))
# param3 = tuple(input("Type your name, age and score: "))


# list1 = []

# while len(list1) <= 4:
#     param = (input("Type your name, age and score: "))
#     param2 = tuple(param.split(','))
#     list1.append(param2)
# list2 = sorted(list1)
# print(list2)



word = input("Type word: ")

word1 = word.upper()
word2 = word1.split(' ')
word_ok = True
if len(word2) > 1:
    print('You should type only one word!')
    word_ok = False
elif len(word2) == 1:
    word3 = word1.isalpha()
    if word3 == False:
        print('Only letters is allowed')
        word_ok = False

        
words_list = []
with open('sowpods.txt', 'r') as file:
    for line in file:
        words_list.append(line[:-1])
print(words_list)

words_to_compare = []
words_to_compare2 = []
for i in words_list:
    if len(i) == len(word1):
        words_to_compare.append(i)

word_2 = list(word1)
word_3 = word_2.sort()

print(words_to_compare)

list_to_sort_2 = []
for letter in range(len(word1)):
    for i in words_to_compare:
        list_to_sort = []
        for letter_wl in range(len(i)):
            j = i[letter_wl]
            list_to_sort.append(j)
            list_to_sort.sort()
            if list_to_sort == word_2:
                list_to_sort_2.append(i)
                list_to_sort_3 = []
                for k in list_to_sort_2:
                    if k not in list_to_sort_3:
                        list_to_sort_3.append(k)
                        l = word1
                        if l in list_to_sort_3:
                            list_to_sort_3.remove(l)
                        
                

            
            # if word1[letter] == i[letter_wl]:
            #     words_to_compare2.append(i)

# word_2 = list(word1)
# word_3 = word_2.sort()




print(word1)
print(list_to_sort_3)







# for letter in range(len(word1)):
#     print(word1[letter])
# for i in words_to_compare:
#     for letter_wl in range(len(i)):
#             print(i[letter_wl])
                    
