# Python3 program to demonstrate the use of
# strip() method

string = """    geeks for geeks    """

# prints the string without stripping
print(string)

# prints the string by removing leading and trailing whitespaces
print(string.strip())

# prints the string by removing geeks
print(string.strip(' geeks'))

a = list(map(int, input().rstrip().split()))
print(a)
print(type(a[1]))
