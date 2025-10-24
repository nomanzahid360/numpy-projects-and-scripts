'''
np.split(array_to_split, indices_or_sections, axis=0)
np.hsplit(array_to_split, indices_or_sections)
np.vsplit(array_to_split, indices_or_sections)
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(arr)

# Split the array into 3 parts
newarr = np.split(arr, 2)
print("\nSplit the array into 2 parts:")
print(newarr)

import numpy as np