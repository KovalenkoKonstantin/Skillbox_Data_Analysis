# Напишите функцию, вычисляющую наибольший общий делитель двух чисел
import math


def calculate_gcd(a, b):
    print(f'Наибольший общий делитель чисел {a} и {b} это число {math.gcd(a, b)}')


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
calculate_gcd(a, b)
