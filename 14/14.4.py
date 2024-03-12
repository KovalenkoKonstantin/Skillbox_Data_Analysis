import numpy as np

m = np.array([[2, 5],
              [6, 8],
              [1, 3]])
print(m)
print(m.ndim)
print(m.shape)
print(m.size)
print(m[1][0])

try:
    print(m[1, 10])
except IndexError:
    print('Out of bounds')

print(m[2])

# срезы spices
print(m[0:2])
print(m[1:])
print(m[:1])
print(m[:])

# шаг
print(m[0:2:2])
print(m[::2])

# отрицательный шаг
print(m[::-1])
