def sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):

            if list[j] < list[i]:
                min = j

        temp = list[i]
        list[i] = list[min]
        list[min] = temp

        print(list)

    return list


list = [8, 7, 6, 5, 4, 3, 2, 1]
sort(list)
print(list)