# python is not call by value or not call by reference

def update(x):
    print(id(a))
    x = 8       # address changes, because its not mutable
    print(id(x))
    print(x)


a = 10
print(id(a))
update(a)

print(a)


def update_lst(x):
    print(id(x))
    x[1] = 5      # address not changes, because it's mutable
    print(id(x))
    print(x)


l = [12, 34, 45]
print(id(l))
update_lst(l)
