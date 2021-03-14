myList = [7, 5, 3, 3, 2]
userNumber = int(input("input number >>>"))

myList.insert(len(myList) - myList[::-1].index(userNumber), userNumber)

print(myList)