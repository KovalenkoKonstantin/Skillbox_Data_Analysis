import numpy as np

marks = np.array([5, 4, 3, 5, 4, 3, 4])
print(marks)
marks.min()
marks.max()
print(marks.mean())
marks.argmax()
marks.argmin()

grades = np.array([[3, 5, 5, 4, 3],
                   [3, 3, 4, 3, 3],
                   [5, 5, 5, 4, 3]])
print(grades)
print(grades.mean(axis=1))
print(grades.mean(axis=0))

