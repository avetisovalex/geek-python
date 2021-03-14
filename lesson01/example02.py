# password = input("enter you password >>>")
#
# originalPassword = "correct"
#
# if originalPassword == password:
#     print("Correct")
# else:
#     print("incorrect")
#
age = int(input("input ur age >>>"))

if age >= 14:
    print("you can get a passport")

    if 20 <= age < 45:
        print("you can change ur passport")
elif age < 1:
    print("smth")
else:
    print("you can't get a passport")
