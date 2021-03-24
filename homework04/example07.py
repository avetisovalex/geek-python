from math import factorial

user_number = int(input("input number >>>"))
result_list = []


def fact(n):
    for item in range(1, n+1):
        yield factorial(item)


count = 0
for el in fact(user_number):
    if count > user_number:
        break
    print(el)
    count += 1
