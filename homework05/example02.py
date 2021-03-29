my_file = open('file_02.txt')

lines_amount = 0
for line in my_file.readlines():
    lines_amount += 1
    line = line.split()
    words_amount = len(line)
    print(words_amount)
print(lines_amount)

