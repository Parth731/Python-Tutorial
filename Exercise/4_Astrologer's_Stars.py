
# pattern printing
'''
input = integer n
Boolean =  true/false

True n=5
*
**
***
****

false n=5
****
***
**
*
'''

n = int(input("How many rows want to print\n"))
b = bool(int(input("Please enter True or False")))
print(b)
if b == True:
    for x in range(n):
        for y in range(x+1):
            print("*",end="")
        print()
elif b == False:
    for x in range(n, 0, -1):
        for y in range(x):
            print("*", end="")
        print()

