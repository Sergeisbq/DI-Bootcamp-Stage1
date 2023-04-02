class Cat:

    cats = []

    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        Cat.cats.append(self)

    # dunder - double underscore / magic metgods
    def __str__(self) -> str:
        return self.name

cat1 = Cat('Mizzy', 5)
cat2 = Cat('Patsy', 7)
cat3 = Cat('Sky', 3)

def oldest_cat(cat_list: list) -> Cat:
    
    oldest = cat_list[0]
    for cat in cat_list:
        if cat.age > oldest.age:
            oldest = cat
    
    return oldest

# cats = [cat1, cat2, cat3]

cats = Cat.cats
oldest = oldest_cat(cats)
print(oldest)