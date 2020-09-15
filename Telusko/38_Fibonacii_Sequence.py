

# 0 1 1 2 3 5 8 13 21 fibonacii


def fib(n):

    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        # print(n)
        for x in range(2,n):
            prev = a + b
            a = b
            b = prev
            print(prev,end=" ")


fib(5)