import numpy as np

# creating a 1D ones array
a = np.ones(3)
# a = np.ones(3, float)
print(a)
print()

print("creating a 1D ones array")
a = np.ones(3, dtype=int)
print(a)
print()

print("creating a 2D ones array")
a = np.ones((2, 3), dtype=int)
print(a)
print(a.shape)
print(a.size)
print(a.ndim)
print()

print("creating a 3D ones array")
a = np.ones((2, 2, 3), dtype=int)
print(a)
print(a.shape)
print(a.size)
print(a.ndim)
print()