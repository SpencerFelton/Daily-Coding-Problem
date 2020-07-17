def fib(n):
    iniFib = 0
    fib = 1
    while n >=1:
        temp = fib
        fib = fib + iniFib
        iniFib = temp
        n -= 1
    return(fib)

def encoded(n):
        maxEncodings = fib(int(len(n)))
        print(maxEncodings)
        return maxEncodings

assert(encoded("12345678")) == 34
assert(encoded("123")) == 3
