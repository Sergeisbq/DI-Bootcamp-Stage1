def multiply_add(num: int, limit: int):
    base = '1'
    res = 0

    for i in range(1, limit + 1):
        multiplicator = base * i
        multiplicator = int(multiplicator)
        res += num * multiplicator

    return(res)

print(multiply_add(3, 6))

    
