import textwrap
x = '2345678'
nums = []
for i in x:
    nums.append(int(i))
print(nums)

it = iter(nums)

print(it.__next__())

for i in nums:
    print(i)

print(it.__next__())
print(next(it))

#
# z = textwrap.wrap(x, 1)
# y = [int(i) for i in z]
# print(y)