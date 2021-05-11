'''
x = int(input("enter a number: "))
if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
    print("It's not a prime number")
else:
    print("it's a prime number")
'''

count = 0
x = int(input("enter a number: "))
for i in range(2, x):
    if x % i == 0:
        count += 1
        break
if count == 1:
    print(x, "this is not a prime number")
else:
    print(x, "This is a prime number")
