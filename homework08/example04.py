class StockOverflowException(Exception):
    def __init__(self, used_capacity):
        self.used_capacity = used_capacity


class StockEmptyException(Exception):
    def __init__(self, used_capacity):
        self.used_capacity = used_capacity


class Stock:
    max_capacity: int
    used_capacity: int
    eq_list: dict

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.used_capacity = 0
        self.eq_list = {}

    def equipment_to_stock(self, my_equipment):
        self.used_capacity += 1
        if my_equipment.device_type in self.eq_list:
            self.eq_list[my_equipment.device_type] += 1
        else:
            self.eq_list[my_equipment.device_type] = 1
        print(f"Current capacity is {self.max_capacity - self.used_capacity}")
        if self.used_capacity >= self.max_capacity:
            raise StockOverflowException(self.used_capacity)

    def equipment_from_stock(self, my_equipment):
        self.used_capacity -= 1
        if my_equipment.device_type in self.eq_list:
            self.eq_list[my_equipment.device_type] -= 1

        print(f"Current capacity is {self.max_capacity - self.used_capacity}")
        if 0 >= self.used_capacity:
            raise StockEmptyException(self.used_capacity)


class Equipment:
    color: str
    weight: int
    device_type: str

    def __init__(self, color, weight, device_type):
        self.color = color
        self.weight = weight
        self.device_type = device_type


class Printer(Equipment):
    speed: int

    def __init__(self, color, weight, device_type, speed):
        super().__init__(color, weight, device_type)
        self.speed = speed


class Scanner(Equipment):
    resolution: int

    def __init__(self, color, weight, device_type, resolution):
        super().__init__(color, weight, device_type)
        self.resolution = resolution


class CopyMachine(Equipment):
    orientation: str

    def __init__(self, color, weight, device_type, orientation):
        super().__init__(color, weight, device_type)
        self.orientation = orientation


my_stock = Stock(10)

my_scanner = Scanner("white", 10, "scanner", 1000)
my_scanner1 = Scanner("white", 10, "scanner", 1000)
my_scanner2 = Scanner("white", 10, "scanner", 1000)
my_scanner3 = Scanner("white", 10, "scanner", 1200)
my_scanner4 = Scanner("white", 10, "scanner", 1000)
my_scanner5 = Scanner("white", 10, "scanner", 1000)
my_scanner6 = Scanner("white", 10, "scanner", 1000)
my_scanner7 = Scanner("white", 10, "scanner", 1000)
my_scanner8 = Scanner("white", 10, "scanner", 1000)
my_copy_machine = CopyMachine("white", 10, "copy_machine", "portrait")
my_printer = Printer("white", 10, "printer", 500)

try:
    my_stock.equipment_to_stock(my_scanner)
    my_stock.equipment_to_stock(my_scanner1)
    my_stock.equipment_to_stock(my_scanner2)
    my_stock.equipment_to_stock(my_scanner3)
    my_stock.equipment_to_stock(my_scanner4)
    my_stock.equipment_to_stock(my_scanner5)
    my_stock.equipment_to_stock(my_scanner6)
    my_stock.equipment_to_stock(my_scanner7)
    my_stock.equipment_to_stock(my_scanner8)


    my_stock.equipment_to_stock(my_printer)
    my_stock.equipment_to_stock(my_copy_machine)
except StockOverflowException as exc:
    print(f"Reached maximum capacity of the stock: {exc}")

try:
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)
    my_stock.equipment_from_stock(my_scanner4)

except StockEmptyException as exc:
    print(f"Stock is already empty")
