import numpy as np

arr_int = np.array([1, 2, 3])
arr_float = np.array([10.00, 11.00, 12.00])
arr_str = np.array(["100", "200", "300"])

print("Previous Array")
print(arr_float)
int_arr = arr_float.astype(int)

print()

print("Current Array")
print(int_arr)