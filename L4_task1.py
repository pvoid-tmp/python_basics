# Lesson 4 task 1

from sys import argv

try:
    a0, salary_base, kpi, bonus, overtime_hours = argv
    base = float(salary_base)
    print(f"{base*0.6 + base*0.4*float(kpi) + float(bonus) + base/20/8*float(overtime_hours)*2:.2f} CHF")
except ValueError as e:
    print(e)
