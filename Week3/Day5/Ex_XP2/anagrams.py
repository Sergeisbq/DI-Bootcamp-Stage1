import anagram_checker

choice = ''
word_check = anagram_checker.AnagramChecker()

while choice != '2':
    choice = input("""
This is an anagram checker

  **********************
      1. Type a word
      2. Exit
  **********************
    """)
    if choice == '1':
        word_ok = False
        while not word_ok:
            word = input('Type a word: ') 
            word = (word.upper()).strip()
            word_ok = word_check.is_valid_word(word)
        words = word_check.get_anagrams(word)
        if words:
            print('''
                YOUR WORD :”{word}”
              this is a valid English word.
            Anagrams for your word: {words}.
            ''')

            

