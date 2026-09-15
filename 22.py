import numpy as np

arr = np.array([50, 60, 70, 80, 90])
standardized = (arr - np.mean(arr)) / np.std(arr)
print(standardized)