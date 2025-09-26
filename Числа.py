import math
x = float(input("Введіть додатне дробове число: "))
integer_part = math.floor(x)
fractional_part = x - integer_part
print(f"Введене число: {x}")
print(f"Ціла частина: {integer_part}")
print(f"Дробова частина: {fractional_part}")
