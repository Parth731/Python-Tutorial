f1 = open("Parth.txt")

try:
    f = open("does2.txt")

# when exception is run, else don't run
# when exception don't not run, else is run
# when try block is fail, except block is run

# except Exception as e:
#     print(e)

except EOFError as e:
    print("Print EOF Error aa gaya hai", e)

except IOError as e:
    print("Print IO Error aa gaya hai", e)

else:
    print("This will run only if except is not running")

# finally statement used cleanup the code
finally:
    print("Run this anyway....")
    f1.close()
    # f.close()

print("important stuff")