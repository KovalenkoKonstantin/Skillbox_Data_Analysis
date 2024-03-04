# Вы встретились со своим старым другом,
# который тоже изучает программирование, правда, в другом учебном заведении.
# За чашкой кофе он пожаловался вам,
# что сумасбродный препод дал им задание написать программу,
# которая из двух введённых чисел определяет наибольшее,
# не используя при этом условные операторы,
# циклы и встроенные функции вроде max/min/sorted.
#
# Радуясь, что на вашем курсе такого не требуют,
# вы всё-таки решаете помочь своему другу.
#
# Напишите для него эту программу.
#
# Пример:
#
# Введите первое число: 10
# Введите второе число: 5
#
# Наибольшее число: 10
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

print(f'Наибольшее число: '
      f'{(first_number + second_number + abs(first_number - second_number)) / 2}')
