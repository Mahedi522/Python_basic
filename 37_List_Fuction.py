lst = [23, 33, 45, 56, 6, 76, 34, 345, 99]

def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        elif i % 2 != 0:
            odd += 1
    return even, odd


even, odd = count(lst)
print(even)
print(odd)
print("even: {} and odd: {}".format(even, odd))
