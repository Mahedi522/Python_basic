def sort(list):
    temp = 0
    for i in range (len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list


list = [8, 7, 6, 5, 4, 3, 2, 1]
print(sort(list))