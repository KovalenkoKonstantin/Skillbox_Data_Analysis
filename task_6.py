print('Задача 6. Проверяем бухгалтера')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
first_number_last_two_digits = first_number % 100
second_number_last_two_digits = second_number % 100
sum_of_last_two_digits = first_number_last_two_digits + second_number_last_two_digits
print('Сумма: ', sum_of_last_two_digits)
