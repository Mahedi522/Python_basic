pos = -1


def b_search(list, n):
    lb = 0
    ub = len(list)-1

    while lb <= ub:
        mid = (lb+ub)//2

        if list[mid] == n:
            globals()['pos'] = mid + 1
            return True
        elif n < list[mid]:
            ub = mid - 1
        else:
            lb = mid + 1
    return False


list = [2, 3, 34, 6, 88, 54, 32, 6, 8, 34, 23, 6, 7, 87, 54, 2]
list.sort()
print(list)

n = 320

if b_search(list, n):
    print("Found at: ", pos)
else:
    print("Not Found")
