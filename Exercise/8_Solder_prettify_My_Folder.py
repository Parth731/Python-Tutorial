
import os

def solder(path,file,format):

    os.chdir(path) # path converted directory

    x = 1

    files = os.listdir(path)
    print("files: ", files)
    print("file :",file)

    with open(file) as fop:
        filelist = fop.read().split("\n")
        print(filelist)

    # folder capitalize
    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{x}{format}")
            x += 1


'''
# solder(r"C:\Users\ADMIN\Desktop\testing",
#        r"E:\code with harry python\pythontut\ext.txt",
#        ".png")
'''

# if __name__ == '__main__':

pathn = input('Enter Path Name:')
filen = input('Enter File Name Which Contain Name Of Files Not TO Alter: ')
ext = input('Enter Extension/Formate: ')
solder(pathn, filen, ext)





