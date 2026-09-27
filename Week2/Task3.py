import numpy as np

# Numerical dataset
data = np.array([10, 20, 30, 40, 50])

print("Dataset:")
print(data)

# Mathematical operations
print("\n----- Mathematical Operations -----")

print("Addition:", data + 5)
print("Subtraction:", data - 5)
print("Multiplication:", data * 2)
print("Division:", data / 2)

# Statistical operations
print("\n----- Statistical Operations -----")

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))