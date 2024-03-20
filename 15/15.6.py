import numpy as np

info = np.array([('Anna', 19, 168), ('Sam', 33, 175.5), ('Pam', 23, 180)],
                dtype=[('name', 'U10'), ('age', int), ('height', float)])
print(info)
np.save("info.npy", info)

new = np.load("info.npy")

print(new)

ages = np.array([61, 73, 18, 92])
np.savetxt("ages.txt", ages)

print(np.array2string(info))

print(ages.tolist())
