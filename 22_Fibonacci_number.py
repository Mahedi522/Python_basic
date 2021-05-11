first, second = 0, 1
for i in range(0, 51):
    if i <= 1:
        fibo = i
        print(i)
    else:
        fibo = first+second
        first = second
        second = fibo
        print(fibo)
