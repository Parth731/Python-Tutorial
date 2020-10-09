
# break and continue satement use in one loop

while (True):
    print("Enter Integer number")
    num = int(input())
    if num < 100:
        print("Print try again\n")
        continue
    else:
        print("congrautlation you input is 100\n")
        break
