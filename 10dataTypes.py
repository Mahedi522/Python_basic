num=4.5
print(type(num))

num1=int(num)
print(type(num1))


num2=6+9j

print(type(num2))

a=5
b=8

c=complex(a,b)
print(c)
print(type(c))

d=a<b
print(d)
print(type(d))

print(int(d))

print(int(True))
print(int(False))

lst=[34,4,3,4,3,33,23]
print(type(lst))

st={34,34,3,43,4,34354,5,34,34234,45}
print(type(st))

tp=(23,23,4,4,56,7)
print(type(tp))

str='Mahedi'
print(type(str))

#range

range(10)
print(range(10))
print(list(range(10)))
print(type(range(10)))

print(list(range(2,10,2)))

d={'mahedi':'iphone','evan':'samsung','romman':'blackberry'}
print(d.keys())
print(d.values())
print(d['mahedi'])

print(d.get('evan'))