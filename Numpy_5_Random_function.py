import numpy as np
from numpy import random

# Random function:
# it returns random float numbers between 0 and 1
a = np.random.random()
print(a)
print()

a = np.random.random(4)
print(a)
print()

print("2D array with random values")
a = np.random.random((2, 3))
print(a)
print()

print("3D array with random values")
a = np.random.random((2, 2, 3))
print(a)

# Randint Function:

print("Random int vales")
a = np.random.randint(2, 13)  #(range between the number would be generated)
print(a)  #(the range start from 0 so lower limit is not nescessary but upper limit is )
print()

print("5 Random int vales")
a = np.random.randint(2, 13, 5)
print(a)
print()

# Rand Function:
# it also returns a float number between 0 and 1
print("rand")
a = np.random.rand()
print(a)
print()

print("4 values using rand")
a = np.random.rand(4)
print(a)
print()

print("2D array using rand")
a = np.random.rand(2, 3)
print(a)
print()

print("3D array using rand")
a = np.random.rand(2, 2, 3)
print(a)
print()

# Randn Function:
print("randn")
a = np.random.randn()
print(a)
print()

print("4 values using randn")
a = np.random.randn(4)
print(a)
print()

print("2D array using randn")
a = np.random.randn(2, 3)
print(a)
print()

print("3D array using randn")
a = np.random.randn(2, 2, 3)
print(a)
print()

# Uniform Function:
print("uniform")
a = np.random.uniform(2, 5)
print(a)
print()

print("4 values using uniform")
a = np.random.uniform(2, 5, 4)
print(a)
print()

print("uniform")
a = np.random.uniform(5)
print(a)
print()

print("uniform this will between 0 and 1")
a = np.random.uniform()
print(a)
print()

# Choice Function:
print("choice")
a = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)

print("choosing 2 numbers")
a = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
print(a)

print("choice")
a = np.random.choice(10, 40)  #this will create 40 random numbers between 0 to 10
print(a)

print("choice passing only one value")
a = np.random.choice(12)
print(a)

print("n choice without repetition")
a = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, replace=False)
print(a)
