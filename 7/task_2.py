# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.
total_salary = 0
for bar in range(12):
    user_choice = int(input(f'Input amount of a salary for {bar + 1} month: '))
    total_salary += user_choice
print('Average month salary is ', total_salary / 12)
