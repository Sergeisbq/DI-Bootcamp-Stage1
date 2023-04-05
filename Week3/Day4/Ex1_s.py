from collections import Counter

filename = 'text_to_work.txt'


# read file line by line
with open(filename, 'r') as file:

    for n in range(5):
        line = file.readline()
        print(f'line {n}:', line)
        if line == '':
            break
    
    # while True:
    #     line = file.readline()
    #     print(line)
    #     if line == '':
    #         break

# read only the 5th line of the file
with open(filename, 'r') as file:

    lines = file.readlines(5)
    print(lines)


# read only 5 first characters of the line
with open(filename, 'r') as file:

    chars = file.readline(5)
    print(chars)


# read all the file and return it as a list of strings. Then split each word
lines = []
with open(filename, 'r') as file:
    text = file.read()
    text_list = text.split('\n')
    lines = text_list

print(lines)


# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
counter = Counter(lines)
print(counter.most_common(3))

print(lines.count("Darth"))
print(lines.count("Luke"))
print(lines.count("Lea"))


# Append your first name at the end of the file
to_append = '\nSergei\n'
with open(filename, 'a') as file:
    file.write(to_append)
print(lines)


# Append "SkyWalker" next to each first name "Luke"

lines_updated = []
for line in lines:
    if line == 'Luke':
        new_line = f'{line} Skywalker'
    else:
        new_line = line
    lines_updated.append(new_line)

with open(filename, 'w') as file:
    file.writelines(lines_updated + '\n')

print(lines_updated)

