li3 = []
li4 = set([])
li6 =[]
li7 = set([])
def getTotalX(a, b):
    m = min(b)
    for i in range(len(a)):
        for j in range(1, m):
            x = a[i]*j
            if x > m:
                break
            elif i == 0:
                li6.append(x)
            k = 0
            while i > 0 and k < len(li6):
                if li6[k] == x:
                    li7.add(li6[k])
                k += 1

    for i in range(len(b)):
        for j in range(1, b[i]+1):
            if b[i]%j == 0:
                if i == 0:
                    li3.append(j)
                k = 0
                while i > 0 and k < len(li3):
                    if li3[k] == j:
                        li4.add(j)
                    k += 1
# li7, li4 = map(set, (li7, li4))
    z = li7.intersection(li7, li4)
    s = len(z)
    return s