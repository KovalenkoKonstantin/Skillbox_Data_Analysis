﻿import numpy as np

a = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
a.dtype
# dtype('float64')
a.dtype = np.int8()
a
# array([-102, -103, -103, -103, -103, -103,  -71,   63, -102, -103, -103,
#        -103, -103, -103,  -55,   63,   51,   51,   51,   51,   51,   51,
#         -45,   63, -102, -103, -103, -103, -103, -103,  -39,   63,    0,
#           0,    0,    0,    0,    0,  -32,   63,   51,   51,   51,   51,
#          51,   51,  -29,   63,  102,  102,  102,  102,  102,  102,  -26,
#          63, -102, -103, -103, -103, -103, -103,  -23,   63,  -51,  -52,
#         -52,  -52,  -52,  -52,  -20,   63], dtype=int8
a.size
# 72
a.dtype = np.float64()
a
# array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
a.dtype = 'float32'
a
# array([-1.58818684e-23,  1.44999993e+00, -1.58818684e-23,  1.57499993e+00,
#         4.17232506e-08,  1.64999998e+00, -1.58818684e-23,  1.69999993e+00,
#         0.00000000e+00,  1.75000000e+00,  4.17232506e-08,  1.77499998e+00,
#         2.72008302e+23,  1.79999995e+00, -1.58818684e-23,  1.82499993e+00,
#        -1.07374184e+08,  1.84999990e+00], dtype=float32)
a.size
# 18
a.itemsize
# 4
a.dtype = 'float64'
a.itemsize
# 8
a.size * a.itemsize
# 72

b = np.ones((3, 4, 5))
b
# array([[[1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.]],
#        [[1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.]],
#        [[1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.]]])
b.ndim
# 3
b.shape  # возвращает кортеж
# (3, 4, 5)
b.shape = 60
b
# array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
#        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
#        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
#        1., 1., 1., 1., 1., 1., 1., 1., 1.])
b.shape = 12, 5
b
# array([[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]])

c = b.reshape(3, 2, 10)  # создаётся новое представление оригинального массива
c
# array([[[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]],
#        [[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]],
#        [[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]]])
b
# array([[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]])
b[0, 0] = 10
b
# array([[10.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.]])
c
# array([[[10.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]],
#        [[ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]],
#        [[ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#         [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]]])
print(id(b), id(c))
# 1508005467440 1508005471664

d = b.T  # транспонировать
d
# array([[10.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]])
b
# array([[10.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.]])

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a
a.shape = 3, 3
b
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.view()  # создаётся копия массива а
a.shape = 3, 3
a
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
b
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array(a)  # b будет ссылаться на копию массива а
b
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a[0] = 100
a
# array([100,   2,   3,   4,   5,   6,   7,   8,   9])
b
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
c = a.copy()  # создаётся копия массива а
c[0] = 1
c
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a
# array([100,   2,   3,   4,   5,   6,   7,   8,   9])
