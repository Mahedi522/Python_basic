from numpy import *

arr = array([2, 3, 4, 5, 6])
arr1 = array([20, 30, 40, 50, 60])

arr2 = arr+5
arr3 = arr+arr1
print(arr)
print(arr2)
print(arr3)
print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sort(arr))
print(concatenate([arr, arr1]))

# copy a array in different memory location
print("copy in different memory location")
arr2 = arr1.view()
print(id(arr2))
print(id(arr1))
# Shallow copy
print("shallow copy")
arr1[0] = 0  # when 1 value change another automatically changed
print(arr1)
print(arr2)

# deep copy
print("deep copy")
arr2 = arr1.copy()
print(id(arr2))
print(id(arr1))
# Shallow copy
arr1[0] = 7  # when 1 value change another automatically changed
print(arr1)
print(arr2)

