import numpy as np
import time

lst = list(range(1000000))

start = time.time()
result = [x * 2 for x in lst]
list_time = time.time() - start

arr = np.arange(1000000)

start = time.time()
result = arr * 2
numpy_time = time.time() - start

print("List Time :", list_time)
print("NumPy Time:", numpy_time)