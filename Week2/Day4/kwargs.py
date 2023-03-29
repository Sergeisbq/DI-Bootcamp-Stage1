def full_info(**kwargs):
    out = "FULL INFO\n---------\n"
    for key, value in kwargs.items():
        out += f'{key}: {value}\n'
    return out

print(full_info(first_name = 'Lea', country = 'IL'))