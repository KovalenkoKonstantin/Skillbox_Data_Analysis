import numpy as np

info = np.array([('Anna', 19, 168), ('Sam', 33, 175.5), ('Pam', 23, 180)],
                dtype=[('name', 'U10'), ('age', int), ('height', float)])
print(info)
print(info[0])
print(info[0:3:2])

print(info['age'])
print(info[['age', 'height']])
print(info['age'][0])
