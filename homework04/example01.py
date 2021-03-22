import sys


def salary_calc(worked_hours, salary_per_hour, bonus):
    return (float(worked_hours) * float(salary_per_hour)) + int(bonus)


try:
    file, user_worked_hours, user_salary_per_hour, user_bonus = sys.argv
except ValueError:
    print("invalid args")

print(salary_calc(user_worked_hours, user_salary_per_hour, user_bonus))
