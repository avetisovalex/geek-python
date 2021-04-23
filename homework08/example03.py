class IsNumberException(Exception):
    def __init__(self, element):
        self.element = element

    def __str__(self):
        return "str was given instead of int"

list = []
a = ""
while a != "stop":
    try:
        a = input("input smth: >>>")
        if a.isdigit():
            list.append(a)
        else:
            raise IsNumberException(a)
    except IsNumberException as exc:
        print(exc)
print(list)
