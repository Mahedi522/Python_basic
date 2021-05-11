from array import *

arr = array('i', [23, 34, 45, 567, 78])

arr1 = array('i', [])


for i in range(len(arr)):
    if i == 2:
        continue
    arr1.append(arr[i])
arr = arr1
print(arr)

arr2 = array('i', [])

val = int(input("enter a value to delete: "))
for i in range(len(arr)):
    if arr[i] == val:
        continue
    arr2.append(arr[i])
arr = arr2
print(arr)
