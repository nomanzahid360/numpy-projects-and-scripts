'''
np.insert(Array_Name, Index_Position, Value_to_Insert, Axis=0)
axis=0 means to insert values along rows
axis=1 means to insert values along columns
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
newarr = np.insert(arr, 3, 4)
print(newarr)
print(arr)

print("\n\n")

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
newarr_2d = np.insert(arr_2d, 1, [0, 2, 5], axis=0)
print(newarr_2d)
