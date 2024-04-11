﻿import numpy as np

a = np.arange(12)
a
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
a[2]
# 2
a[0]
# 0
a[-1]
# 11
a[-2]
# 10
a[12]
# IndexError: index 12 is out of bounds for axis 0 with size 12
a[0] = 100
a
# array([100,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11])
b = a[2:4]
b
# array([2, 3])
b[0] = -100
b
# array([-100,    3])
a
# array([ 100,    1, -100,    3,    4,    5,    6,    7,    8,    9,   10,
#          11])
a[3:]
# array([ 3,  4,  5,  6,  7,  8,  9, 10, 11])
a[5:]
# array([ 5,  6,  7,  8,  9, 10, 11])
a[-5:-1]
# array([ 7,  8,  9, 10])
a[1:6:2]
# array([1, 3, 5])
a[::2]
# array([ 100, -100,    4,    6,    8,   10])
a[::-1]
# array([  11,   10,    9,    8,    7,    6,    5,    4,    3, -100,    1,
#         100])
a[:4] = [-1, -2, -3, -4]
a
# array([-1, -2, -3, -4,  4,  5,  6,  7,  8,  9, 10, 11])
a[4::2] = np.array([10, 20, 30, 40])
a
# array([-1, -2, -3, -4, 10,  5, 20,  7, 30,  9, 40, 11])

for x in a:
    print(x, sep=' ', end=' ')

# -1 -2 -3 -4 10 5 20 7 30 9 40 11
x = np.array([(1, 2, 3), (10, 20, 30), (100, 200, 300)])
x
# array([[  1,   2,   3],
#        [ 10,  20,  30],
#        [100, 200, 300]])
x[1, 1]
# 20
x[-1, -1]
# 300
x[0]
# array([1, 2, 3])
x[0, :]
# array([1, 2, 3])
x[:, 1]
# array([  2,  20, 200])
for row in x:
    for val in row:
        print(val, end=' ')
    print()

# 1 2 3
# 10 20 30
# 100 200 300
for val in x.flat:
    print(val, end=' ')

# 1 2 3 10 20 30 100 200 300

a = np.arange(1, 82).reshape(3, 3, 3, 3)
a[1, 2, 0, 1]
# 47
a[:, 1, :, :]
# array([[[10, 11, 12],
#         [13, 14, 15],
#         [16, 17, 18]],
#        [[37, 38, 39],
#         [40, 41, 42],
#         [43, 44, 45]],
#        [[64, 65, 66],
#         [67, 68, 69],
#         [70, 71, 72]]])
a[0, 0]
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
a[0, 0, :, :]
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
a[:, :, 1, 1]
# array([[ 5, 14, 23],
#        [32, 41, 50],
#        [59, 68, 77]])
a[0:2, 0:2, 1, 1]
# array([[ 5, 14],
#        [32, 41]])
a[..., 1, 1]
# array([[ 5, 14, 23],
#        [32, 41, 50],
#        [59, 68, 77]])

a = np.arange(1, 9)
a[0]
# 1
a[:3]
# array([1, 2, 3])
a
# array([1, 2, 3, 4, 5, 6, 7, 8])
b = a[0]
b
# 1
b = a[[0]]
b
# array([1])
b[0] = 100
a
# array([1, 2, 3, 4, 5, 6, 7, 8])
b
# array([100])
a[[0, 1, 7, 5]]
# array([1, 2, 8, 6])
b[0] = 100
a
# array([1, 2, 3, 4, 5, 6, 7, 8])
a[[0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7]]
# array([1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8])

a[[0, 1, 7, 5]] = [10, 20, 30, 40]
a
# array([10, 20,  3,  4,  5, 40,  7, 30])
indx = np.array([0, 0, 1, 1, 1, 2])
a[indx]
# array([10, 10, 20, 20, 20,  3])
bIndx = [True, True, False, False, False, True, False, False]
a[bIndx]
# array([10, 20, 40])
i = a > 5
i
# array([ True,  True, False, False, False,  True,  True,  True])
a[i]
# array([10, 20, 40,  7, 30])
a[a > 5]
# array([10, 20, 40,  7, 30])
