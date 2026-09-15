import numpy as np

marks = np.random.randint(0, 101, 100)

print("0-39 :", np.sum((marks >= 0) & (marks <= 39)))
print("40-59:", np.sum((marks >= 40) & (marks <= 59)))
print("60-79:", np.sum((marks >= 60) & (marks <= 79)))
print("80-100:", np.sum((marks >= 80) & (marks <= 100)))