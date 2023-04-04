class Object:

    number_objects_created = 0
    objects = {}

    def __init__(self) -> None:
        Object.objects[Object.number_objects_created] = self
        Object.number_objects_created += 1

    @classmethod
    def find_object(cls, id: int):
        if id in cls.objects:
            object_retrieved = cls.objects[id]
            print(object_retrieved)
            return cls.objects[id]
        else:
            print(f'No such object with id {id}')

Object()
Object()

Object.find_object(1)