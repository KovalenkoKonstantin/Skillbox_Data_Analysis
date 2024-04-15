import numpy as np

a = np.array([1, 2, 3, 4, 4, 3, 2, 1])
a
# array([1, 2, 3, 4, 4, 3, 2, 1])
setA = np.unique(a)
setA
# array([1, 2, 3, 4])
np.unique(a, return_counts=True)
# (array([1, 2, 3, 4]), array([2, 2, 2, 2], dtype=int64))
np.unique(a, return_index=True)
# (array([1, 2, 3, 4]), array([0, 1, 2, 3], dtype=int64))
np.unique(a, return_inverse=True)
# (array([1, 2, 3, 4]), array([0, 1, 2, 3, 3, 2, 1, 0], dtype=int64))

setA, indx = np.unique(a, return_inverse=True)
setA
# array([1, 2, 3, 4])
indx
# array([0, 1, 2, 3, 3, 2, 1, 0], dtype=int64)
setA[indx]
# array([1, 2, 3, 4, 4, 3, 2, 1])
x = np.array([[0, 1, 1, 2], [0, 1, 1, 2], [9, 1,1, 2]])
x
# array([[0, 1, 1, 2],
#        [0, 1, 1, 2],
#        [9, 1, 1, 2]])
np.unique(x)
# array([0, 1, 2, 9])
np.unique(x, axis=0)
# array([[0, 1, 1, 2],
#        [9, 1, 1, 2]])
np.unique(x, axis=1)
# array([[0, 1, 2],
#        [0, 1, 2],
#        [9, 1, 2]])
x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.in1d(x, y)
# array([False,  True,  True,  True])
np.random.shuffle(y)
y
# array([3, 2, 6, 1, 7, 5, 8, 4])
np.in1d(x, y)
# array([False, True, True, True])
np.intersect1d(x, y)
# array([1, 2, 3])
np.union1d(x, y)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8])
np.setdiff1d(x, y)
# array([0])
np.setdiff1d(y, x)
# array([4, 5, 6, 7, 8])
np.setxor1d(x, y)
# array([0, 4, 5, 6, 7, 8])
