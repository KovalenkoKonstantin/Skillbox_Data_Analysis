﻿import numpy as np

a = np.array([1, 2, 3, 10, 20, 30])
a.sum()
# 66
a.mean()  # среднее арифметическое
# 11.0
a.max()
# 30
a.min()
# 1
a.resize(3, 2)
a
# array([[ 1,  2],
#        [ 3, 10],
#        [20, 30]])
a.sum()
# 66
a.sum(axis=0)
# array([24, 42])
a.sum(axis=1)
# array([ 3, 13, 50])
a.max(axis=0)
# array([20, 30])
a.max(axis=1)
# array([ 2, 10, 30])

a = np.array([-1, 1, 5, -44, 32, 2])
np.abs(a)
# array([ 1,  1,  5, 44, 32,  2])
np.abs(-10.5)
# 10.5
np.abs([-10.5, -2, 5])
# array([10.5,  2. ,  5. ])
np.amax(a)
# 32
a
# array([ -1,   1,   5, -44,  32,   2])
np.amin(a)
# -44
np.round(0.7)
# 1.0
np.round(0.5)
# 0.0
np.round(a)
# array([ -1,   1,   5, -44,  32,   2])
np.argmax(a)  # возвращает индекс элемента в массиве с максимальным значением
# 4
np.argmin(a)
# 3
a.resize((2, 3))
a
# array([[ -1,   1,   5],
#        [-44,  32,   2]])
np.amax(a, axis=0)
# array([-1, 32, 5])
np.amax(a, axis=1)
# array([ 5, 32])
a = np.linspace(0, np.pi, 10)
a
# array([0.        , 0.34906585, 0.6981317 , 1.04719755, 1.3962634 ,
#        1.74532925, 2.0943951 , 2.44346095, 2.7925268 , 3.14159265])
np.sin(a)
# array([0.00000000e+00, 3.42020143e-01, 6.42787610e-01, 8.66025404e-01,
#        9.84807753e-01, 9.84807753e-01, 8.66025404e-01, 6.42787610e-01,
#        3.42020143e-01, 1.22464680e-16])
np.cos([0, 1.57, 3.14])
# array([ 1.00000000e+00,  7.96326711e-04, -9.99998732e-01])

np.random.rand()  # в диапазоне от 0 до 1 включительно
# 0.22759235372649755
# 0.28220966678560777
# 0.8681413851925017
np.random.rand(5)  # в диапазоне от 0 до 1 включительно. 5 - количество элементов
# array([0.3558123 , 0.50376657, 0.91279947, 0.39216855, 0.35294524])
np.random.rand(2, 3)
# array([[0.09790913, 0.08443122, 0.0034793 ],
#        [0.19623051, 0.88163805, 0.89448463]])
np.random.randint(10)  # целые случайные элементы
# 1
# 2
# 3
# 4
# 5
np.random.randint(5, 10)
# 6
np.random.randint(5, size=4)  # size - размер массива
# array([1, 2, 3, 0])
np.random.randint(1, 10, size=(2, 5))
# array([[4, 1, 3, 1, 5],
#        [4, 6, 4, 6, 5]])
np.random.randn()
# 1.085849613450095
# 1.395266088680915
np.random.randn(5)
# array([ 0.18938473, -0.3372471 ,  0.12358703,  1.57399993,  0.32477726])
np.random.randn(2, 3)
# array([[-0.04764971, -0.50710268, -2.08725713],
#        [ 0.93659602, -0.55435633, -0.56509461]])
np.random.pareto(2.0, size=3)
# array([0.99127784, 0.81440589, 0.08657929])
np.random.beta(0.1, 0.3, size=(3, 3))
# array([[2.73690184e-07, 7.13731248e-02, 1.95135747e-09],
#        [9.71218408e-01, 2.70015903e-04, 7.12272220e-02],
#        [6.85365899e-01, 1.69278566e-01, 2.09258843e-13]])
np.random.randn()
# -1.0034763567964093
# -0.4032088491753368
# 0.6577740514343988
# -0.026974912053182292
np.random.seed(13)  # позволяет генерировать одни и те же случайные последовательности
np.random.randn()
# -0.712390662050588
np.random.seed(13)
np.random.randint(10, size=10)
# array([2, 0, 0, 6, 2, 4, 9, 3, 4, 2])
np.random.seed(13)
np.random.randint(10, size=10)
# array([2, 0, 0, 6, 2, 4, 9, 3, 4, 2])
np.random.randint(10, size=10)
# array([6, 5, 9, 4, 2, 0, 3, 5, 3, 6])
np.random.seed(13)
np.random.randint(10, size=10)
# array([2, 0, 0, 6, 2, 4, 9, 3, 4, 2])

a = np.arange(10)
a
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.random.shuffle(a)
a
# array([8, 7, 9, 6, 3, 4, 0, 2, 1, 5])

a = np.arange(1, 10).reshape(3, 3)
a
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
np.random.shuffle(a)  # с многомерными массивами перетосовываются только строки массива
a
# array([[4, 5, 6],
#        [1, 2, 3],
#        [7, 8, 9]])
np.random.permutation(10)  # массив со случайно расположенными элементами от 0 до 9
# array([1, 9, 2, 6, 0, 8, 3, 7, 5, 4])

x = np.array([1, 4, 3, 7, 10, 8, 14, 21, 20, 23])
y = np.array([4, 1, 6, 9, 13, 11, 16, 19, 15, 22])
np.median(x)
# 9.0
np.var(x)  # дисперсия случайной величины
# 57.29
np.std(x)  # среднеквадратическое отклонение
# 7.569015788066504

XY = np.vstack([x, y])  # объединение двух массивов
XY
# array([[ 1,  4,  3,  7, 10,  8, 14, 21, 20, 23],
#        [ 4,  1,  6,  9, 13, 11, 16, 19, 15, 22]])
np.corrcoef(XY)
# array([[1.        , 0.93158099],
#        [0.93158099, 1.        ]])
np.cov(XY)
# array([[63.65555556, 49.82222222],
#        [49.82222222, 44.93333333]])
np.correlate(x, y)
# array([1736])
