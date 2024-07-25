# Unary operators are limited to one operand
# can be applied row wise or column wise using the axis parameter

import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(a.shape)
print()

# Max and min and sum in the array
print(a.max())
print(a.min())
print(a.sum())
print()

a = np.array([[1, 2, 3, ], [4, 5, 6]])
print(a)
print(a.ndim)
print(a.shape)
print()
print(a.max())
print(a.min())
print(a.sum())
print()

#axis = 1 is for rows
#axis = 0 is for columns

print(a.max(axis=1))
print(a.max(axis=0))
print()

print(a.min(axis=1))
print(a.min(axis=0))
print()

print(a.sum(axis=1))
print(a.sum(axis=0))
print()

# To create a 3D array
c = np.arange(18).reshape(2, 3, 3)
print(c)
print(c.max())
