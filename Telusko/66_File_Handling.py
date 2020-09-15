

fop = open('mytextfile.txt','r')

# print(fop)
# print(fop.read()) #read everything
# print(fop.readlines())

# read the line
# print(fop.readline(),end="")
# print(fop.readline())

# read the  four char
# print(fop.readline(4),end="")
fop.close()

fop1 = open('abc','w')
# first check abc file is available or not but not available create the file.
fop1.write("something ")
fop1.write("Laptop ")
fop1.close()

# open file in append mode
fop1 = open("abc","a")
fop1.write("mobile ")
fop1.close()

# how to copy one the data to other file
fop = open("mytextfile.txt","r")
fop1 = open("abc","w")

for data in fop:
    # print(data)
    fop1.write(data)

fop.close()
fop1.close()

# copy image one file to other
fop = open("DSC_8670.JPG","rb") # read binary
fop1 = open("mypic.JPG","wb")   # write binary

for x in fop:
    # print(x)
    fop1.write(x)

fop.close()
fop1.close()
