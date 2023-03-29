#1
word = input('Type some word: ')
word_dict = {}
i = 0
for f in word:
     if f in word_dict:
         b = word_dict[f]
         b.append(i)
     else: 
         word_dict[f] = [i]
     i += 1
print(word_dict)


#2