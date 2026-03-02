import numpy as np

print("===== NUMPY ARRAY OPERATIONS =====\n")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

add_result = a + b
print("\nAddition (a + b):", add_result)

mul_result = a * b
print("Multiplication (a * b):", mul_result)

c = np.array([[1, 2],
              [3, 4]])

d = np.array([[5, 6],
              [7, 8]])

print("\nMatrix c:\n", c)
print("Matrix d:\n", d)

print("\nMatrix Addition:\n", c + d)

print("\nMatrix Multiplication (element-wise):\n", c * d)

print("\nSum of all elements in a:", np.sum(a))
print("Mean of a:", np.mean(a))
print("Max value in b:", np.max(b))

print("\n===== PROGRAM COMPLETED =====")