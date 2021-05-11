for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(j), end="")
    print()

for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(i), end="")
    print()

for i in range(65, 70):
    k = i
    for j in range(65, i+1):
        print(chr(k), end="")
        k = k+1
    print()

name="Mahedi"
for i in range(6):
    for j in range(i+1):
        print(name[j], end="")
    print()

for i in range(65, 70):
    for j in range(i, 64, -1):
        print(chr(j), end="")
    print("")

for i in range(4):
    for j in range(4):
        if i < j:
            print(chr(65+14+j),end="")

        else:
            print(chr(65+j), end="")
    print()
