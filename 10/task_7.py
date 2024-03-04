# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29
number_of_levels = int(input("Enter the number of pyramid levels: "))

number = 1
for i in range(1, number_of_levels + 1):
    row = ' ' * 3 * (number_of_levels - i)
    for j in range(i):

        if number == 1:
            adjust = ''
        elif 1 < number < 10:
            adjust = ' ' * 5
        elif 10 < number < 100:
            adjust = ' ' * 4
        elif 100 < number < 1000:
            adjust = ' ' * 3
        elif 1000 < number < 10000:
            adjust = ' ' * 2
        else:
            adjust = ' '

        row += str(number) + adjust
        number += 2
    print(row)

# height = int(input('Укажите количество уровней: '))
#
# start_num = 1
#
# for i in range(1, height + 1):
#
#     print('\t' * (height - i), end='')
#
#     for j in range(i):
#
#          print('\t', start_num, end='\t')
#
#         start_num += 2
#
#     print()
    