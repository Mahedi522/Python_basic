num=5

print(id(num))

name='Mahedi'

print(id(name))   #address in memory

a=10
b=a

print(id(a))
print(id(b))
print(id(10))

k=10
print(id(k))

a=9
print(id(a))

k=a
print(id(k))

b=a
print(id(b))

print(id(10))

PI=3.14  #in python constant declaration is not possible.
print(PI)
PI=3.15
print(PI)#by capital letter declaration we want to say this is constant.

print(type(PI))
print(type(a))