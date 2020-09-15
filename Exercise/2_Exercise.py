#Exercise 2 - Faulty Calculator
# 45*3 = 555, 56+9 = 77 , 56/6 = 4
# Design a caluclator which will correctly solve all the problems except
# the following ones:
# Your program should take operator and the two numbers as input from the user and then return the result


print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")
op =  input("choose the option +, -, *, /")

print("Enter the number 1")
a = int(input())
print("Enter the number 2")
b = int(input())

if op == '+':
    if a == 56 and b == 9:
        print("77")
    else:
        print(a+b)
elif op == '-':
    if a == 55 and b == 10:
        print("60")
    else:
        print(a - b)
elif op == '*':
    if a == 45 and b == 3:
        print("555")
    else:
        print(a * b)
elif op == '/':
    if a == 56 and b == 6:
        print("4")
    else:
        print(a / b)
else:
    print("Error ! please check your input")

