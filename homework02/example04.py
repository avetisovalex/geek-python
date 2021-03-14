listWords = input("type some words >>>").split()
number = 0
for element in listWords:
    number += 1
    print(str(number) + " " + element[:10], end='\n')
