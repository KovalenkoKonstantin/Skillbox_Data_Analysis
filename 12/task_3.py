# Степан использует калькулятор для расчёта суммы и разности чисел,
# но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную,
# поэтому решил немного расширить функционал калькулятора.

# Напишите программу,
# запрашивающую у пользователя число и действие,
# которое нужно сделать с числом:
# вывести сумму его цифр,
# максимальную
# или минимальную цифру.

# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы,
# максимума и минимума при помощи аргументов.

def sum_of_digits(num):
    result = 0
    for digit in str(num):
        result += int(digit)
    print(f'Сумма цифр числа: {num} есть число {result}')


def maximum_digit(num):
    result = 0
    collection = []
    for digit in str(num):
        collection.append(int(digit))
        result = max(collection)
    print(f'Максимальная цифра числа: {num} есть число {result}')


def minimum_digit(num):
    result = 0
    collection = []
    for digit in str(num):
        collection.append(int(digit))
        result = min(collection)
    print(f'Минимальная цифра числа: {num} есть число {result}')


while True:
    try:
        num = int(input("Введите число: "))
        action = int(input("Выберите действие (1. сумма/ 2. максимум/ 3. минимум): "))

        if action == 1:
            sum_of_digits(num)
        elif action == 2:
            maximum_digit(num)
        elif action == 3:
            minimum_digit(num)
        else:
            print("Некорректное действие. Попробуйте снова.")

        continue_program = int(input("Хотите продолжить? (1. да/ 2. нет): "))
        if continue_program == 2:
            break
    except ValueError:
        print("Ошибка ввода. Попробуйте снова.")
