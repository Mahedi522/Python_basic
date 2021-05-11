def fib(x):

    first, second = 0, 1
    for i in range(x):
        if i <= 1:
            print(i)
        else:
            fibo = first + second
            first = second
            second = fibo
            print(fibo)


fib(3)
