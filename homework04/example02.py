from random import randint

user_list = []
list_length = int(input("input amount of numbers in list >>>"))
for i in range(list_length):
    user_list.append(randint(-100, 100))
print(user_list)
# user_list = map(int, input("input some numbers >>>").split())
tmp = 0  # variable which is used to compare values
result_list = []
for item in user_list:
    if item > tmp:
        result_list.append(item)
    tmp = item
print(result_list[1::])
