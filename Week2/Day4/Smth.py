matrix = [
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    '^r!',
    ]

text = []

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        if matrix[row][col] == '3':
          text += ''
        elif matrix[row][col].isalpha() == True:
          text += matrix[row][col]
        elif matrix[row][col].isalpha() == False:
          text += ' '
        
text = ''.join(text)
splitted = ' '.join(text.split())
print(splitted)