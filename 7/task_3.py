# Мы всё ближе и ближе подбираемся к серьёзной математике.
# Одна из классических задач - задача на нахождение факториала числа.
# И в будущем мы с ней ещё встретимся.
#
# Дано натуральное число N. Напишите программу, которая находит N! (N факториал)
#
# Запись N! означает следующее:
#
# N! = 1 * 2 * 3 * 4 * 5 * … * N
#
# Пример:
#
# Введите число: 5
# Факториал числа 5 равен 120
input_number = int(input('Введите число: '))
fak = 1
for _ in range(1, input_number + 1):
    fak *= _
print('Факториал числа', input_number, 'равен', fak)
