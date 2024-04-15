﻿import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
a
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
b
# array([[10, 11, 12],
#        [13, 14, 15],
#        [16, 17, 18]])
a * b
# array([[ 10,  22,  36],
#        [ 52,  70,  90],
#        [112, 136, 162]])
np.dot(a, b)
# array([[ 84,  90,  96],
#        [201, 216, 231],
#        [318, 342, 366]])
np.dot(b, a)
# array([[138, 171, 204],
#        [174, 216, 258],
#        [210, 261, 312]])
np.matmul(b, a)
# array([[138, 171, 204],
#        [174, 216, 258],
#        [210, 261, 312]])
a.size = -1, 1
# AttributeError: attribute 'size' of 'numpy.ndarray' objects is not writable
a.shape = -1, 1
a
# array([[1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6],
#        [7],
#        [8],
#        [9]])
np.dot(a, b)
# ValueError: shapes (9,1) and (3,3) not aligned: 1 (dim 1) != 3 (dim 0)
a.shape = 1, -1
a
# array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
np.dot(a, b)
# ValueError: shapes (1,9) and (3,3) not aligned: 9 (dim 1) != 3 (dim 0)

a = np.arange(1, 10)
b = np.ones(9)
a
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b
# array([1., 1., 1., 1., 1., 1., 1., 1., 1.])
np.dot(a, b)
# 45.0
np.inner(a, b)
# 45.0
np.outer(a, b)
# array([[1., 1., 1., 1., 1., 1., 1., 1., 1.],
#        [2., 2., 2., 2., 2., 2., 2., 2., 2.],
#        [3., 3., 3., 3., 3., 3., 3., 3., 3.],
#        [4., 4., 4., 4., 4., 4., 4., 4., 4.],
#        [5., 5., 5., 5., 5., 5., 5., 5., 5.],
#        [6., 6., 6., 6., 6., 6., 6., 6., 6.],
#        [7., 7., 7., 7., 7., 7., 7., 7., 7.],
#        [8., 8., 8., 8., 8., 8., 8., 8., 8.],
#        [9., 9., 9., 9., 9., 9., 9., 9., 9.]])
a @ b
# 45.0
a.resize(3, 3)
b.resize(3, 3)
a
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
b
# array([[1., 1., 1.],
#        [1., 1., 1.],
#        [1., 1., 1.]])
a @ b
# array([[ 6.,  6.,  6.],
#        [15., 15., 15.],
#        [24., 24., 24.]])
b @ a
# array([[12., 15., 18.],
#        [12., 15., 18.],
#        [12., 15., 18.]])

a = np.array([1, 2, 3])
b = np.arange(4, 10).reshape(3, 2)
a
# array([1, 2, 3])
b
# array([[4, 5],
#        [6, 7],
#        [8, 9]])
np.dot(a, b)
# array([40, 46])
np.dot(b, a)
# ValueError: shapes (3,2) and (3,) not aligned: 2 (dim 1) != 3 (dim 0)

a = np.array([1, 2])
a
# array([1, 2])
a.shape = -1, 1
a
# array([[1],
#        [2]])
np.dot(b, a)
# array([[14],
#        [20],
#        [26]])
b @ a
# array([[14],
#        [20],
#        [26]])
a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
a
# array([[ 1,  2,  3],
#        [ 1,  4,  9],
#        [ 1,  8, 27]])
np.linalg.matrix_rank(a)
# 3
y = np.array([10, 20, 30])
np.linalg.solve(a, y)
# array([-5.        , 10.        , -1.66666667])
invA = np.linalg.inv(a)
invA
# array([[ 3.        , -2.5       ,  0.5       ],
#        [-1.5       ,  2.        , -0.5       ],
#        [ 0.33333333, -0.5       ,  0.16666667]])
a @ invA
# array([[ 1.00000000e+00,  0.00000000e+00, -2.77555756e-17],
#        [ 3.33066907e-16,  1.00000000e+00, -8.32667268e-17],
#        [ 9.99200722e-16,  0.00000000e+00,  1.00000000e+00]])
invA @ y
# array([-5.        , 10.        , -1.66666667])
