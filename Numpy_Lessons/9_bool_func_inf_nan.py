import numpy as np

a = np.array([1, 2, 3, 10, 20, 30])
a[a > 5]
# array([10, 20, 30])
a > 5
# array([False, False, False,  True,  True,  True])
b = np.array([1, 2, 3, 4, 5, 6])
a == b
# array([ True,  True,  True, False, False, False])
a != b
# array([False, False, False,  True,  True,  True])
a != 2
# array([ True, False,  True,  True,  True,  True])
np.greater(a, b)
# array([False, False, False,  True,  True,  True])
a > b
# array([False, False, False,  True,  True,  True])
np.less(a, b)
# array([False, False, False, False, False, False])
a < b
# array([False, False, False, False, False, False])
np.equal(a, b)
# array([ True,  True,  True, False, False, False])
a == b
# array([ True,  True,  True, False, False, False])
if (a == b): print('a == b')
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
if np.array_equal(a, b):
    print('a == b')
np.array_equal(a, b)
# False
np.any(a > 5)
# True
a
# array([ 1,  2,  3, 10, 20, 30])
np.any(a == 5)
# False
np.any(a == b)
# True
a == b
# array([ True,  True,  True, False, False, False])
np.all(a > 5)
# False
np.all(a > 0)
# True
np.all(a > b)
# False
a / 0
# RuntimeWarning: divide by zero encountered in divide
#   a /0
# Out[19]: array([inf, inf, inf, inf, inf, inf])  # inf сокращение от infinity
b = np.array([1, 2, np.inf])
b
# array([ 1.,  2., inf])
b * 0
# RuntimeWarning: invalid value encountered in multiply
#   b*0
# Out[22]: array([ 0.,  0., nan])  # nan - not a number
c = b * 0
# RuntimeWarning: invalid value encountered in multiply
#   c = b * 0
c
# array([ 0.,  0., nan])
c.sum()
# nan

b = np.array([1, 2, np.nan, np.inf, -np.inf])
b
# array([  1.,   2.,  nan,  inf, -inf])
np.isinf(b)
# array([False, False, False,  True,  True])
np.isnan(b)
# array([False, False,  True, False, False])
indx = np.isinf(b)
indx
# array([False, False, False,  True,  True])
b[~indx]  # ~ означает что мы индекс инвертируем
# array([1., 2., nan])
np.isfinite(b)
# array([ True,  True, False, False, False])

a = np.array([1 + 2j, 3 - 4j, 5])
a
# array([1.+2.j, 3.-4.j, 5.+0.j])
np.iscomplex(a)
# array([ True,  True, False])
np.isreal(a)
# array([False, False,  True])
np.isreal(b)
# array([ True,  True,  True,  True,  True])
b
# array([  1.,   2.,  nan,  inf, -inf])

X = np.array([True, False, True, False])
Y = np.array([True, True, False, False])
np.logical_and(X, Y)
# array([ True, False, False, False])
np.logical_or(X, Y)
# array([ True,  True,  True, False])
np.logical_not(X)
# array([False,  True, False,  True])
np.logical_xor(X, Y)
# array([False,  True,  True, False])
a = np.array([1, 0, 2, 0])
b = np.array([3, 4, 0, 0])
np.logical_and(a, b)
# array([ True, False, False, False])
