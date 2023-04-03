class Door:

    def __init__(self) -> None:
        self.is_opened = False

    def open(self):
        self.is_opened = True

    def close(self):
        self.is_opened = False

class BlockedDoor(Door):

    def open(self):
        func_name = open.__name__
        raise TypeError(f'{func_name}: Blocked Door can not be opened!')

    def close(self):
        raise TypeError('Blocked Door can not be closed!')
    
blocked = BlockedDoor()

d = {}
try:
    blocked.open()
    if d['Hello'] == 1:
        pass
except TypeError:
    print('Someone is trying to open a Blocked Door!')
except KeyError:
    print('Invalid Key!')

print('Something')