import numpy as np

M = np.arange(1, 10, 0.003)
print(M)
print(M.round())
print(M.round(2))

A = np.array([2.5, 2.7, 8.1, 9.25])
print(np.floor(A))
print(np.ceil(A))

print(np.add(A, 2))
print(np.subtract(A, 1))
print(np.sum(A))
print(np.prod(A))

d1 = '2017-01-25'
d2 = '2019-02-28'

print(np.datetime64(d2) - np.datetime64(d1))

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]

plt.plot(x, y)
plt.show()

x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()

x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.plot(x, y, color='green', marker='o', markersize=7)

plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Комбинирование графиков')
plt.legend()
plt.show()

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

plt.pie(vals, labels=labels)
plt.title("Распределение марок автомобилей на дороге")
plt.show()

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")
plt.show()

labels = ['2017', '2018', '2019', '2020', '2021']
android_users = [85, 85.1, 86, 86.2, 86]
ios_users = [14.5, 14.8, 13, 13.8, 14.0]

width = 0.35       #Задаём ширину столбцов
fig, ax = plt.subplots()

ax.bar(labels, android_users, width, label='Android')
ax.bar(labels, ios_users, width, bottom=android_users,
      label='iOS') #Указываем с помощью параметра bottom, что значения в столбце должны быть выше значений переменной android_users

ax.set_ylabel('Соотношение, в %')
ax.set_title('Распределение устройств на Android и iOS')
ax.legend(loc='lower left', title='Устройства') #Сдвигаем легенду в нижний левый угол, чтобы она не перекрывала часть графика

plt.show()
