import numpy as np

# Create a NumPy array containing 10 numbers
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("NumPy Array:")
print(arr)

print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)


# One-dimensional array
one_d = np.array([1, 2, 3, 4, 5])

print("\nOne-Dimensional Array:")
print(one_d)


# Two-dimensional array
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nTwo-Dimensional Array:")
print(two_d)

print("Shape of 2D Array:", two_d.shape)