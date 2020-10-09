
# def print1(str1):
#     print("This is  " + str1)
#     print1(str1)
#
# print1("herry")

def functorial_iterative(n):
    '''

    :param n: integer
    :return: n * n-1 * n-2 * n-3.......1
     '''

    fac = 1
    for x in range(n):
        fac = fac * (x+1)
    return fac


def functorial_recursive(n):
    '''

    :param n: integer
    :return: n * n-1 * n-2 * n-3.......1
     '''

    if n == 1:
        return 1
    else:
        return n * functorial_recursive(n-1)



# iterative
# n! =>  n * n-1 * n-2 * n-3.......1
# n! => n * (n-1)!
number = int(input("Enter the number"))
print("factorial using iterative Method",functorial_iterative(number))
print("factorial using recursive Method",functorial_recursive(number))



def fibonaci(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        print(n)
        return fibonaci(n-1)+fibonaci(n-2)





number = int(input("Enter the fibonacci number"))
print(fibonaci(number))



