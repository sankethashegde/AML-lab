import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 70, 72],
    [88, 92, 85],
    [55, 60, 58]
])

total = np.sum(marks, axis=1)
avg_student = np.mean(marks, axis=1)
avg_subject = np.mean(marks, axis=0)

print("Total:", total)
print("Average:", avg_student)
print("Subject Average:", avg_subject)
print("Highest Total Student:", np.argmax(total) + 1)
print("Highest in each subject:", np.max(marks, axis=0))