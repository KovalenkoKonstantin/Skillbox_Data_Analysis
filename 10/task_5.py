# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.
N = int(input("Введите количество чисел N: "))
max_number = 0
max_sum_of_digits = 0
sum_of_digits = 0
collection = []

for i in range(N):
    number = int(input(f"Введите {i + 1} число: "))
    if number > 1:
        is_prime = True
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            collection.append(number)
    for k in collection:
        for l in str(k):
            sum_of_digits += int(l)
        if sum_of_digits > max_sum_of_digits:
            max_sum_of_digits = sum_of_digits
            max_number = number
        sum_of_digits = 0

# print(collection)
print(f'Это число {max_number}')
print(f'Сумма его цифр {max_sum_of_digits}')
