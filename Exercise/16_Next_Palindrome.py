
'''

Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222

'''

def next_palindrome(num):
    num += 1
    while  not is_palindrome(num):
        print("print")
        num += 1 # palindrome nai hai to num 1 increment ho jayega
    return num


def is_palindrome(num):
    return str(num) == str(num)[::-1]    # check palindrom or not


if __name__ == '__main__':
    size = int(input("Enter the number of test cases\n"))
    lst = []

    for x in range(size):
        lst.append(int(input("Enter the number:\n")))

    print(lst)

    for x in range(size):
        print(f"Next palindrome for {lst[x]} is {next_palindrome(lst[x])}")