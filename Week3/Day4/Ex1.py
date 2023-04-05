# Read the file line by line
# Read only the 5th line of the file
# Read only the 5th first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"


filename = 'text_to_work.txt'

text = ""
text_lines1 = []


# r - read
with open(filename, 'r') as file:
    # text = file.read()
    # text_lines1 = file.readlines()
    text_line2 = file.readline(5)

# print(text_lines1[])
print(text_line2)

file_obj = open(filename, "r")
  
# reading the data from the file
file_data = file_obj.read()
  
# splitting the file data into lines
lines = file_data.splitlines()
print(lines)

print(lines.count("Darth"))
print(lines.count("Luke"))
print(lines.count("Lea"))

new_line = 'Sergei'
# a - append
with open(filename, 'a') as file:
    file.write('Luke' + 'SkyWalker')

print(lines)
