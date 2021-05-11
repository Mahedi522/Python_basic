from array import *

val = array('i', [5, 4, -6, 3, 7, 4])

print(val)

print(val.buffer_info())
print(val.typecode)
val.reverse()
print(val)
val.append(12)
print(val)
print(val[0])

for i in range(len(val)):     # or for i in range val:
    print(val[i], end=" ")

char = array('u', ['a', 'f', 'r', 'g'])

print(char)
for e in char:
    print(e)

newVal = array(val.typecode, [a for a in val])
for i in newVal:
    print(i)

newVal = array(val.typecode, [a*a for a in val])
for i in newVal:
    print(i)

newVal = array(val.typecode, [a**3 for a in val])
i = 0
while i < len(newVal):
    print(newVal[i], end=",")
    i += 1
