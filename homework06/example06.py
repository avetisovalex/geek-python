class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing")


class Pen(Stationery):
    def draw(self):
        print("Start drawing by pen")


class Pencil(Stationery):
    def draw(self):
        print("Start drawing by pencil")


class Handle(Stationery):
    def draw(self):
        print("Start drawing by handle")


my_pen = Pen("my_pen")
my_pencil = Pencil("my_pencil")
my_handle = Handle("my_handle")
my_stationery = Stationery("my_stationery")

my_pen.draw()
my_pencil.draw()
my_handle.draw()
my_stationery.draw()
