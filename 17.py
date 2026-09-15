import numpy as np

arr = np.random.randint(1, 101, 20)

arr[arr < 50] = 0
print(arr)