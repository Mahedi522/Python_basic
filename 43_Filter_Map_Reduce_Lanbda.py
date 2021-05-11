from functools import reduce
'''def is_even(n):
    print(n % 2 == 0)
'''

nums = [2, 4, 3, 5, 6, 7, 8]

# evens = list(filter(is_even, nums))


even = list(filter(lambda a: a % 2 == 0, nums))
print(even)
double = list(map(lambda a: a*2, nums))
print(double)

"""
def add_all(a, b):
    return a+b
"""

sum = reduce(lambda a, b: a+b, nums)
print(sum)

'''from functools import reduce


def add(a, b):
    return a + b


l = [3, 4, 6, 34, 65, 44]

x = reduce(add, l)

print(x)

print(list(filter(lambda y: y % 2 == 0, l)))

print(list(map(lambda z: z*2, l)))
'''


