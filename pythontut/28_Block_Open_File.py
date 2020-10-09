with open("Parth2.txt") as fop:
    a = fop.read(4)
    print(a)

fop.close()
# Question of the day -> with open ke bad me fir se file open
# karake read karuga to read hogi ya nahi



fop = open("Parth2.txt","rt")
print(fop.readlines())
# print(fop.readline())


fop.close()