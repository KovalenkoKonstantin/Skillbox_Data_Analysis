# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
user_input = int(input('Введите число: '))
# user_input = 5
# for number in range(1, user_input + 1):
#     for number_2 in range(user_input):
#         if number_2 >= number:
#             print('', end='')
#         else:
#             print(number, end=' ')
#     print()

for number in range(1, user_input +1):
    for number_2 in range(number):
        print(number, end=' ')
    print()
