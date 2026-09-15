import numpy as np

matrix = np.random.random((5, 5))

print("Row Means:", np.mean(matrix, axis=1))
print("Column Means:", np.mean(matrix, axis=0))