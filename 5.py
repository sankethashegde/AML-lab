import numpy as np
arr = np.arange(1, 25)

a = arr.reshape(4, 6)
b = arr.reshape(6, 4)
c = arr.reshape(2, 3, 4)

print(a.shape, a.ndim)
print(b.shape, b.ndim)
print(c.shape, c.ndim)