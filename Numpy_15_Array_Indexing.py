# [start_index:stop_index]
# [0:4] --> it will print all the elements from 0 to 3(4-1)
import numpy as np

# 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print()

print(a[0])
print(a[2])
print(a[0:])
print(a[0:5])
print(a[:2])
print()

a = np.array([[1, 2, 3, ], [4, 5, 6]])
print(a)
print(a.ndim)
print(a.shape)
print()
print(a[0])
print(a[1])
print(a[:])
print(a[0, 1:2])
print(a[1, 1:2])
print()
print(a[a > 4])
print()

# 3D array
c = np.arange(18).reshape(2, 3, 3)
print(c)
print(c[0, 1, 1]) #-->4

#printing 15 to 17 --> second matrix 3rd row all the columns
print(c[1, 2, :])
print(c[1, 1, 1]) #-->13


