from numpy import *
arr = array([1, 2, 3, 4, 5])
arr1 = array([10, 20, 30, 40, 50])
arr2 = zeros(len(arr), int)
for i in range(len(arr)):
    print(i)
    arr2[i] = (arr[i]+arr1[i])
print(arr2)
