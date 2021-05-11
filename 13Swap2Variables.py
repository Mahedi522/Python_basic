a=5
b=6

temp=a
a=b
b=temp
print(a)
print(b)

b=a+b
a=b-a
b=b-a
print(a)
print(b)

#XOR
b=a^b
a=b^a
b=b^a
print(a)
print(b)

#Python way

a,b=b,a

print(a)
print(b)