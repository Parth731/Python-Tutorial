
# raise
# search buit in expection

# a = input("What is your name?")
# b = int(input("how much do you earn"))
#
# if b==0:
#     raise ZeroDivisionError("b is 0 stopping the program")
#
# if a.isnumeric():
#     raise Exception("Number are not allowed")
#
# print(f"hello {a}")


# for exmaple: 1000 lines running taking 1 hour
# i want to saving 1 hours
# input sahi nai hai to 1000 line me run karake me kya karuga
# vo 1000 line me run nai karana chahata

c = input("Enter your name")
try:
    print(a)

except Exception as e:
    if c=="harry":
        raise valueError("Harry is blocked he is not allowed")
    print("Exception handled")
