# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######
height = int(input("Введите высоту пирамиды: "))

for i in range(1, height + 1):
    spaces = " " * (height - i)
    hashes = "#" * (2 * i - 1)
    print(spaces + hashes + spaces)
