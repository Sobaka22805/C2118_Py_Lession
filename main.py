print("Hello World!")


class Pumpkin:
    color: str
    thinkness: int
    isAvailable: bool

    def __init__(self, color, tninkness, isAvailable = True):
        self.color = color
        self.thinkness = tninkness
        self.isAvailable = isAvailable

    def get_info(self):
        print('General Info:')
        if self.isAvailable:
            print(f'\tcolor-{self.color} | thk - {self.thinkness}')
        else:
            print('\tthis pumpkin is absent in storage, sorry')


pumpkinYellow = Pumpkin('Yellow', 12)
pumpkinYellow.get_info()
pumpkinOrange = Pumpkin('Orange', 10)
pumpkinOrange.get_info()
