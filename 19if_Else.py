if True:
    print("I'm right")

print("not belongs into if.")


x = int(input("Enter a number: "))
r = x % 2

if r == 0:
    print("Even")
    if x > 6:
        print("greater than 6")
    else:
        print("smaller than 6")
else:
    print("Odd")


# elif   #if one condition is true than doesn't check other condition.

if x == 1:
    print("One")
elif x == 2:
    print("two")
elif x == 3:
    print("four")
else:
    print("not belongs to 1,2,3,4")
