# Задача 1. Космические рейнджеры
#
# В далеком (а может и не очень) будущем на некоторой планете можно купить
# космический корабль за пол-кредита (CR).
# Один CR это 2200 чатлов.
# Причем чатлы неделимы и являются всегда целым числом.
# Напишите простую программу-конвертор валют.
# В программу вводится количество чатлов,
# а она сообщает сколько это CR и сколько кораблей можно купить на эту сумму.
#
# Пример 1:
#
# Сколько чатлов? 3150
# Это 1.4318181818181819 CR
# Можно купить кораблей: 2
#
# Пример 2:
# Сколько чатлов? 4400
# Это 2.0 CR
# Можно купить кораблей: 4
#
#

chatles = int(input("Сколько чатлов? "))
cr_convert_coef = 1 / 2200
cr_out = chatles * cr_convert_coef
print("Это", cr_out, "CR")
ship_price = 0.5
ships_can_buy = int(cr_out / ship_price)
print("Можно купить кораблей:", ships_can_buy)

# Задача 2. Компьютерное зрение
#
# Вы участвуете в разработке робота,
# который играет в шахматы на реальной,
# физической шахматной доске размером 0.8 х 0.8 метра.
# Робот смотрит камерой на доску и видит расположение фигур
# в вещественных числах с очень высокой точностью.
#
# Напишите программу, в которую вводятся вещественные координаты шахматной фигуры,
# а программа определяет в какой клетке доски находится эта фигура.
# Каждая клетка доски имеет размер 10х10 см и
# целочисленные координаты, состоящие из двух чисел.
# Например левая верхняя клетка имеет целые координаты (0, 0),
# справа от неё клетка (1, 0) а снизу (0, 1).
# Также обеспечьте контроль ввода: нельзя выходить за границы доски.
#
# Пример:
#
# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.149
#
# Фигура находится в клетке (7, 1)
#
# Введите местоположение фигуры
# По горизонтали: 0.833
# По вертикали: -0.132
#
# Клетки с такой координатой не существует
#
#


x_coord = float(input("По горизонтали: "))
y_coord = float(input("По вертикали: "))
if 0 < x_coord < 0.8 and 0 < y_coord < 0.8:
    x_number = int(x_coord * 10)
    y_number = int(y_coord * 10)
    print("Фигура находится в клетке (", x_number, ",", y_number, ")")
else:
    print("Клетки с такой координатой не существует")

# Задача 3. Точность и аккуратность
#
# Робот из задачи “Компьютерное зрение” правильно определяет
# на какой клетке стоят фигуры. Но вот беда,
# часто по вине соперника-человека фигуры стоят на доске не ровно по центру клетки,
# а со смещением.
# Если во время игры такое смещение станет слишком велико,
# то станет непонятно в какой клетке стояла фигура.
# Чтобы избежать этой ситуации нужно чтобы робот поправлял фигуры на доске,
# выставляя их по центру клетки.
# Модифицируйте программу “Компьютерное зрение” так,
# чтобы она выдавала не только номера клетки,
# в которой находится фигура но и две вещественных поправки:
# на сколько нужно подвинуть фигуру по горизонтали и вертикали для того
# чтобы она оказалась по центру своей клетки.
#
# Пример:
#
# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.167
# Фигура находится в клетке (7, 1)
# Поправьте положение фигуры на (0.019, -0.017)

x_coord = float(input("По горизонтали: "))
y_coord = float(input("По вертикали: "))
if 0 < x_coord < 0.8 and 0 < y_coord < 0.8:
    x_number = int(x_coord * 10)
    y_number = int(y_coord * 10)
    print("Фигура находится в клетке (", x_number, ",", y_number, ")")
    center_x = x_number / 10 + 0.05
    center_y = y_number / 10 + 0.05
    delta_x = round(center_x - x_coord, 3)
    delta_y = round(center_y - y_coord, 3)
    print("Поправьте положение фигуры на (", delta_x, ",", delta_y, ")")
else:
    print("Клетки с такой координатой не существует")
