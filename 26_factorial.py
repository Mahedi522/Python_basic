x = int(input("enter a number: "))
f = 1
j = 1
for i in range(1, x):
    f = i * j
    j = j + f
print(j)
z = 1
for i in range(1, x + 1):
    z = z * i
print(z)
