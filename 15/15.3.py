import numpy as np

# income = np.array([[20000, 30000, 25000, 700000],
#                    [23000, 35000, 20000, 32000]])
# a = np.log(income)  # натуральный логорифм
#
# print(a)
#
# # %matplotlib inline
# from matplotlib import pyplot as plt
#
# plt.plot(np.arange(8), income.flatten(), 'bo')
#
# # %matplotlib inline
# plt.plot(np.arange(8), np.log(income).flatten(), 'bo')

L = [2, 6, 7, 1]
# L ** 2
L_sq = [i ** 2 for i in L]
print(L_sq)
L_log = [np.log(num) for num in L]
print(L_log)
L_sqrt = [np.sqrt(j) for j in L]
print(L_sqrt)

