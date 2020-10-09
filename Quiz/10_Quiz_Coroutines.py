import time

def search_file():

    fop = open("data.txt")
    time.sleep(4)

    while True:

        text = (yield)


        if text in fop.read():
            print("Your name is in this file")
        else:
            print("Your name is not in this file")

    fop.close()


name =input("What is your name?").lower()
search = search_file()
print("file is searching....")
next(search)
search.send(name)
search.close()





