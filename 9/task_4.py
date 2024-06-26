# К роботу Валли отправили «коллегу» Билли.
# Это его первая высадка на Марс,
# поэтому его тестируют в прямоугольном помещении размером 15 × 20 м.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# затем управление им передаётся оператору, то есть пользователю вашей программы.

# Программа спрашивает,
# в какую сторону оператор хочет направить робота:
# север (клавиша W), юг (клавиша S),
# запад (клавиша A) или восток (клавиша D).
# Оператор делает выбор,
# марсоход перемещается в эту сторону на один метр,
# а программа сообщает новую позицию робота.
# Если марсоход упёрся в стену,
# он не должен пытаться переместиться в сторону стены —
# в этом случае его позиция не меняется.

# Что нужно сделать
# Создайте программу для управления роботом Билли.

# Пример:
#
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: S
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: S
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
position_row = 19
position_column = 6

while True:
    user_input = input(f'[Программа]: '
                       f'Марсоход находится на позиции  {position_column}, '
                       f'{position_row}, введите команду:')
    print(f'[Оператор]: {user_input}')
    if user_input == 'A' or user_input == 'a':
        position_column -= 1
    elif user_input == 'D' or user_input == 'd':
        position_column += 1
    elif user_input == 'W' or user_input == 'w':
        position_row -= 1
    elif user_input == 'S' or user_input == 's':
        position_row += 1
    else:
        print('Incorrect input. The rower remains on the same position.')
    if position_row > 20:
        position_row = 20
    elif position_row < 0:
        position_row = 0
    elif position_column > 15:
        position_column = 15
    elif position_column < 0:
        position_column = 0
