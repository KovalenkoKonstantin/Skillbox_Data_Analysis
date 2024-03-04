# Задача 1. Герон
#
# Существует, так называемая, формула Герона,
# позволяющая вычислить площадь треугольника, зная длины его сторон.
#
# S= √ (p * (p - a)*(p - b)*(p - c)) ,где
#
# S - площадь;
# p - полупериметр треугольника (a+b+c)/2;
# a,b,c - длины сторон треугольника.
#
# Напишите программу,
# которая принимает на вход длины сторон треугольника и выводит его площадь
#
#
import math

a = float(input("Введите сторону а: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

p = (a + b + c) / 2

area_formula = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Площадь треугольника:", area_formula)

# Задача 2. Игра
#
# Мы решили написать 2D игру (вид сверху, игрок двигается в двух плоскостях).
# Первым делом надо написать управление персонажем
# - от игрока мы получаем пройденное расстояние и угол по которому он двигался и нам,
# зная эту информацию, нужно изменить текущие координаты (0, 0) на новые (х, у).
#
# Чтобы это сделать - нам нужно узнать сколько человек пройдёт расстояния по горизонтали
# (по оси Х - расстояние * косинус угла) и сколько
# он пройдет расстояния по вертикали (по оси У - расстояние * синус угла)
#
# Напишите программу, которая получает на вход расстояние и угол поворота.
# В результате выведите координаты нового местоположения игрока.
#
#

distance = float(input("Пройденное расстояние: "))

# Ввод угла
# функции cos/sin принимают на вход радианы,
# значит нужно сделать перевод, сделать это можно по-разному:

# Вариант 1:
angle = float(input("Угол поворота: "))
angle /= 57.2958

# Вариант 2:
angle = math.radians(float(input("Угол поворота: ")))

x_coord = distance * math.cos(angle)
y_coord = distance * math.sin(angle)

print("Координаты нового местоположения - (", x_coord, ",", y_coord, ")")

# Задача 3. Мега-калькулятор
#
# Кеша учится в третьем классе, и уже умеет программировать на питоне.
# Как и многие его одноклассники,
# он очень любит сразу применять все полученные знания на практике.
# Вчера Кеша узнал про модуль math и его основные возможности,
# поэтому решил написать мега-калькулятор,
# который бы применял сразу все функции к введенному пользователем числу.
# Чтобы ничего не забыть,
# он пользуется шпаргалкой, которую прикрепили к уроку
#
# Напишите программу, которая получает от пользователя вещественное число,
# по очереди применяет к нему функции модуля Math и выводит результат:
#
# округляет вниз
# округляет вверх
# берет модуль числа
# извлекает квадратный корень
# возводит экспоненту в степень, равную числу
# считает натуральный логарифм числа
# считает логарифм числа по основанию 2
# считает логарифм числа по основанию 10
# считает синус и косинус числа
# И так как Кеша самый умный в классе,
# он решил попробовать посчитать факториал числа.
# Для этого ему пришлось придумать и реализовать контроль ввода:
# факториал вычисляется, только если введенное число было натуральным.

user_number = float(input("Введите число: "))
print(math.floor(user_number))
print(math.ceil(user_number))
print(abs(user_number))
print(math.sqrt(user_number))
print(math.exp(user_number))
print(math.log(user_number))
print(math.log2(user_number))
print(math.log10(user_number))
print(math.sin(user_number), math.cos(user_number))
if user_number % 1 == 0:
    print(math.factorial(int(user_number)))
