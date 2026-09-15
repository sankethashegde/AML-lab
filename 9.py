import numpy as np

marks = np.array([45, 78, 89, 32, 67, 90, 55, 76, 41, 84])

print(marks[marks > 75])
print(marks[(marks >= 50) & (marks <= 80)])
print(np.sum(marks < 50))
print((np.sum(marks >= 60) / len(marks)) * 100)