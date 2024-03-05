# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками
import math

input_number = float(input('Enter a positive float number: '))

# print(math.floor((input_number - math.floor(input_number)) * 10))
print(int(input_number * 10) % 10)
