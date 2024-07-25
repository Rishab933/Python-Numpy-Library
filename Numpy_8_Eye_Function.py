# The eye function returns a 2D array with 1 on the dialonals and 0 else where
# np.eye(shape,k(index of diagonal),dtype)
# if only number of rows is passed then it creates a square matrix of that row number
import numpy as np

a = np.eye(4)
print(a)

# using k
a = np.eye(4, k=0)  #k=0 represents the main diagonal
print(a)

a = np.eye(4, k=1)  # diagonal start point changes
print(a)
print()

a = np.eye(4, k=-1)
print(a)

a = np.eye(4, k=1, dtype=int)
print(a)
print()

a = np.eye(4, 5)
print(a)
print()

a = np.eye(5, 4)
print(a)
print()

a = np.eye(4, 5, k=1, dtype=int)
print(a)
print()

a = np.eye(4, 5, k=1, dtype=str)
print(a)
print(a.ndim)
print()
