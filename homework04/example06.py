from itertools import count, cycle

user_number = int(input("input starting number >>>"))
user_counter = int(input("input final number >>>"))
for item in count(user_number):
    if item > user_counter:
        break
    else:
        print(item)

user_list = input("input some numbers >>>").split()
user_counter = int(input("input total amount of repeated numbers >>>"))
count = 0
for item in cycle(user_list):
    if count > user_counter:
        break
    print(item)
    count += 1
