# Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

# Пояснение:
# 15 -> 1*5*3 = 15 - получившееся число равно оригиналу, значит число надо вывести
# 16 -> 1*6*3 = 18 - число выводить не нужно, 18 не равно 16
for i in range(10, 100):
    if i // 10 * i % 10 * 3 == i:
        print(i)
