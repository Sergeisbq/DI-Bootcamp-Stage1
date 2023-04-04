class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def str(self) -> str:
        return str(f'{self.amount} {self.currency}')
    def int(self) -> int:
        return self.amount
    def __iadd__(self, other_cur):
        if type(self) == type(other_cur):
            if self.currency == other_cur.currency:
                self.amount += other_cur.amount
                return f'{self.amount} {self.currency}'
            else:
                print('It is not possible to addition different currencies')
        elif type(other_cur) == int:
            self.amount += other_cur
            return f'{self.amount} {self.currency}'

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

Currency.str(c1)
print(Currency.str(c1))
print(Currency.int(c1))

# c1 += 25
# print(c1)

c1 += c2
print(c1)
