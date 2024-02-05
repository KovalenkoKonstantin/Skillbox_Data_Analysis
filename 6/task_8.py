# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: При желании найдите описание алгоритма бинарного поиска
# и попробуйте применить в этой задаче.
# Разбор подобного решения будет в следующем модуле.
import random

boy_number = random.randint(1, 100)
# print(boy_number)
computer_guess = 0
counter_of_guesses = 0
while computer_guess != boy_number:
    computer_guess = int(input('Введите число: '))
    counter_of_guesses += 1
    if computer_guess > boy_number:
        print('3 — меньше')
        continue
    elif computer_guess < boy_number:
        print('2 — больше')
        continue
print('1 — равно! Число попыток: ', counter_of_guesses)
