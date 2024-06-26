# Задача 1. Python!
# Напишите программу, которая выводит в отдельную строчку каждый символ фразы “Python!”.
#
#
#
phrase = "Python!"
for symbol in phrase:
    print(symbol)

# Задача 2. Вирус
# Ваня экспериментирует с различного рода компьютерными вирусами,
# которые портят жизнь людям.
# На просторах Интернета он нашёл код довольно необычного вируса,
# который “поворачивает” весь текст в документе
# и повторяет каждый символ 3 раза.
#
# Пользователь вводит текст. Напишите программу,
# которая выводит каждый символ текста в отдельной строке и три раза.
#
# Пример:
#
# Введите текст: Привет!
#
# ППП
#
# ррр
#
# иии
#
# ввв
#
# еее
#
# ттт
#
# !!!
#
#

# Без разворота по условию задачи:
phrase_in = input("Введите текст: ")
for symbol in phrase_in:
    print(symbol * 3)

# С разворотом(с использованием не изученных пока срезов):
phrase_in = input("Введите текст: ")
for symbol in phrase_in[::-1]:
    print(symbol * 3)

# Задача 3.
# Мы входим в команду разработки нового текстового редактора
# и нам поручили разработать для него подсчёт нужного символа в тексте,
# а именно - буквы Ы. Причём отдельно с верхним регистром и отдельно с нижним.
#
# Напишите программу,
# которая считает количество больших
# и количество маленьких букв Ы в тексте и выводит ответ на экран.
#
# Пример:
#
# Введите текст: Прыг скок
#
# Больших букв Ы: 0
#
# Маленьких букв Ы: 1

upper_letter = "Ы"
lower_letter = "ы"
upper_count = 0
lower_count = 0

phrase_in = input("Введите текст: ")
for symbol in phrase_in:
    if symbol == upper_letter:
        upper_count += 1
    elif symbol == lower_letter:
        lower_count += 1

print("Больших букв Ы: ", upper_count)
print("Маленьких букв Ы: ", lower_count)
