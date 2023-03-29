def generate_info() -> tuple[int, str]:
    return 30, 'A'

res = generate_info()

print(res)

num, letter = generate_info()
print(num)
print(letter)