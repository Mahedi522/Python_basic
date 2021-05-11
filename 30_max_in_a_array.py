from numpy import *

arr1 = array([10, 20, 30, 40, 50])

k = 0

for i in arr1:
    if i > k:
        k = i
    else:
        continue
print(k)
