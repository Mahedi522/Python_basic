nums = [14, 23, 43, 23, 11]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not Found")
