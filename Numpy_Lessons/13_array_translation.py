import numpy as np

a = np.array([1, 2, 3, 10, 20, 30])
b = np.array([2])
a
# array([ 1,  2,  3, 10, 20, 30])
b
# array([2])
a * b
# array([ 2,  4,  6, 20, 40, 60])
a + b
# array([ 3,  4,  5, 12, 22, 32])
b = np.array([2, 3])
a * b
# ValueError: operands could not be broadcast together with shapes (6,) (2,)
a.ndim
# 1
b.ndim
# 1

a = np.arange(1, 10).reshape(3, 3)
b = np.array([4, 5, 6])
a
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
b
# array([4, 5, 6])
a + b
# array([[ 5,  7,  9],
#        [ 8, 10, 12],
#        [11, 13, 15]])

a = np.arange(6).reshape(3, 1, 2)
b = np.ones(4).reshape(2, 2)
c = a * b
c.shape
# (3, 2, 2)
a = a.reshape(2, 3, 1)
a * b
# ValueError: operands could not be broadcast together with shapes (2,3,1) (2,2)

b = np.ones(6).reshape(3, 2)
c = a * b
c.shape
# (2, 3, 2)

a = np.array([1, 2, 3])
b = np.array([4, 5])
c = np.array([7, 8, 9, 10])
a * b + c
# ValueError: operands could not be broadcast together with shapes (3,) (2,)

a.shape = 1, 1, -1
b.shape = 1, -1, 1
c.shape = -1, 1, 1
c = a * b + c
c.shape
# (4, 2, 3)

a = np.array([1, 2, 3])
b = np.array([4, 5])
c = np.array([7, 8, 9, 10])
an, bn, cn, = np.ix_(a, b, c)
an.shape
# (3, 1, 1)
bn.shape
# (1, 2, 1)
cn.shape
# (1, 1, 4)
c = an * bn * cn
c
# array([[[ 28,  32,  36,  40],
#         [ 35,  40,  45,  50]],
#        [[ 56,  64,  72,  80],
#         [ 70,  80,  90, 100]],
#        [[ 84,  96, 108, 120],
#         [105, 120, 135, 150]]])
