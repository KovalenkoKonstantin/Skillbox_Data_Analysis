import numpy as np

a = 6
b = 9
ages = np.array([
    [15, 23, 32, 45, 52],
    [68, 34, 55, 78, 20],
    [25, 67, 33, 45, 14]
])
# print(ages >= 16)
m = ages >= 16
m = (ages >= 16) & (ages < 60)
# m = sum((ages >= 16) & (ages < 60))

# print(m)
# print(m.sum())
n = (ages < 18) | (ages > 60)
# print(n)
k = ages[(ages >= 16) & (ages < 60)]
print(k)
