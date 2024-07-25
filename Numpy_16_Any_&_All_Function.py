# Any an all function are build in function
# Works on comparison basis
# Any function returns true if any element satisfy the given condition
# All function returns true if all element satisfy the given condition
# np.all(condition) -->uses and operator
# np.any(condition) -->uses or operator

import numpy as np
x = np.random.randint(10, 100, 15)
print(x)

print(np.any(x == 12))
print(np.any(x > 102))

print(np.all(x > 12))
print(np.all(x < 120))

x = np.random.randint(10, 100, (2, 2))
print(x)

print(np.any(x == 12))
print(np.any(x > 102))

print(np.all(x > 12))
print(np.all(x < 120))