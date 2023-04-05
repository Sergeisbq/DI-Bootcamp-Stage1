filename = 'sample.txt'

text = ""
text_lines1 = []
text_lines2 = []

# r - read
with open(filename, 'r') as file:
    # text = file.read()
    text_lines1 = file.readlines()
    file.seek(0)
    print(file.tell())
    text_lines2 = file.readlines()


# print(text)
print(text_lines1)
print(text_lines2)