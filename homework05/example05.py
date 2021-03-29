with open('file_05.txt', 'w') as my_file:
    my_file.write(input("input some numbers divided by spaces >>>" + " "))

with open('file_05.txt', 'r') as my_file:
    print(sum(list(map(int, (my_file.readline()).split()))))
