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

j_list = []

def make_sentence():
    i = int(input("Type the length of sentence (from 2 to 20): "))
    for j in range(i):
        j = random.randint(1, len(text_lines) - 1)
        p = text_lines[j]
        j_list.append(p)

def main():
    '''
    This function creates a random sentence with users length 
    '''

make_sentence()

new_list = []
for p in range(len(j_list)):
    new_list.append(j_list[p].replace('\n', ''))
print(new_list)

sentence = str.join(" ", new_list).lower()
print(sentence)

