class Cell:
    amount: int

    def __init__(self, amount):
        self.amount = amount

    def make_order(self, items_in_row):
        result = ""
        for item in range(self.amount):
            if ((item % items_in_row) == 0) and (item != 0):
                result += "\n"
            result += "* "
        return result

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount > other.amount:
            return Cell(self.amount - other.amount)
        else:
            return "can't do that"

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(self.amount // other.amount)


my_cell = Cell(5)
another_cell = Cell(6)

print(my_cell.make_order(5))

print((my_cell + another_cell).make_order(2))

# trying to run make_order over diminishing cells
try:
    print((my_cell - another_cell).make_order(20))
# getting the error message if another_cell more that my_cell
except AttributeError:
    print(my_cell - another_cell)

print((my_cell * another_cell).make_order(3))

print((my_cell / another_cell).make_order(4))
