import numpy as np
from numpy import random

# ones like array: it returns an array of ones with the shape and type as of the given array
a = np.array([1, 2, 3, 4])
b = np.ones_like(a)
print(b)
print()

c = np.random.random((3, 4))
print(np.ones_like(c))

c = np.random.random((3, 4))
print(np.ones_like(c, dtype=int))
print()

# zeros like array: it returns an array of zeros with the shape and type as of the given array
a = np.array([1, 2, 3, 4])
b = np.zeros_like(a)
print(b)
print()

c = np.random.random((3, 4))
print(c)
print(np.zeros_like(c, dtype=int))
print()

# Full like array
a = np.array([1, 2, 3, 4])
b = np.full_like(a, 7)
print(b)
print()

c = np.random.random((2, 3, 4))
print(c)
print(np.full_like(c, 10, dtype=int))
print()
