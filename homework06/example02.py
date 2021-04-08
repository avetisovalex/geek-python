class Road:
    _length: int
    _width: int
    mass = 25
    layer = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        print(self._length * self._width * self.mass * self.layer)


my_road = Road(5000, 20)
my_road.calculate()
