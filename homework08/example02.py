class DivisionByZeroException(Exception):
    def __init__(self, divider):
        self.divider = divider

    def __str__(self):
        return f"Divider can't be 0. You entered {self.divider}"


def division(dividend, divider):
    if divider == 0:
        raise DivisionByZeroException(divider)
    return dividend / divider


a, b = map(int, (input("Type 2 numbers. We'll try to divide 1st by 2nd >>>")).split())

try:
    print(division(a, b))
except DivisionByZeroException as exc:
    print(exc)