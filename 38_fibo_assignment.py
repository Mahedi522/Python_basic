def fib(x):
    fibo = 0
    first, second = 0, 1
    for i in range(0,50):
        #if i <= 1:
            #print(i)
        #else:
        z = fibo
        fibo = first + second
        first = second
        second = fibo

        #print(fibo)
        if fibo > x-1:
            break
    return z


a = fib(50)
print(a)