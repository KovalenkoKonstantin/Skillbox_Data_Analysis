# Задача 1. Степень нечётного числа
# Выведите третью степень каждого нечётного числа
# в диапазоне от единицы до указанного пользователем числа включительно.
# Для этого используйте шаг внутри функции range.
#
#

n = int(input("До какого числа выводить кубы: "))
for i in range(1, n + 1, 2):
    print("Число:", i, "Куб числа:", i ** 3)

# Задача 2. Театр
# Ваню заставили пойти в театр на балет.
# Ему стало там настолько скучно, что он придумал себе очень странное развлечение:
# считать сумму номеров каждого пятого стула в рядах.
#
# Напишите программу для вычисления суммы
# каждого пятого числа, лежащего в диапазоне от единицы до N.
# Использовать условный оператор нельзя.
#
# Пример:
#
# Введите число: 21
# Номер стула: 1
# Номер стула: 6
# Номер стула: 11
# Номер стула: 16
# Номер стула: 21
# Сумма: 55
#
#

count = int(input("Введите число: "))
chair_sum = 0
for i in range(1, count + 1, 5):
    print("Номер стула:", i)
    chair_sum += i
print(chair_sum)

# Задача 3. Диета
# Саша просыпается когда угодно, но в 23 часа уже точно идёт спать.
# Питается Саша следующим образом:
# каждые 3 часа он выпивает литр воды и съедает N калорий.
# Пить и есть он, кстати, начинает сразу как только проснётся.
# Напишите программу,
# которая считает сколько он выпьет литров воды
# и сколько калорий он съест перед тем как пойдёт спать.

hour_start = int(input("Когда проснулся Саша? "))
water = 0
food = 0
for hour in range(hour_start, 23, 3):
    water += 1
    food_eaten = int(input("Сколько еды за день съел? "))
    food += food_eaten
print("Еды съедено:", food, "Воды выпито:", water)
