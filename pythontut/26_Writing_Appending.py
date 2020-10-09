'''

'''


# f1 = open("Parth2.txt","w")
# a = f1.write("parthbhai  bahut achhe hain\n")
# print(a) #28
# f1.close()

# f1 = open("Parth2.txt","a")
# a = f1.write("parthbhai  bahut achhe hain\n")
# print(a) //28
# f1.close()


# Handle read and write both
# f1 = open("harry2","r+") #error
f1 = open("Parth2.txt","r+")
print(f1.read())
f1.write("Thank you")
f1.close()

