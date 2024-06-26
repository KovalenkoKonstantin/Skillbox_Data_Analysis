r = 'Red'
g = 'Green'
b = 'Blue'
distinct = 'Red Blue Green RedGreenBlue Blue GreenBlue'

temp = r + ' ' + b + ' ' + g + ' ' + r + g + b + ' ' + b + ' ' + g + b

print(temp == distinct)

first_animal = 'Заяц'
second_animal = 'Черепаха'
print(first_animal, 'спит,', second_animal, 'идёт')

print('Задача 6. Обмен значений двух переменных')

# Что нужно сделать
# Дана программа, которая запрашивает у пользователя два слова, а затем выводит их на экран два раза.

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
# стереть эту строчку и вставить свой код здесь
print(a, b)

# Задача: поменять значения переменных a и b местами.
# Изменять, удалять, менять местами 6-ю, 7-ю, 8-ю и последнюю строчки нельзя.
# Но в 9-ю строку можно вставлять сколько угодно кода, не трогая последний принт.
# Пример результата работы программы:

# Введите первое слово: Сок
# Введите второе слово: Вода
# Сок Вода
# Вода Сок

# Начинаем решение!
# Сперва шаги:
# 1) У нас есть пример ввода вывода (тут сразу надо понимать, что код должен работать не только с названиями Сок и Вода, но и с любыми другими, которые будут введены в a,b). Сперва сравним то, что есть сейчас с тем, что надо получить.
# 2) У нас есть ограничения - нельзя трогать текущий код, последний вывод должен быть изменен новым кодом. Т.е. нам надо дописать что-то между принтами (можно дописывать много строк), чтобы второй принт после этого выводил названия в обратном порядке. Тут надо решить сперва без кода - что надо сделать между принтами, чтобы print(a,b) выводил слова в другом порядке.
# 3) Попробуем идею из №2 реализовать кодом

# №1 - посмотрим что сейчас выводит код:
# Введите первое слово: Сок
# Введите второе слово: Вода
# Сок Вода
# Сок Вода  -- отличия есть в этой строке, Сок и Вода выводятся в таком же порядке, как при первом принте

# №2
# раз мы не можем решить задачу "в лоб" - т.е. нельзя сделать так print(b,a)
# то нам надо поработать с самими переменными:
# 1) в 'a' надо записать то, что было в 'b'
# 2) в 'b' надо записать то, что было в 'a'

# №3
# Добавляем действия, которые придумали в код:
a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
a = b
b = a
print(a, b)
# Получаем вывод:
# Введите первое слово: Сок
# Введите второе слово: Вода
# Сок Вода
# Вода Вода  -- проблема, где Сок?
# Посмотрим на операции внимательнее, что они должны делать?
# Для понимания так же важно понимать - что находится в переменных перед выполнением:
print(a, b)  # -- до первой операции в 'a' записан Сок, в 'b' записана Вода
a = b  # -- записываем строку из 'b' в 'a'
print(a, b)  # -- теперь и там, и там записана Вода
b = a  # -- и теперь мы просто записываем воду из 'a' в 'b', хотя там и так была вода, вот и причина проблемы - мы потеряли Сок, который был записан в 'a'
print(a, b)

# Возвращаемся к шагу №2
# Идея остается той же, но нам надо придумать как сохранить значение в переменной "а" до её изменения
# Мы можем сделать это при помощи третьей переменной.
# т.е. надо
# 1) записать то, что было в "a" в новую переменную,
# 2) затем записать в "a" то, что было в "b",
# 3) а потом в "b" записать то, что было в новой переменной

# №3
a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
c = a  # 1) записать то, что было в "a" в новую переменную,
a = b  # 2) затем записать в "a" то, что было в "b",
b = c  # 3) а потом в "b" записать то, что было в новой переменной
print(a, b)

# Вот и всё, решение готово!
