from array import *

val = array('i', [34, 56, 34, 78, 43, 65, 86, 33, 465])

for i in range(len(val)):
    for j in range(len(val)):
        if val[i] < val[j]:
            temp = val[i]
            val[i] = val[j]
            val[j] = temp
for i in val:
    print(i, end=',')
