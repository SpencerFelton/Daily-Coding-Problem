def fib(n):
    iniFib = 0
    fib = 1
    while n >=1:
        temp = fib
        fib = fib + iniFib
        iniFib = temp
        n -= 1
    return(fib)

fib(5)

def encoded(n):
        maxEncodings = fib(int(len(n)))
        print(maxEncodings)

encoded("12345678")
