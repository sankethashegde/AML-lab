import numpy as np

arr = np.random.randint(1, 101, 20)

even = arr[arr % 2 == 0]
print(even)