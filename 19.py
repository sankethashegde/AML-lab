import numpy as np

arr = np.random.randint(1, 20, 20)

unique, freq = np.unique(arr, return_counts=True)

print("Unique:", unique)
print("Frequency:", freq)