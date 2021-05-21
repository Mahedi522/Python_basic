def sockMerchant(n, ar):
    x = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if ar[i] == ar[j]:
                del ar[j]
                x += 1
                break
    return x


li = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(len(li), li)
print(li)
print(result)