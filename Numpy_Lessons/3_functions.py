﻿import numpy as np

a = np.array([1, 2, 3])
a
# array([1, 2, 3])
np.array([0] * 10)
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.array([1] * 15)
# array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
np.array([x for x in range(10)])
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.empty(10)
# array([4.45042952e-307, 2.11397635e-307, 9.34608432e-307, 1.37959129e-306,
#        1.37962320e-306, 1.78019625e-306, 1.60219035e-306, 9.34598246e-307,
#        2.97893274e-317, 0.00000000e+000])
np.empty(10, dtype='int16')
# array([-32768, -10183,  32766,      0,  31808, -28605,    492,      0,
#             0,      0], dtype=int16)
np.empty((3, 2), dtype='int16')
# array([[     0,      0],
#        [     0,      0],
#        [ 32032, -28605]], dtype=int16)

np.eye(4)
# array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])
np.eye(4, 2)
# array([[1., 0.],
#        [0., 1.],
#        [0., 0.],
#        [0., 0.]])
np.identity(5)
# array([[1., 0., 0., 0., 0.],
#        [0., 1., 0., 0., 0.],
#        [0., 0., 1., 0., 0.],
#        [0., 0., 0., 1., 0.],
#        [0., 0., 0., 0., 1.]])
np.zeros((2, 3, 4))
# array([[[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]],
#        [[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]]])
np.ones([4, 3], dtype='int8')
# array([[1, 1, 1],
#        [1, 1, 1],
#        [1, 1, 1],
#        [1, 1, 1]], dtype=int8)
np.full((3, 2), -1)
# array([[-1, -1],
#        [-1, -1],
#        [-1, -1]])
np.mat('1 2 3 4')  # создаёт матрицу 1х4 из строки
# matrix([[1, 2, 3, 4]])
np.mat('1, 2, 3, 4')
# matrix([[1, 2, 3, 4]])
np.mat('1 2; 3 4')
# matrix([[1, 2],
#         [3, 4]])
np.mat([5, 4, 3])
# matrix([[5, 4, 3]])
np.mat([[1, 2, 3],
        [4, 5, 6]])
# matrix([[1, 2, 3],
#         [4, 5, 6]])
np.mat([(1, 2, 3), (4, 5, 6)])
# matrix([[1, 2, 3],
#         [4, 5, 6]])
np.mat([(1, 2, 3), (4, 5, 6, 7)])
# arr = N.array(data, dtype=dtype, copy=copy)
np.diag([1, 2, 3])
# array([[1, 0, 0],
#        [0, 2, 0],
#        [0, 0, 3]])
np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# array([1, 5, 9])
np.diagflat([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 2, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 3, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 4, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 5, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 6, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 7, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 8, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 9]])
np.tri(4)
# array([[1., 0., 0., 0.],
#        [1., 1., 0., 0.],
#        [1., 1., 1., 0.],
#        [1., 1., 1., 1.]])
np.tri(4, 2)
# array([[1., 0.],
#        [1., 1.],
#        [1., 1.],
#        [1., 1.]])
np.tri(2, 4)
# array([[1., 0., 0., 0.],
#        [1., 1., 0., 0.]])
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
a
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
np.tril(a)
# array([[1, 0],
#        [3, 4],
#        [5, 6]])
np.triu(a)
# array([[1, 2],
#        [0, 4],
#        [0, 0]])
np.tril([1, 2, 3])
# array([[1, 0, 0],
#        [1, 2, 0],
#        [1, 2, 3]])
np.tril([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# array([[[1, 0, 0],
#         [4, 5, 0],
#         [7, 8, 9]]])
np.tril([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
         [[100, 200, 300], [400, 500, 600], [700, 800, 900]]])
# array([[[  1,   0,   0],
#         [  4,   5,   0],
#         [  7,   8,   9]],
#        [[ 10,   0,   0],
#         [ 40,  50,   0],
#         [ 70,  80,  90]],
#        [[100,   0,   0],
#         [400, 500,   0],
#         [700, 800, 900]]])
np.vander([1, 2, 3])
# array([[1, 1, 1],
#        [4, 2, 1],
#        [9, 3, 1]])

np.arange(5)
# array([0, 1, 2, 3, 4])
np.arange(1, 5)
# array([1, 2, 3, 4])
np.arange(1, 5, 0.5)
# array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])
np.arange(0, np.pi, 0.1)
# array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
#        1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. , 2.1, 2.2, 2.3, 2.4, 2.5,
#        2.6, 2.7, 2.8, 2.9, 3. , 3.1])
np.cos(np.arange(0, np.pi, 0.1))
# array([ 1.        ,  0.99500417,  0.98006658,  0.95533649,  0.92106099,
#         0.87758256,  0.82533561,  0.76484219,  0.69670671,  0.62160997,
#         0.54030231,  0.45359612,  0.36235775,  0.26749883,  0.16996714,
#         0.0707372 , -0.02919952, -0.12884449, -0.22720209, -0.32328957,
#        -0.41614684, -0.5048461 , -0.58850112, -0.66627602, -0.73739372,
#        -0.80114362, -0.85688875, -0.90407214, -0.94222234, -0.97095817,
#        -0.9899925 , -0.99913515])

np.linspace(0, np.pi, 0)
# array([], dtype=float64)
np.linspace(0, np.pi, 1)
# array([0.])
np.linspace(0, np.pi, 2)
# array([0.        , 3.14159265]
np.linspace(0, np.pi, 3)
# array([0.        , 1.57079633, 3.14159265])
np.linspace(0, np.pi, 4)
# array([0.        , 1.04719755, 2.0943951 , 3.14159265])
np.linspace(0, np.pi, 5)
# array([0.        , 0.78539816, 1.57079633, 2.35619449, 3.14159265])

np.logspace(0, 1, 3)
# array([ 1.        ,  3.16227766, 10.        ])
np.logspace(0, 1, 4)
# array([ 1.        ,  2.15443469,  4.64158883, 10.        ])

np.geomspace(1, 4, 3)
# array([1., 2., 4.])
np.geomspace(1, 16, 5)
# array([ 1.,  2.,  4.,  8., 16.])

a = np.array([(1, 2), (3, 4)])
a
# array([[1, 2],
#        [3, 4]])
b = np.copy(a)
b
# array([[1, 2],
#        [3, 4]])
b[0] = 100
b
# array([[100, 100],
#        [  3,   4]])
a


# array([[1, 2],
#        [3, 4]])
def getRange(x, y):
    return 100 * x + y


a = np.fromfunction(getRange, (2, 2))
a
# array([[  0.,   1.],
#        [100., 101.]])
np.fromfunction(lambda x, y: x * 100 + y, (2, 2))
# array([[  0.,   1.],
#        [100., 101.]])

np.fromiter('hello', dtype='U1')
# array(['h', 'e', 'l', 'l', 'o'], dtype='<U1')

def getRange(N):
    for i in range(N):
        yield i

np.fromiter(getRange(4), dtype='int8')
# array([0, 1, 2, 3], dtype=int8)

np.fromstring('1 2 3', dtype='int16', sep=' ')
# array([1, 2, 3], dtype=int16)
np.fromstring('1, 2, 3', dtype='int16', sep=', ')
# array([1, 2, 3], dtype=int16)
