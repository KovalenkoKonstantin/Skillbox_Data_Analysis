import numpy as np

a = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
a.dtype
a.dtype = np.int8()
a
a.size
a.dtype = np.float64()
a
a.dtype = 'float32'
a
a.size
a.itemsize
a.dtype = 'float64'
a.itemsize
a.size * a.itemsize

b = np.ones((3, 4, 5))
b
b.ndim
b.shape  # возвращает кортеж
b.shape = 60
b
b.shape = 12, 5
b

c = b.reshape(3, 2, 10)  # создаётся новое представление оригинального массива
c
b
b[0, 0] = 10
b
c
print(id(b), id(c))

d = b.T  # транспонировать
d
b

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a
a.shape = 3, 3
b
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.view()  # создаётся копия массива а
a.shape = 3, 3
b
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array(a)  # b будет ссылаться на копию массива а
a[0] = 100
b
c = a.copy()  # создаётся копия массива а
c[0] = 1
c
a


