import numpy as np

print(np.sqrt(17))
print(np.log(4))
print(np.mean([20, 40, 30, 450, 45, 30]))
print(np.median([20, 40, 30, 450, 45, 30]))
print(np.array([2, 3, 4]))
print(np.array([[5, 2, 3.5], [1, 9, 6.5]]))
print(np.array([[[6, 3],
                 [6, 8]],
                [[1, 0],
                 [0, 1]]]))
print(np.array([['Ann', ' Kate'],
                [23, 24]]))
turnout = np.array([0.62, 0.43, 0.79, 0.56])
print(turnout)
print(turnout * 100)
print(np.array([2, 3, 8, ]) + np.array([7, 8, 9]))
week1 = np.array([4000, 0, 2000, 0, 1200])
week2 = np.array([1000, 2000, 0, 0, 3500])
week_all = week1 + week2
print(week_all)
(week1 + week2) / 2
