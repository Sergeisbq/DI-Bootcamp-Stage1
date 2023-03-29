def full_info(*info): #doesn't metter how many arguments you are going to put in
    out = ""
    for data in info:
        out += data + '\n'
    return out

print(full_info('Lea', '30'))