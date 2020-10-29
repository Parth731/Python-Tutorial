
# koi ak function ko aadha chalaya ak bar aor jab chaye tab bich me
# se chale


def searcher():
    import time
    # some 4 second time consuming task

    book = "This is a book an harry and code with harry and good"

    time.sleep(4)   # resume book, machine learning file read

    while True:
        text = (yield)

        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
print("Search started")
next(search)
search.send("harry")

print("Next method run")
input("Press any key")
search.send("harry and")
input("Press any key")
search.send("Parth code")
input("Press any key")
search.send("This is")

search.close()
print("Search closing")

input("Press any key")
search.send("good bou")




