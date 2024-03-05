# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
#
# Введите число: 1000
# Число наоборот: 0001
#
# Введите число: 0
# Программа завершена!
#
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
#
# Введите число: 1230
# Число наоборот: 321
#
# Кстати, нули, которые мы убрали, называются ведущими.
def reverse_number(num):
    reversed_num = str(num)[::-1]
    print(f'Число наоборот: {reversed_num}')


while True:
    try:
        num = input('Введите целое число: ')
        int(num)

        if num == '0':
            print('Программа завершена!')
            break

        reverse_number(num)

    except ValueError:
        print('Ошибка ввода. Попробуйте снова.')