''''
decorator is add extra feature in existing function

swapping two number without teaching function

'''


def div(a,b):
    print(a/b)


def smart_div(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
            print(a,b)
        return func(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)