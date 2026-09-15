import numpy as np

salary = np.array([25000, 32000, 28000, 45000,
                   50000, 38000, 42000, 30000])

print("Total:", np.sum(salary))
print("Average:", np.mean(salary))
print("Highest:", np.max(salary))
print("Lowest:", np.min(salary))
print("Median:", np.median(salary))
print("Std Dev:", np.std(salary))