import numpy as np

lst = [1, 2, 3]
a = np.array([1, 2, 3])
lst * 2
# [1, 2, 3, 1, 2, 3]
a * 2
# array([2, 4, 6])
a
# array([1, 2, 3])
-a
# array([-1, -2, -3])
a - 3
# array([-2, -1,  0])
a + 2
# array([3, 4, 5])
2 + a
# array([3, 4, 5])
a * 5
# array([ 5, 10, 15])
a / 5
# array([0.2, 0.4, 0.6])
a // 2
# array([0, 1, 1], dtype=int32)
a ** 3
# array([ 1,  8, 27], dtype=int32)
a % 2
# array([1, 0, 1], dtype=int32)
b = np.array([3, 4, 5])
a - b
# array([-2, -2, -2])
b + a
# array([4, 6, 8])
a * b
# array([ 3,  8, 15])
a / b
# array([0.33333333, 0.5       , 0.6       ])
a // b
# array([0, 0, 0])
b ** a
# array([  3,  16, 125])
b % a
# array([0, 0, 2])
b = np.array([3, 4, 5, 6])
a + b
# ValueError: operands could not be broadcast together with shapes (3,) (4,)

b = np.arange(1, 7)
b.resize(2, 3)
b
# array([[1, 2, 3],
#        [4, 5, 6]])
a
# array([1, 2, 3])
a + b
# array([[2, 4, 6],
#        [5, 7, 9]])
a = np.arange(1, 19)
a.resize(3, 3, 2)
b = np.ones((3, 2))
a - b
# array([[[ 0.,  1.],
#         [ 2.,  3.],
#         [ 4.,  5.]],
#        [[ 6.,  7.],
#         [ 8.,  9.],
#         [10., 11.]],
#        [[12., 13.],
#         [14., 15.],
#         [16., 17.]]])
a * 10
# array([[[ 10,  20],
#         [ 30,  40],
#         [ 50,  60]],
#        [[ 70,  80],
#         [ 90, 100],
#         [110, 120]],
#        [[130, 140],
#         [150, 160],
#         [170, 180]]])
a // b
# array([[[ 1.,  2.],
#         [ 3.,  4.],
#         [ 5.,  6.]],
#        [[ 7.,  8.],
#         [ 9., 10.],
#         [11., 12.]],
#        [[13., 14.],
#         [15., 16.],
#         [17., 18.]]])
a = np.array([1, 2, 6, 8])
a
# array([1, 2, 6, 8])
a += 5
a
# array([ 6,  7, 11, 13])
a += 5
a
# array([11, 12, 16, 18])
a -= 5
a
# array([ 6,  7, 11, 13])
b = np.ones(4)
b
# array([1., 1., 1., 1.])
a
# array([ 6,  7, 11, 13])
b *= a
b
# array([ 6.,  7., 11., 13.])
a += b
# UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'
(a + b) * 5 - 10
# array([ 50.,  60., 100., 120.])

