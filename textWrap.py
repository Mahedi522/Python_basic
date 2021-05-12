import textwrap
x = "hello world"
y = x.split()
print(y)
z = textwrap.wrap(x, 1)
print(z)
z = textwrap.fill(x, 1)
print(z)
