'''
np.delete(array_name, index_to_delete, axis_number)
'''

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print("Original 1D array:", arr_1d)
new_arr_1d = np.delete(arr_1d, 2)  # Delete element at index 2
print("1D array after deletion:", new_arr_1d)

print("\n\n")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:\n", arr_2d)
new_arr_2d = np.delete(arr_2d, 1, axis=0)  # Delete row at index 1
print("2D array after deleting row 1:\n", new_arr_2d)