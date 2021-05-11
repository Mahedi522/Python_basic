for j in range(4):
    for i in range(4):
        print("# ", end="")
    print("")

for i in range(4):
    for j in range(i+1):
        print("#", end="")
    print("")

for i in range(4):       # when i =0;  j=4-i=4;
    for j in range(4-i):
        print("#", end="")
    print("")


for i in range(4):
    print(i)

