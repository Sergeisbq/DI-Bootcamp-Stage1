class Object:

    number_objects_created = 0
    objects = {}

    def __init__(self) -> None:
        Object.objects[Object.number_objects_created] = self
        Object.number_objects_created += 1
        

Object()
Object()
Object()
Object()
Object()

print(Object.number_objects_created)

print(Object.objects)
