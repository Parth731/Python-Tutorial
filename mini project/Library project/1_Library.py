''''
create a library class

    1. diplay book
    2. addbook
    3. leadbook -> (who own the book if not present)
    4. returnbook

    harrylibrary(list of books, library_name)

    dictionary  key-> books-nameofperson

create main function and run an infinite while loop asking user for their
input


'''

class Library:

    def __init__(self,llist_of_book,library_name):
        self.lead_data = {}
        self.list_of_book = llist_of_book
        self.library_name = library_name

        for books in self.list_of_book:
            self.lead_data[books] = None
            # print(self.lead_data[books])

    def Display_Book(self):

        # for num,books in enumerate(self.list_of_book):
        #     print(f"{num} : {books}")

        for key,name in self.lead_data.items():
            print(f"{key}: {name}")


    def Lead_Book(self,book,reader):

        if book in self.list_of_book:
            if self.lead_data[book] is None:
                self.lead_data[book] = reader
                print("\nBook Lead\n")
            else:
                print(f"sorry this book lead by {self.lead_data[book]}")
        else:
                print("You have written wrong  name")
    print()

    def return_Book(self,book,reader):
        if book in self.list_of_book:
            print(f"{str(self.lead_data[book])} -> {book}")
            if self.lead_data[book] == reader:
                self.lead_data[book] = None
                print(f"\n{book} book return successful\n")
            else:
                print("sorry this book is not Lead")
        else:
            print("You have written wrong  name")
        print()


    def add_Book(self,book_name):
        self.list_of_book.append(book_name)
        self.lead_data[book_name] = None
        print(f"\n {book_name} Add book successful\n")
        print()

    def delete_Book(self,book_name):
        self.lead_data.pop(book_name)
        self.list_of_book.remove(book_name)
        print(f"\n {book_name} delete book successful\n")
        print()






def main():
    List_of_Books = ['Cookbook','Sherlock Holmes','Chacha_chaudhary','Rich Dad and Poor Dad']
    library_name = "P.K library"
    secret_Key = 123456

    Parth = Library(List_of_Books,library_name)

    print(
        f"Welcome To {Parth.library_name} library\n\nExit Using 'Q' \nDisplay Book Using 'D' \nadd lend book using 'L' \nReturn a Book using 'R' \n"
        f"Add Book Using 'A' \nDelete Book using 'DEL' \n")

    Exit = False


    while Exit is not True:
        print()
        print(
            f"Exit Using 'Q' \nDisplay Book Using 'D' \nadd lend book using 'L' \nReturn a Book using 'R' \n"
            f"Add Book Using 'A' \nDelete Book using 'DEL' \n")

        _input = input("Option: ").lower()
        print("\n")

        if _input == 'Q'.lower():
            Exit = True

        elif _input == 'D'.lower():
            Parth.Display_Book()

        elif _input == 'L'.lower():
            _input2 = input("What is Your name: ")
            print(str(Parth.list_of_book) + "\n")
            _input3 = input("Which Book Do you want to lend: ")
            Parth.Lead_Book(_input3,_input2)

        elif _input == "DEL".lower():
            _input_secret =int(input("Write a secret Key to delete: "))
            if _input_secret == secret_Key:
                print(str(Parth.list_of_book) + "\n")
                _input2 = input("which Book you want to delete: ")
                Parth.delete_Book(_input2)
            else:
                print("Sorry We can't Delete the Book: ")

        elif _input == "R".lower():
            _input2 = input("What is  your name: ")
            print(str(Parth.list_of_book) + "\n")
            _input3 = input("which book you want to return: ")
            Parth.return_Book(_input3,_input2)

        elif _input == "A".lower():
            _input2 = input("Book name:")
            Parth.add_Book(_input2)





if __name__ == '__main__':
    main()