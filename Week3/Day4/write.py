text = '''This is the 1 line in the text\n
This is the 2nd
This is the 3rd
4th
...'''

text_list = text.split('\n')
print(text_list)

filename = 'sample.txt'

with open(filename, 'w') as file:
    # file.write(text)
    # file.writelines(text_list)
    for line in text_list:
        file.write(line + '\n')