from translate import Translator

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
translator = Translator(from_lang="french",to_lang="english")

eng_words = []
for word in french_words:
    translation = translator.translate(word)
    eng_words.append(translation)
    
print(french_words)
print(eng_words)

x = dict(zip(french_words, eng_words))
print(x)