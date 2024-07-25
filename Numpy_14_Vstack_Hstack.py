# It is used to combine 2 or more arrays to form a new array
# vstack combines the array vertically
# hstack combines the array horizontally

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
b = np.array([10, 20, 30, 40, 50])
print(b)
print()

c = np.vstack((a, b))
print(c)
print()

c = np.hstack((a, b))
print(c)
print()

a = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])
print(a)
x = np.array([[12, 22, 32, 42, 52], [110, 120, 130, 410, 510]])
print(x)
print()

c = np.vstack((a, x))
print(c)
print()

c = np.hstack((a, x))
print(c)
print()