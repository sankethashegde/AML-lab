import numpy as np

sales = np.array([
    12000, 15000, 17000, 14000,
    18000, 21000, 19000, 22000,
    25000, 23000, 26000, 28000
])

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Month:", np.argmax(sales) + 1)
print("Lowest Month:", np.argmin(sales) + 1)
print("Months > 20000:", np.sum(sales > 20000))

increase = ((sales[-1] - sales[0]) / sales[0]) * 100
print("Percentage Increase:", increase)