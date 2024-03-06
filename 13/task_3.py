# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225
def reverse_number(num):
    return int(str(num)[::-1])


def sum_and_reverse(n, k):
    n_reverse = reverse_number(n)
    k_reverse = reverse_number(k)

    total = n_reverse + k_reverse
    total_reverse = reverse_number(total)

    return total_reverse


n = int(input('Введите первое число: '))
k = int(input('Введите второе число: '))


result = sum_and_reverse(n, k)
print()
print(f'Первое число наоборот: {reverse_number(n)}')
print(f'Второе число наоборот: {reverse_number(k)}')
print()
print(f'Сумма: {reverse_number(n) + reverse_number(k)}')
print(f'Сумма наоборот: {result}')
