

'''

You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]


'''
def next_palindrome(num):
    '''here first check palindrome or not then
    printing next palindrome number'''
    num += 1
    while not is_palindrome(num):
        num += 1
    return num

def is_palindrome(num):
    ''' if that have palindrome, return 1 and
    if not palindrome, return 0 '''
    return str(num) == str(num)[::-1]

if __name__ == '__main__':

    size = int(input("Enter the size of your list\n"))
    lst = []

    for x in range(size):
        lst.append(int(input("Enter the number\n")))


    print(f"you have entered {lst}")

    print(f"output list: {[lst[x] if lst[x] < 10 else next_palindrome(lst[x]) for x in range(size)]}")

    # new_lst = []
    # for x in lst:
    #     if x > 10:
    #         num = next_palindrome(x)
    #         new_lst.append(num)
    #     else:
    #         new_lst.append(x)
    # print(f"output list: {new_lst}")