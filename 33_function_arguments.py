def update(x):
    print(id(x))
    x = 8
    print("x", x)
    print(id(x))


a = 10
print(id(a))
update(a)
print("a", a)


def update1(y):
    print(id(y))
    y[1] = 10
    print(y)
    print(id(y))


lst = [2, 3, 4, 5]
print(lst)
print(id(lst))
update1(lst)
