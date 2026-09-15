import numpy as np

marks = np.array([
    [78, 85, 90, 88],
    [65, 70, 72, 68],
    [92, 88, 95, 91],
    [55, 60, 58, 62],
    [80, 75, 82, 79]
])

total = np.sum(marks, axis=1)
avg = np.mean(marks, axis=1)

print("Totals:", total)
print("Averages:", avg)
print("Subject Average:", np.mean(marks, axis=0))
print("Highest Student:", np.argmax(total) + 1)
print("Lowest Student:", np.argmin(total) + 1)
print("Average > 80:", np.where(avg > 80)[0] + 1)
print("Class Average:", np.mean(marks))

categories = np.select(
    [avg >= 85,
     (avg >= 70) & (avg < 85),
     (avg >= 50) & (avg < 70),
     avg < 50],
    ["Excellent", "Good", "Average", "Needs Improvement"]
)

print(categories)