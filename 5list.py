nums=[12,34,456,67,34]  # different types of value List

print(nums)

print(nums[0])
print(nums[1:3])


names=['mahedi','evan','romman']
print(names)
print(names[1])

values=[9.5,'Mahedi',25]

mil=[nums,names]

print(mil)

nums.append(45)
print(nums)

nums.sort()
print(nums)

nums.insert(2,55)
print(nums)

nums.remove(34)
print(nums)


print(nums.pop(4))
print(nums)

print(nums.pop())

del nums[2:]
print(nums)

nums.extend([12,45,78,33])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

nums.sort()
print(nums)

nums[2]=333
print(nums)