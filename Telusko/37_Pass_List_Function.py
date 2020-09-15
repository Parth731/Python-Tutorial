

def count(lst):
    even =0
    odd = 0

    for x in lst:
        if x%2==0:
            even += 1
        else:
            odd += 1

    return even,odd


lst = [20,25,14,19,16,24,28,47,26]

even, odd = count(lst)

print(even,odd)
print("Even : {} and odd : {}".format(even,odd))