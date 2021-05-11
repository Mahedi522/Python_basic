from math import ceil
num = int(input("Enter a number: "))
for i in range(2,  ceil(num/2)):
    if num % i == 0:
        print(num, "is not Prime",i)
        break
else:
    print(num, "is Prime")
