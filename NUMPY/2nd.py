import numpy as np

arr = np.arange(10, 50, 2).reshape(4, 5)
print("Original Matrix: \n", arr)


third_column = arr[:, 2]
print("\nThird Column:")
print(third_column)



arr[3] = [1, 2, 3, 4, 5]
print("\nAfter changing fourth row:")
print(arr)