#1
# word = input('Type some word: ')
# word_dict = {}
# i = 0
# for f in word:
#      if f in word_dict:
#          a = word_dict[f]
#          a.append(i)
#      else: 
#          word_dict[f] = [i]
#      i += 1
# print(word_dict)


#2
items_purchase = {
                "Water": "$1",
                "Bread": "$3",
                "TV": "$1,000",
                "Fertilizer": "$20"
                }

wallet = "$300"
wallet2 = str(wallet)
wallet3 = int(wallet2.replace('$', ''))

variable = items_purchase.keys()
for i in variable:
    inew = items_purchase[i].replace(',', '')
    inew = int(inew.replace('$', ''))
    items_purchase[i] = inew

new_list = []
for i in items_purchase.keys(): 
    if wallet3 - items_purchase[i] >= 0: 
        new_list.append([i]) 
        wallet3 -= items_purchase[i]

if new_list == []:
    print('Nothing')
else:
    print(sorted(new_list))