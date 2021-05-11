pos = -1


def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False

# i = 0
# while i < len(list):
#     if list[i] == n:
#         globals()['pos'] = i
#         return True
#     i += 1
# return False


li = [2, 4, 5, 3, 6, 9, 22]
n = 9
if search(li, n):
    print("Found at : ", pos+1)
else:
    print("Not Found")
