with open('file_03.txt') as my_file:
    sum_salary = 0
    line_count = 0
    for line in my_file.readlines():
        if float(line[line.rfind(" "):]) <= 20000:
            print(line[:line.rfind(" ")])
        sum_salary += float(line[line.rfind(" "):])
        line_count += 1
    print(sum_salary/line_count)
        # medium_salary = /sum(1 for _ in my_file)
