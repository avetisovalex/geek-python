my_list = [1, 1, 2, 2, 4, 5, 7, 8, 8, 10, 11]
result = []
for item in my_list:
    if item not in result:
        result.append(item)
print(result)