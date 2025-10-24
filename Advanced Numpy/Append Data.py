'''
np.append(array_to_append, Values_to_append, axis=None)
'''

import numpy as np

arr = np.array([[1, 2, 3, 4, 5, 6]])
added_arr = np.append(arr, [7, 8, 9, 10, 11, 12])
print(added_arr)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
added_arr_2d = np.append(arr_2d, [[7, 8, 9]], axis=0)
print(added_arr_2d) 
