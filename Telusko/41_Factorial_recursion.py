

def fact(n):

    if n == 0:
        return 1
    print(n,end=" ")
    return n * fact(n-1)





res = fact(5)
print()
print(res)