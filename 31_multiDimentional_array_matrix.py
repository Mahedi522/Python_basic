from numpy import *

arr = array([
    [1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9]
])
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr2 = arr.flatten()  # 2 dimension to 1 dimension
print(arr2)
print("Reshape")
arr3 = arr2.reshape(3,4)  # 1 dimension to 3 dimension
print(arr3)

print("2 2 dimensional array in a 3d array")
arr4 = arr2.reshape(2, 2, 3)  # 1 dimension to 3 dimension
print(arr4)