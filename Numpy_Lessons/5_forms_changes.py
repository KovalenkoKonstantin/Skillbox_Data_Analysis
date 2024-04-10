import numpy as np

a = np.arange(10)
a
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a.shape = 2, 5
a
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])
b = a.reshape(10)
b
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])
b[0] = -1
b
# array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
a
# array([[-1,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9]])
b = a.reshape(9)
# ValueError: cannot reshape array of size 10 into shape (9,)
a.shape = 3, 3
# ValueError: cannot reshape array of size 10 into shape (3,3)
a.shape = -1, 2  # отрицательный элемент кортежа означает,
# что пусть будет столько строк сколько останется
a
# array([[-1,  1],
#        [ 2,  3],
#        [ 4,  5],
#        [ 6,  7],
#        [ 8,  9]])
a.shape = -1, 5
a
# array([[-1,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9]])
b.reshape(-1, 1)
# array([[-1],
#        [ 1],
#        [ 2],
#        [ 3],
#        [ 4],
#        [ 5],
#        [ 6],
#        [ 7],
#        [ 8],
#        [ 9]])
b.reshape(1, -1)
# array([[-1,  1,  2,  3,  4,  5,  6,  7,  8,  9]]) # матрица [[]]
b
# array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9]) # вектор []
a
# array([[-1,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9]])
a.ravel()  # многомерный массив преобразовать к одномерному (вектор)
# array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
c = a.ravel()
c
# array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
a
# array([[-1,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9]])
a.shape = -1
a
# array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
a.resize(2, 5)  # меняет представление текущего массива
a
# array([[-1,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9]])
a.resize(3, 3)
# ValueError: cannot resize an array that references or is referenced
# by another array in this way.
a.resize(3, 3, refcheck=False)
a
# array([[-1,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8]])
a.resize(4, 5, refcheck=False)
a
# array([[-1,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  0],
#        [ 0,  0,  0,  0,  0],
#        [ 0,  0,  0,  0,  0]])
a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
a
# array([[ 1,  2,  3],
#        [ 1,  4,  9],
#        [ 1,  8, 27]])
b = a.T  # операция транспонирования создаёт лишь новое представление
b
# array([[ 1,  1,  1],
#        [ 2,  4,  8],
#        [ 3,  9, 27]])
x = np.arange(1, 10)
x
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x.T
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x.shape = 1, -1
x
# array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
x.T
# array([[1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6],
#        [7],
#        [8],
#        [9]])
x_test = np.arange(32).reshape(8, 2, 2)
x_test
# array([[[ 0,  1],
#         [ 2,  3]],
#        [[ 4,  5],
#         [ 6,  7]],
#        [[ 8,  9],
#         [10, 11]],
#        [[12, 13],
#         [14, 15]],
#        [[16, 17],
#         [18, 19]],
#        [[20, 21],
#         [22, 23]],
#        [[24, 25],
#         [26, 27]],
#        [[28, 29],
#         [30, 31]]])
x.shape
# (1, 9)
x_test.shape
# (8, 2, 2)
x_test4 = np.expand_dims(x_test, axis=0)
x_test4.shape
# (1, 8, 2, 2)
x_test4[0, 0, 0, 0] = -100
x_test
# array([[[-100,    1],
#         [   2,    3]],
#        [[   4,    5],
#         [   6,    7]],
#        [[   8,    9],
#         [  10,   11]],
#        [[  12,   13],
#         [  14,   15]],
#        [[  16,   17],
#         [  18,   19]],
#        [[  20,   21],
#         [  22,   23]],
#        [[  24,   25],
#         [  26,   27]],
#        [[  28,   29],
#         [  30,   31]]])
x_test4.shape
# (1, 8, 2, 2)
a = np.append(x_test4, x_test4, axis=0) # будет добавляться первая ось
a.shape
# (2, 8, 2, 2)
b = np.delete(a, 0, axis=0)
b.shape
# (1, 8, 2, 2)
b = np.expand_dims(x_test4, axis=-1)  # будет добавляться последняя ось
b.shape
# (1, 8, 2, 2, 1)
c = np.squeeze(b) # удаляет из массива все оси где есть один элемент
c.shape
# (8, 2, 2)
c = np.squeeze(b, axis=0)
c.shape
# (8, 2, 2, 1)
c = np.squeeze(b, axis=1)
# ValueError: cannot select an axis to squeeze out which has size not equal to one

a = np.arange(1, 10)
a
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a[np.newaxis, :]
b.shape
# (1, 9)
b
# array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
b = a[:, np.newaxis]
b
# array([[1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6],
#        [7],
#        [8],
#        [9]])
c = a[np.newaxis, :, np.newaxis]
c
# array([[[1],
#         [2],
#         [3],
#         [4],
#         [5],
#         [6],
#         [7],
#         [8],
#         [9]]])
c.shape
# (1, 9, 1)
