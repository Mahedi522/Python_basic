
f = open('file', 'r')

# print(f.read())

# print(f.readline(), end='')
# print(f.readline(), end="")
# print(f.readline())


# f1 = open("File_1", "w")  # when execute clear previous data
# f1.write("Something ")
# f1.write("People")

f1 = open("File_1", "a")

f1.write(" Laptop")

for data in f:
    f1.write(data)
