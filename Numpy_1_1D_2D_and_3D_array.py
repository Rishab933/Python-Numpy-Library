import numpy as np

# creating 1D array:
a1 = np.array([1, 2, 3, 4])
print(a1)
print(type(a1))
print(a1.shape)
print(a1.size)
print()

#creating a 2D array:
a2 = np.array([[1,  2, 3, 4], [4, 3, 2, 1]])
print(a2)
print(type(a2))
print(a2.shape)
print(a2.size)
print(a2.ndim)
print()

#creating 3D array:
a3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
print(a3)
print(type(a3))
print(a3.shape)
print(a3.size)
print(a3.ndim)
print()