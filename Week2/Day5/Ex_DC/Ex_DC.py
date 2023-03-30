data = input('Type some words dividing them by comma: ')

def sorting(data) -> str:
    for i, word in enumerate(data):
        data[i] = word.strip(' ')
    return sorted(data)

output = sorting(data.split(','))
print(output)