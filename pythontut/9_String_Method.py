
#capitalize()
# The capitalize() method returns a string where the first character is upper case.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#casefold()
#The casefold() method returns a string where all the characters are lower case.
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center()
#The center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.center(20)
print(x)

#count()
#The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# encode()
# The encode() method encodes the string, using the specified encoding.
txt = "My name is Ståle"
x = txt.encode()
print(x)

# endwith()
# The endswith() method returns True if the string ends with the specified value, otherwise False.
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# expandtabs()
# The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

# find()
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# formate()
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
#
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# index() same as find()
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# isalnum()
#The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
txt = "Company12"
x = txt.isalnum()
print(x)

# isalpha()
# The isalpha() method returns True if all the characters are alphabet letters (a-z).
txt = "CompanyX"
x = txt.isalpha()
print(x)

# decimal()
# The isdecimal() method returns True if all the characters are decimals (0-9).
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

# isdigit()
# The isdigit() method returns True if all the characters are digits, otherwise False.
txt = "50800"
x = txt.isdigit()
print(x)

# isidentifier()
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
txt = "Demo"
x = txt.isidentifier()
print(x)

# islower()
# The islower() method returns True if all the characters are in lower case, otherwise False.
txt = "hello world!"
x = txt.islower()
print(x)

# isnumeric()
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
txt = "565543"
x = txt.isnumeric()
print(x)

# isprintable()
# The isprintable() method returns True if all the characters are printable, otherwise False.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

# isspace()
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
txt = "   "
x = txt.isspace()
print(x)

# istitle()
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

# isupper()
# The isupper() method returns True if all the characters are in upper case, otherwise False.
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

# join()
# The join() method takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# ljust()
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# lower()
# The lower() method returns a string where all characters are lower case.
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# lstrip()
# The lstrip() method removes any leading characters (space is the default leading character to remove)
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

# maketrans()
# The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
txt = "Hello Sam!";
mytable = txt.maketrans("S", "P");
print(txt.translate(mytable));

# partition()
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
'''
1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
'''

# replace()
# The replace() method replaces a specified phrase with another specified phrase.
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# rfind()
#The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

# rindex()
# The rindex() method finds the last occurrence of the specified value.
# The rindex() method raises an exception if the value is not found.
# The rindex() method is almost the same as the rfind() method. See example below.
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

# rjust()
# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
# Note: In the result, there are actually 14 whitespaces to the left of the word banana.
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

# rpartition()
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

# rsplit()
# The rsplit() method splits a string into a list, starting from the right.
# If no "max" is specified, this method will return the same as the split() method.
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

# rstrip()
# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# split()
# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
txt = "welcome to the jungle"
x = txt.split()
print(x)

# splitlines()
# The splitlines() method splits a string into a list. The splitting is done at line breaks.
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

# startswith()
# The startswith() method returns True if the string starts with the specified value, otherwise False.
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# strip()
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# splitlines()
# The splitlines() method splits a string into a list. The splitting is done at line breaks.
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

# startswith()
# The startswith() method returns True if the string starts with the specified value, otherwise False.
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# strip()
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# swapcase()
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# title()
# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
txt = "Welcome to my world"
x = txt.title()
print(x)

# translate()
# The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# upper()
# The upper() method returns a string where all characters are in upper case.
txt = "Hello my friends"
x = txt.upper()
print(x)

# zfill()
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
txt = "50"
x = txt.zfill(10)
print(x)
