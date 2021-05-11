lst = []
n = int(input("Enter Number of Names: "))


def length(x):
    a = 0
    for i in range(x):
        name = input("Enter no.{} name: ".format(i))
        lst.append(name)
        if len(lst[i]) > 5:
            a += 1
        #print(lst[i], "has {} letters".format(len(lst[i])))

    return a


a = length(n)
print(a, "users has length more than 5 letter")



'''lst = []
n = int(input("Enter Number of Names: "))


def length(x):
    lst1 = []
    for i in range(x):
        name = input("Enter no.{} name: ".format(i))
        lst.append(name)
        lst1.append(len(lst[i]))
    return lst1


lst3 = length(n)
print(lst3)
'''