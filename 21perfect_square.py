from math import sqrt
for i in range(1, 50):
    if sqrt(i).is_integer():
        print(i)

for i in range(50, 0, -1):
    if sqrt(i) % 1 == 0:
        print(i)

