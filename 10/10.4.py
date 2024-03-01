# Задача 1. Электронная очередь
#
# Нам дали заказ написать программу для электронной очереди.
# У каждого человека в очереди есть номер:
# нулевой, первый, второй, третий и так далее.
# Каждый час очередь уменьшается на одного человека,
# то есть уходит сначала нулевой номер, затем первый, второй и так далее.
# Наша программа получает на вход одно число
# — количество людей в очереди — и выводит на экран историю обслуживания очереди:
# какие номера в какой час оставались.
#

# human_count = int(input("Введите количество людей в очередь: "))
human_count = 5
for human_start in range(human_count + 1):
    print("Час:", human_start)
    for human_number in range(human_start, human_count):
        print(human_number, end='\t')
    print()

# Задача 2. Цифры больше пяти
#
# Пользователь вводит последовательность из N чисел. Напишите программу,
# которая подсчитывает общее количество цифр больше пяти во всей последовательности.

# n = int(input("Количество чисел в последовательности: "))
n = 5
cipher_count = 0
for _ in range(n):
    # new_number = int(input("Введите число: "))
    new_number = 6
    for element in str(new_number):
        if int(element) > 5:
            cipher_count += 1
    # while new_number:
    #     if new_number % 10 > 5:
    #         cipher_count += 1
    #     new_number //= 10

print(cipher_count)

# Задача 3. Лестница чисел
#
# Пользователь вводит число N. Напишите программу,
# которая по этому числу выводит вот такую лестницу из чисел:

# n = int(input("Введите число: "))
n = 5
for start in range(n + 1):
    for number in range(start, n + 1):
        print(number, end='\t')
    print()

print()
print(1356 // 10)  # отбросить последнюю цифру
print(1356 % 10)  # взять последнюю цифру
