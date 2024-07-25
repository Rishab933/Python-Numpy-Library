# The linspace function in numpy returns evenly scaped values within the given interval
# np.linspace(start_val, stop_val, (how many numbers in output)num=50, enbdpoint=false, retstep=true, dtype=none)

import numpy as np
a = np.linspace(2, 20, 10)
print(a)

# including endpoint
a = np.linspace(2, 20, 10, endpoint=False)
print(a)

a = np.linspace(2, 20, 10, endpoint=True)
print(a)

# including retstep
a = np.linspace(2, 20, 10, endpoint=True, retstep=True)
print(a)

a = np.linspace(2, 20, 10, endpoint=True, retstep=False)
print(a)

#including dtype
a = np.linspace(2, 20, 10, endpoint=True, retstep=True, dtype=int)
print(a)

a = np.linspace(2, 20, 10, endpoint=True, retstep=True, dtype=str)
print(a)

# by default it has the ability to show 50 values
a = np.linspace(2, 20, retstep=True)
print(a)
