x = int(input("How many candy you want ? : "))
av = 4
i = 1
while i <= x:
    if av < i:
        print("Out of stock")
        break
    print("Candy")
    i += 1
print("Bye")
