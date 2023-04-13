import string

class AnagramChecker:

    def __init__(self):
        self.words_list = []
        with open('sowpods.txt', 'r') as file:
            for line in file:
                self.words_list.append(line) #[:-1]

    def is_valid_word(word):
        word1 = word
        word_ok = True


    def get_anagrams(word):
        pass

print(AnagramChecker.__init__)