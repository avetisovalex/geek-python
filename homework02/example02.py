myList = list(map(int, input("type some numbers >>>").split()))

for i in range(0, (len(myList) - 1), 2):
    swap = myList[i]
    myList[i] = myList[i + 1]
    myList[i + 1] = swap

print(myList)
