import numpy as np

temperature = np.array([
    31, 32, 33, 35, 36, 34, 32,
    30, 29, 31, 33, 35, 37, 36
])

avg = np.mean(temperature)

print("Mean:", avg)
print("Max:", np.max(temperature))
print("Min:", np.min(temperature))
print("Days Above Average:", np.sum(temperature > avg))
print("Above 34:", temperature[temperature > 34])
print("Difference:", np.max(temperature) - np.min(temperature))
print("Std Dev:", np.std(temperature))