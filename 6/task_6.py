# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.
deposit = int(input('Put the deposit amount: '))
target = int(input('Put the target amount: '))
percentage = int(input('Put the annual percentage: '))
year_counter = 0
while deposit < target:
    deposit *= round((1 + percentage/100), 2)
    year_counter += 1
print('You will need', year_counter, 'years to aim your goal')
