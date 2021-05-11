from array import *

arr = array('i', [23, 34, 45, 567, 78])
arr1 = array('i', [])
k = 0
for i in range(len(arr)-1, -1, -1):
    print(i)
    arr1.append(arr[i])
    # arr[k] = arr[i]
    # k += 1
arr = arr1
print(arr)
