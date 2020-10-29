'''

Problem Statement:-
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swapping the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user

[5, 4, 1]

Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!

'''



print("Enter the number of list one by one\n")
size = int(input("Enter size of list\n"))
lst = []

for x in range(size):
    lst.append(int(input("Enter the element\n")))


print(f"your list is {lst}")

# lst = [97,13,22,56,18]

reverse1 = lst.copy()
reverse1.reverse()
print(f"my list reversed list of {lst} is {reverse1}")
reverse2 = lst[::-1]
print(f"my list reversed list of {lst} is {reverse2}")

reverse3 = lst[::]
print(reverse3)
for x in range(len(reverse3)//2):
    # a,b = b,a
    reverse3[x],reverse3[len(reverse3)-x-1] = reverse3[len(reverse3)-x-1],reverse3[x]
    print(f"my list reversed list at x={x} is {reverse3}")

print(reverse3)

print(f"my third reverse list of {lst} is {reverse3}")


if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three method gives same result")

