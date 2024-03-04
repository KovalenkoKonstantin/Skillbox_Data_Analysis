# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

knight_x = float(input('Введите местоположение коня:\n'))
knight_y = float(input(''))
point_x = float(input('Введите местоположение точки на доске:\n'))
point_y = float(input(''))

if 0 < knight_x < 0.8 and 0 < knight_y < 0.8 and 0 < point_x < 0.8 and 0 < point_y < 0.8:
    knight_x = int(knight_x * 10)
    knight_y = int(knight_y * 10)

    point_x = int(point_x * 10)
    point_y = int(point_y * 10)

    print(f'Конь в клетке ({knight_x}, {knight_y}). Точка в клетке ({point_x}, {point_y}).')
else:
    print('Клетки с такой координатой не существует')

if (abs(knight_x - point_x) == 1 and abs(knight_y - point_y) == 2)\
        or (abs(knight_x - point_x) == 2 and abs(knight_y - point_y) == 1):
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')
