'''
.ravel() --> Returns A View Of The Original Array, Flattened
.flatten() --> Returns A Copy Of The Original Array, Flattened
'''

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:")
print(arr_2d)

print("\nUsing ravel():", arr_2d.ravel())
print("Using flatten():", arr_2d.flatten())