import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original array:", arr)
print("Element at index 2:", arr[2])
print("Elements from index 2 to 5:", arr[2:6])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D array:")
print(matrix)
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
print("Element at row 2, column 3:", matrix[1, 2])

reshaped = arr.reshape(2, 5)
print("\nReshaped array (2 rows, 5 columns):")
print(reshaped)
print("Original array remains:", arr)
