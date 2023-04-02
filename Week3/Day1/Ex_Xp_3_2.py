class Cat:

    cats = {}

    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        Cat.cats[self.name] = self

    # dunder - double underscore / magic metgods
    def __str__(self) -> str:
        return self.name

cat1 = Cat('Mizzy', 5)
cat2 = Cat('Patsy', 7)
cat3 = Cat('Sky', 3)

def oldest_cat(cat_dict: dict) -> Cat:
    
    oldest = max(cat_dict, key=lambda cat: cat.age)
    return oldest
    


cats = Cat.cats
oldest = oldest_cat(cats)
print(oldest)


# class Cat:

#     cats = []

#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#         Cat.cats.append(self)

#     # dunder - double underscore / magic metgods
#     def __str__(self) -> str:
#         return self.name

# cat1 = Cat('Mizzy', 5)
# cat2 = Cat('Patsy', 7)
# cat3 = Cat('Sky', 3)

# def oldest_cat(*cats) -> Cat:
    
#     oldest = max(cats, key=lambda cat: cat.age)
#     return oldest
    


# cats = Cat.cats
# oldest = oldest_cat(cats)
# print(oldest)