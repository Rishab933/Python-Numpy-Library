import numpy as np

# creating a zeros array
a = np.zeros(3)
print(a)
print()

a1 = np.zeros(5, dtype=int)
print(a1)
print()

# creating 2D zeros array
b = np.zeros((3,4), dtype=int)
print(b)
print(b.shape)
print(b.size)
print()

# creating 3D zeros array
c = np.zeros((2,3,4), dtype=int)
print(c)
print(c.shape)
print(c.size)

