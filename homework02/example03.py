monthNumber = int(input("input number of month >>>"))

listWinter = [1, 2, 12]
listSpring = [3, 4, 5]
listSummer = [6, 7, 8]
listAutumn = [9, 10, 11]

if monthNumber in listWinter:
    print("it's Winter")
elif monthNumber in listSpring:
    print("it's Spring")
elif monthNumber in listSummer:
    print("it's Summer")
elif monthNumber in listAutumn:
    print("it's Autumn")
else:
    print("There are no such months!")

dictSeason = {1: "Winter", 2: "Winter", 12: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer",
              8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn"}
if monthNumber in dictSeason:
    print("it's " + dictSeason[monthNumber])
else:
    print("There are no such months!")
