# formal argument , actual argument
# actual argument--> position,keyword,default,variable length

#position
def position(name, age):
    print(name)
    print(age)

position("Mahedi", 25)

# keyword
def keyword(name, age):
    print(name)
    print(age-5)

keyword(age = 25, name = "Mahedi")

# Default
def default(name, age = 18):
    print(name)
    print(age)

default("Mahedi")

# variable length
def add(a, *b):
    sum = a
    for i in b:
        sum = sum + i
    print(sum)

add(5, 5, 10, 10, 10)

# or

def add(*b):
    sum = 0
    for i in b:
        sum = sum + i
    print(sum)

add(5, 5, 10, 10, 10)


