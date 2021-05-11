def div(a, b):
    print(a/b)


def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div = smart_div(div)
div(4, 8)

'''def smart_div(a,b):
    if a<b:
        a,b = b,a
    return div(a,b)


div1= smart_div(4,8)

#div1(4,8)'''


def smrt_div(f):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return f(a, b)
    return inner


def sub(a, b):
    print(a - b)


d = smrt_div(sub)
d(3,5)
