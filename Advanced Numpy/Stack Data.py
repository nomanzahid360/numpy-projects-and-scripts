'''
vstack() --> Verticaly Stack Data
hstack() --> Horizontaly Stack Data
dstack() --> Depth Stack Data
column_stack() --> Column Stack Data
'''

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
newarr = np.vstack((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Verticaly Stacked Array:")
print(newarr)
print("\n")
newarr = np.hstack((arr1, arr2))
print("Array 1:", arr1) 
print("Array 2:", arr2)
print("Horizontaly Stacked Array:")
print(newarr)
print("\n")
