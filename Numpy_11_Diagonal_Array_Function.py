# Diagonal Function is used to extract the diagonal elements of an array
# np.diag(a(array), k(starting index))

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a.ndim)
print()

# extracting the diagonal elements of the given array
b = np.diag(a)
print(b)
print(b.ndim)
print()

# Representing this extracted array as a diagonal element
print(np.diag(b))
print()

# Using the second parameter k
c = np.diag(a, k=0)
print(c)
print()

c = np.diag(a, k=1)
print(c)
print()

c = np.diag(a, k=2)
print(c)
print()

c = np.diag(a, k=-1)
print(c)
print()

c = np.diag(b, k=0)
print(c)
print()

c = np.diag(b, k=1)
print(c)
print()

c = np.diag(b, k=-1)
print(c)
print()

# If starting index is not in the array then it prints an empty array
c = np.diag(a, k=4)
print(c)
print()