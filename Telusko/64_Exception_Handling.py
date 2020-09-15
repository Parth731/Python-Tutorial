
'''
Type of Errors

- compile time error :  ex: syntax error
- Logical error:    ex: wrong output
- Run Time Error: ex: divide by zero

statement

- normal: will not give any error
- critical
'''


a = 5
b = 2
# print(a/b)
# print("Bye")

'''
here two problem 
1. user will not understand what error means this
2. you can see we are not bye output
'''


try:
    print("resource open")
    print(a/b)
    # print("resource close")
    k = int(input("Enter a Number"))
    print(k)

# except Exception:
except ZeroDivisionError as e:
    print("Hey, you can not divide a Number by zero", e)
    # print("resource close")

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong....")



# finally block will be executed if we get error as well as if we don't get error
finally:
    print("resource closed")


print("Bye")