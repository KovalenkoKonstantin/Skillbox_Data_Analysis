# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|
width = int(input('Enter frame width: '))
height = int(input('Enter frame height: '))
# width = 9
# height = 8

print(" " + "_ " * width)
for _ in range(height):
    print("|" + " " * (width * 2) + "|")
print("|" + "_ " * width + "|")
