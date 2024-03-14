import numpy as np

scores = np.array([3, 5, 7, 9, 8, 10])
pairs = scores.reshape(3, 2)

print(pairs)

pairs[0][0] = 4

print(pairs)

pairs[0][0] = 3

pairs2 = pairs
pairs2[0][0] = 4  # не копия объекта а ссылка на него
print(pairs)
print(pairs2)

pairs[0][0] = 3
pairs3 = pairs2.copy()  # создание копии с помощью метода
pairs3[2][1] = 9

print(pairs2)
print(pairs3)

pairs4 = pairs3[:]  # беру все элементы с первого до последнего
# полный срез
pairs4[2][1] = 6

print(pairs3)
print(pairs4)

print(pairs[0:2])   # изменение списков с использованием срезов

pairs[0:2] = [[5, 4], [9, 7]]
print(pairs)
