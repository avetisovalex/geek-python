firstName = "John"
lastName = "Smith"
fullName = firstName + " " + lastName
fullNameFormat = f"{firstName} {lastName}"

print(fullName)
print(fullNameFormat)

template = "1234c5678"
countryCode = template[4]

print(countryCode)

passport = "1234567012"
passportSerial = passport[0:4]
passportNumber = passport[4:]

print(passportSerial, passportNumber)

reverseString = "123"
print(reverseString[::-1])
