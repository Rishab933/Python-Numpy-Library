# Transpose Function it changes the rows in column and vise versa

import numpy as np

a = np.array([[1, 2, 3,], [4, 5, 6]])
print(a)
print(a.ndim)
print(a.shape)
print()

b = np.transpose(a)
print(b)
print(b.shape)
print()

# Alternative way to do the transpose
b = a.T
print(b)
print(b.shape)
print()

# Transpose Function a 1D array
c = np.array([1, 2, 3, 4])
print(c)
print(c.shape)
print()
print(c.T)
# Transpose of 1D array does not works --> no change

# Transpose Function a 3D array
a = np.array([[[1, 2, 3,], [4, 5, 6], [0, 0, 0]]])
print(a)
print(a.ndim)
print(a.shape)
print()
print(a.T)
print(a.T.shape)