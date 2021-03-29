my_file = open(r'file_01.txt', 'w')

user_input = input("type smth >>>")

while user_input != "":
    my_file.writelines(user_input)
    user_input = input("type smth >>>")

my_file.close()
