import numpy as np

scores = np.array([3, 5, 7, 9, 8, 10])
pairs = scores.reshape(3, 2)
print(pairs)

print(scores.ndim)
print(pairs.ndim)

scores.reshape(3, 2)

t = pairs.transpose()
print(t)
print(
    t.ravel())  # returns a view of the original array whenever possible.
# This isn't visible in the printed output,
# but if you modify the array returned by ravel,
# it may modify the entries in the original array.
# If you modify the entries in an array returned from flatten this will never happen.
# ravel will often be faster since no memory is copied,
# but you have to be more careful about modifying the array it returns.
print(t.flatten())  # always returns a copy
