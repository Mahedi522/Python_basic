def sort(list):
    temp = 0
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


li = [34, 45, 57, 32, 87, 34, 9, 4, 23]
print(li)
sort(li)
print(li)
