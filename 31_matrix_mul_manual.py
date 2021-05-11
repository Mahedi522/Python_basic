from numpy import *

arr1 = array([[2, 3, 4], [5, 6, 7]])
arr2 = array([[5, 5], [5, 5], [5, 5]])
arr3 = array([zeros(2), zeros(2)], int)
sum = 0
for i in range(2):
    for j in range(2):
        for k in range(3):
            sum = sum + arr1[i][k] * arr2[k][j]
            arr3[i][j] = sum
        sum = 0
print(arr3)