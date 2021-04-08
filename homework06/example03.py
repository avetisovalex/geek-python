class Worker:
    firstname: str
    lastname: str
    position: str
    _income: dict
    wage: int
    bonus: int

    def __init__(self, firstname, lastname, position, income):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print("Name is " + self.firstname + " " + self.lastname)
        pass

    def get_total_income(self):
        print("Total income is " + str(sum(self._income.values())))
        pass


employee = Position("John", "Smith", "developer", {"wage": 500, "bonus": 5000})

employee.get_full_name()
employee.get_total_income()
