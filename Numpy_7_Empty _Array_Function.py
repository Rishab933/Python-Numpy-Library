# Empty function is used to create an array of random values, of given shape ans size and data type, without initializing the entries

import numpy as np

# 1D array
a = np.empty(5)
print(a)

a = np.empty(5, dtype=int)
print(a)

a = np.empty(5, dtype=object)
print(a)

# 2D Array
a = np.empty((5, 3), dtype=int)
print(a)

a = np.empty((5, 3), dtype=object)
print(a)

# 3D Array
a = np.empty((2, 5, 3), dtype=int)
print(a)

a = np.empty((2, 5, 3), dtype=object)
print(a)
print(a.shape)
print(a.size)
