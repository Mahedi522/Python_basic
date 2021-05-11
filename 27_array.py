from array import *

arr = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
for i in arr:
    print(i, end=",")
print()
# Manual method. have to found given values index
k = 0
val = int(input("enter the value: "))
for j in arr:
    if j == val:
        print(k)
        break
    k += 1
else:
    print("not found")
# function
print(arr.index(val))
