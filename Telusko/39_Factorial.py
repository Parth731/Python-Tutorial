
# 5!  5*4*3*2*1


def fact(n):

    f = 1
    for x in range(1,n+1):
        f = f * x
        print(f,end=" ")
    return f


res = fact(5)
print()
print(res)