class Person:

    def __init__(self, name) -> None:
        self.__name = name

    @property # makes a method act like an attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_value: str):
        self.__name = new_value


person = Person('David')
print(person.__dict__)
print(person.name)

# print(person.__name)

person.name = 'Ben'
print(person.name)
# print(person.name)