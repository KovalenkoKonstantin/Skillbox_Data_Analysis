# Напишите программу,
# которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b],
# кратных числу c.
import statistics

a = int(input('input a number: '))
b = int(input('input b number: '))
c = int(input('input c number: '))
count = 0
summ = 0
my_list = []
for number in range(a, b + 1):
    if number % c == 0 and number != 0:
        my_list.append(number)
        count += 1
        summ += number
try:
    average = summ / count
    print('the arithmetic mean of all numbers '
          'from the segment [{}; {}], multiples of {} is: {}'.format(a, b, c, average))
    print('using the statistical function it turns out:', statistics.mean(my_list))

except ZeroDivisionError:
    print('wrong spacing')
