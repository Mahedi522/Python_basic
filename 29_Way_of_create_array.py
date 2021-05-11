from numpy import *
# 6 Way
# array()
arr = array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype)

# linspace()    # devide into how many parts  #gap between 2 element is fixed

arr1 = linspace(0, 16, 3)  # By default part is 50
print(arr1)

# arange()     # skip steps

arr2 = arange(1, 16, 2)  # steps skip steps
print(arr2)

# logspace()

arr3 = logspace(1, 5, 5)  # start from 10**1 to 10**50 and it will get devided into 5 parts
print(arr3)
print('%.2f' % arr3[1])

# zeros() #efficient #by default value 0

arr4 = zeros(5)
print(arr4)

# ones() #efficient #by default value 1

arr5 = ones(5)
print(arr5)
