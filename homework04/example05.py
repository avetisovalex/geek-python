from functools import reduce

my_list = [item for item in range(100, 1001) if item % 2 == 0]

print(reduce(lambda x, y: x * y, my_list))