# В классе N человек.
# Каждый из них получил за урок по информатике оценку:
# 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок -
# N чисел - и выводит на экран сообщение о том,
# кого сегодня больше:
# отличников, хорошистов или троечников.

# Замечание:
# можно предположить,
# что количество отличников,
# хорошистов, троечников различно.
number_of_grades = int(input('Input total number of all grades: '))
grade = 0
good_student = 0
bad_student = 0
awful_student = 0
biggest = ''
for i in range(number_of_grades):
    grade = int(input(f'Input {i + 1} st(nd) grade between 3 and 5: '))
    if grade < 3 or grade > 5:
        print('You entered an incorrect grade. '
              'The input is finished.')
        break
    elif grade == 5:
        good_student += 1
    elif grade == 4:
        bad_student += 1
    else:
        awful_student += 1
# print('Total number of students with A grade is', good_student, '\n'
#       'Total number of students with B grade is', bad_student, '\n'
#       'Total number of students with C grade is', awful_student)
if good_student > bad_student and good_student > awful_student:
    biggest = 'A'
elif bad_student > good_student and bad_student > awful_student:
    biggest = 'B'
else:
    biggest = 'C'
print("Today's biggest amount of students are with", biggest, 'grade')
