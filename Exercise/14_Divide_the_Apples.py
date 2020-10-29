
'''
Problem Statement:-
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisor of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5

2 is a divisor of20

3 is not a divisor of 20

…

5 is a divisor of 20

'''

apple = int(input("Enter the n number of apple\n"))
mn = int(input("Enter the starting range\n"))
mx = int(input("Enter the end of range\n"))

for x in range(mn,mx):
    if apple%x == 0:
        print(f"{x} is divisor of {apple}")
    else:
        print(f"{x} is not divisor of {apple}")
