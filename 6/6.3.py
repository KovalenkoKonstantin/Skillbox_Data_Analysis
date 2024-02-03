# Задача 1. Бегать — это полезно
#
# Представим, что у нас далёкое будущее и мы можем заниматься спортом на планетах
# со странными перепадами температур.
# Спортсмен бегает по стадиону до тех пор,
# пока температура на улице больше 15 градусов. Он пробегает 20 метров,
# затем температура падает на два градуса, и,
# если уже в этот момент она стала меньше либо равна 15 градусам,
# спорт сразу заканчивается.
# Если же всё в порядке, то он проходит пешком ещё 10 метров.
# Затем всё это повторяется.
#
# Напишите программу, которая спрашивает у пользователя,
# сколько на улице градусов, и, исходя из погоды,
# считает количество пройденных по стадиону метров и выводит ответ на экран.
#
#
#

# degrees = int(input("Сколько градусов на улице? "))
# metres = 0
# while degrees > 15:
#     metres += 20
#     degrees -=2
#     if degrees <= 15:
#         break
#     metres += 10
# print("Спортсмен прошёл", metres, "метров.")



# Задача 2. Расшифровка кода
#
# Нам нужно расшифровать определённый код в виде одного большого числа.
# Для этого нужно посчитать сумму цифр справа налево.
# Если мы встречаем в числе цифру 5, то выводим сообщение «Обнаружен разрыв»
# и заканчиваем считать сумму.
# В конце программы на экран выводится сумма тех цифр, которые мы взяли.
#
#
#

# number = int(input("Put the number: "))
# summ = 0    # initialized sum
# while number != 0:
#     # print(number)
#     last_digit = number % 10  # last digit of a number
#     if last_digit == 5:
#         print("Обнаружен разрыв")
#         break
#     summ += last_digit   # add last digit to the sum
#     number //= 10   # trimmed number
# print(summ)


# Задача 3. Начальная школа
#
# Авторы учебника по математике для второклассников очень любят всё усложнять.
# Например, отрицательные числа изучают только в пятом классе,
# а они всё норовят дать задачки на них во втором классе.
# Нам нужна программа, которая будет проверять,
# что в учебнике для второклашек не будет отрицательных чисел.
#
# Напишите программу, которая считывает числа до тех пор,
# пока не встретит отрицательное число.
# При появлении отрицательного числа программа завершается
# и показывает количество введенных чисел.
# Подумайте, обязательно ли здесь использовать оператор break.

# С break:
# input_number = int(input("Put a number: "))
# count: int = 1
# while True:
#     count += 1
#     if input_number < 0:
#         break
#     input_number = int(input("Put a number: "))
# print(count)


# Без break:

# input_number = int(input("Put a number: "))
# count: int = 1
# while input_number >= 0:
#     count += 1
#     input_number = int(input("Put a number: "))
# print(count)

# Задача 4. Ставки приняты, ставок больше нет
#
# Костя опять за старое!
# Только теперь он играет в кубики более надёжно,
# то есть на какую-то фиксированную сумму.
# И при этом пока что постоянно выигрывает!
# Однако по правилам это не мешает ему проиграть сразу всё.
#
# Напишите программу, которая запрашивает у пользователя начальное количество денег
# и, пока оно меньше 10 000,
# запрашивает число, которое выпало на кубике (от 1 до 6).
# Если на кубике выпало 3, то выводится сообщение «Вы проиграли всё!»,
# и деньги обнуляются. Если выпало другое число, к сумме прибавляется 500.
#
#
#
# Пример:
# Введите стартовую сумму: 5000
# Сколько выпало на кубике? 4
# Выиграли 500 рублей!
# Сколько выпало на кубике? 5
# Выиграли 500 рублей!
# Сколько выпало на кубике? 3
# Вы проиграли всё!
# Игра закончена.
# Итого осталось: 0 рублей
#
# Пример 2:
# Введите стартовую сумму: 9700
# Сколько выпало на кубике? 4
# Выиграли 500 рублей!
# Игра закончена.
# Итого осталось: 10200 рублей

money = int(input("Put amount of the money: "))
while money < 10000:
    gambling_number = int(input("What's the number? :"))
    while 1 > gambling_number or gambling_number > 6:
        gambling_number = int(input("wrong number, revalidate the number: "))
    if gambling_number == 3:
        print('You lose everything.')
        print('Game is over.')
        money = 0
        break
    print('You win')
    money += 500
print('Total amount of money:', money)


# \n - символ перехода на новую строку, его можно использовать
# чтобы перенести часть строки на новую строку при выводе в консоль.
