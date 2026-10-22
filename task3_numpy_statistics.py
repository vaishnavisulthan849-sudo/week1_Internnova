import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Standard deviation:", round(np.std(a), 2))
print("Sum:", np.sum(a))
