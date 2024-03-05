# Задача 1. Ставки на спорт
#
# Нас наняла букмекерская контора,
# где проводятся ставки на конный спорт.
# Напишите программу расчёта потенциального выигрыша игрока.
# Для этого вводится его ставка в рублях и коэффициент (вещественное число),
# а выводится их произведение в качестве потенциального выигрыша.
#
# Пример:
#
# Сколько ставим? 1234
# Какой коэффициент? 1.716
# Потенциальный выигрыш: 2117.544
#
# Усложнение задачи: сделайте так, чтобы после точки выводилось не больше двух цифр.
#
#

bet_in = float(input("Сколько ставим? "))
bet_coef = float(input("Какой коэффициент? "))

# Вариант 1:
print("Потенциальный выигрыш: ", bet_in * bet_coef)

# *Вариант 2:
bet_out = int(bet_in * bet_coef * 100) / 100
print("Потенциальный выигрыш: ", bet_out)

# *Вариант 3:
bet_out = round(bet_in * bet_coef, 2)
print("Потенциальный выигрыш: ", bet_out)

# Задача 2. День рождения
#
# В честь дня рождения сына отец не придумал ничего лучше,
# кроме как подарить денег. Зато он придумал хоть и странную,
# но интересную формулу,
# по которой высчитывается сколько он подарит:
# возраст сына умножается на 1.5 и на его температуру тела.
# Остаётся только позавидовать такой фантазии.
#
# Напишите программу,
# которая запрашивает у пользователя возраст (целое число)
# и температуру тела (вещественное число)
# и в результате выводит сколько отец подарит сыну денег на день рождения.
#
#
user_age = int(input("Ваш возраст? "))
user_temperature = float(input("Ваша температура тела? "))
formula_for_money = user_age * 1.5 * user_temperature
print(round(formula_for_money, 2))

# Задача 3. Индекс массы тела
#
# Алексей работает диетологом в частной клинике,
# каждый день он принимает пациентов разных возрастов
# и с разными показателями роста (в метрах)
# и веса (в кг). Для каждого человека ему нужно считать индекс массы тела -
# это вес поделить на рост в квадрате.
# По государственным стандартам индекс округляется до двух знаков после точки.
# Затем по этому индексу определяется,
# всё ли в порядке у человека с массой тела:
# если до 18.5, то недобор; до 25 - всё нормально,
# до 30 уже идёт избыток, а после 30 - ожирение.
# Напишите такую программу для Алексея.

user_weight = float(input("Вес пациента: "))
user_height = float(input("Рост пациента: "))

result = round(user_weight / user_height ** 2, 2)
if result < 18.5:
    print("Недобор")
elif result < 25:
    print("Норма")
elif result < 30:
    print("Избыток")
else:
    print("Ожирение")