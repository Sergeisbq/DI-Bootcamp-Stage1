filename = 'sample.txt'

text_lines = []
# r - reading
with open(filename, 'r') as file:
    text_lines = file.readlines()

print(text_lines)

new_str = 'In between\n'

text_lines.insert(2, new_str)

print(text_lines)

# w - writing
with open(filename, 'w') as file:
    text_lines = file.writelines(text_lines)


with open(filename, 'r') as file:
    text_lines = file.readlines()