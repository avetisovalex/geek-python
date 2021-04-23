class Date:
    date: str

    def __init__(self, date):
        Date.date = date

    @classmethod
    def given_date_to_int(cls):
        day = int(cls.date.split('-')[0])
        month = int(cls.date.split('-')[1])
        year = int(cls.date.split('-')[2])

        return day, month, year

    @staticmethod
    def validate(day: int, month: int, year: int):
        if day > 31:
            print("given day is incorrect")
        if month > 12:
            print("given month is incorrect")
        if (year > 2500) or (1900 > year):
            print("given year is incorrect")


new_date = "222-51-54000"

print(Date(new_date).given_date_to_int())

Date.validate(*Date(new_date).given_date_to_int())

