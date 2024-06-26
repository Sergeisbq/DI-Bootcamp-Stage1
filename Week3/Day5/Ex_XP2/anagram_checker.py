class AnagramChecker():

    def __init__(self):
        self.words_list = []
        with open('sowpods.txt', 'r') as file:
            for line in file:
                self.words_list.append(line[:-1]) 
        return 

    def is_valid_word(self, word):
        word1 = word.upper()
        word2 = word1.split(' ')
        word_ok = True
        if len(word2) > 1:
            print('You should type only one word!')
            word_ok = False
        elif len(word2) == 1:
            word3 = word.isalpha()
            if word3 == False:
                print('Only letters is allowed')
                word_ok = False
        return word_ok


    def get_anagrams(self, word):
        word1 = word.upper()
        word_2 = list(word1)
        word_2.sort()
        words_to_compare = []

        for i in self.words_list:
            if len(i) == len(word1):
                words_to_compare.append(i)

        list_to_sort_2 = []
        list_to_sort_3 = []
        
        for i in words_to_compare:
            list_to_sort = []
            for letter_wl in range(len(i)):
                j = i[letter_wl]
                list_to_sort.append(j)
                list_to_sort.sort()
                if list_to_sort == word_2:
                    list_to_sort_2.append(i)
                    for k in list_to_sort_2:
                        if k not in list_to_sort_3:
                            list_to_sort_3.append(k)
                            l = word1
                            if l in list_to_sort_3:
                                list_to_sort_3.remove(l)
        return list_to_sort_3
