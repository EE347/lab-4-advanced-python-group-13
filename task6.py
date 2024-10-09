import numpy as np

x = np.ones((8, 8))
print('Before:')
print(x)

# Modify the inner part of the array to be zeros
x[1:-1, 1:-1] = 0

print('After:') 
print(x)