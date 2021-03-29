def translate(input_string):
    vocabulary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять"}
    if input_string in vocabulary.keys():
        return vocabulary.get(input_string)
    else:
        return "can't translate"


with open('file_04.txt') as my_file:
    for line in my_file.readlines():
        print(translate(line[:line.find(" ")]))
