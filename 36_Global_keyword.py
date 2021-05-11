a = 10
b = 15
c = 30

g = 50
print(id(g))


def something():  # preference local variable first
    b = 20   # local variable b
    print("In function: ", b)
    print("in fun b: ", a)   # we can access a global variable from a function as well
    global c     # for changing global variable from a fun
    c = 40
    print("in fun c: ", c)
    x = globals()["g"]
    print(id(globals()["g"]))
    print("In fun local g: ", globals()["g"])
    globals()["g"] = 65
    g =6
    print("In fun g: ", g)


something()
print(id(g))
print("Out Fun b: ", b)
print("Out Fun c: ", c)
print("out fun g: ", g)