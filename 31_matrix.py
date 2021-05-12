from numpy import *

arr = array([[1, 2, 3, 4], [5, 6, 7, 8]])

m = matrix(arr)
print(m)

print("matrix without creating an array")
m1 = matrix('1 3 5 7 ; 2 4 6 8')
print(m1)

print('3 column')
m1 = matrix('1 3 5; 7 2 4; 6 8 0')
print(m1)
print("min max")
print("min:", m1.min())
print("max:", m1.max())

print("diagonal")
print(diagonal(m1))

print('Addition and multiplication')
m1 = matrix('1 3 5; 7 2 4; 6 8 0')
m2 = matrix('1 2 5; 7 5 4; 6 4 0')
m3 = m1 + m2
m4 = m1 * m2
print("add")
print(m3)
print("mul")
print(m4)

print(m1.dtype)
print(m1.ndim)
print(m1.shape)
print(m1.size)
