import numpy as np

# default data type is float
a = np.identity(3)
print(a)
print()

a = np.identity(3, dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print()

# we can perform arithmatic functions also
a = a*2
print(a)
print()

a = a+2
print(a)
print()

a = a/2
print(a)