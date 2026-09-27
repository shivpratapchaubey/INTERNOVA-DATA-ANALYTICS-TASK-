import numpy as np

# Original array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:")
print(arr)

# Indexing
print("\nElement at index 0:", arr[0])
print("Element at index 4:", arr[4])
print("Last element:", arr[-1])

# Slicing
print("\nFirst five elements:")
print(arr[:5])

print("\nElements from index 2 to 6:")
print(arr[2:7])


# Two-dimensional array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nTwo-Dimensional Array:")
print(matrix)

# Access rows
print("\nFirst Row:")
print(matrix[0])

print("\nSecond Row:")
print(matrix[1])

# Access columns
print("\nFirst Column:")
print(matrix[:, 0])

print("\nSecond Column:")
print(matrix[:, 1])

# Reshaping
original = np.array([1, 2, 3, 4, 5, 6])

reshaped = original.reshape(2, 3)

print("\nOriginal Array:")
print(original)

print("\nReshaped Array:")
print(reshaped)