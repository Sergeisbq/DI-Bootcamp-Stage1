import random
filename = 'text.txt'

text_lines = []

with open(filename, 'r') as file:
    # text = file.read()
    text_lines = file.readlines()
    
def get_words_from_file():
    with open(filename, 'r') as file:
        text_lines = file.readlines()
    return text_lines

# def get_random_sentence():
#     i = int(input("Type the length of sentence (from 2 to 20): "))
#     return(i)

j_list = []


    
try:
    i = int(input("Type the length of sentence (from 2 to 20): "))
    if i > 20 or i < 2:
        print('You should type a number between 2 and 20')

except ValueError:
    print('You should type a number')
   
for j in range(int(i)):
    j = random.randint(1, len(text_lines))
    p = text_lines[j]
    j_list.append(p)
        
def main():
    '''
    This function creates a random sentence with users length 
    '''


# print(text)
# print(get_words_from_file())
# get_random_sentence()

print(j_list)
sentence = str.join('\n', j_list)
sentence2 = sentence.split('\n')
sentence3 = str.join(" ", sentence2)
print(sentence)
print(sentence2)
print(sentence3.lower())

