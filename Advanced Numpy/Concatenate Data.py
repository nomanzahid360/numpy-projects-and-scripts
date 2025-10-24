'''
np.conactenate((Array1, Array2), axis=0)
'''

import numpy as np

arr = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
newarr = np.concatenate((arr, arr2))

print("Array 1:", arr)
print("Array 2:", arr2)
print("Concatenated Array:")
print(newarr)