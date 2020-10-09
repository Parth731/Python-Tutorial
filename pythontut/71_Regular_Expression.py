



import  re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
indian mobile: +91 9883443344
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map
Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# findall, search, split, sub, finditer

'''
findall:	Returns a list containing all matches
search:	The search() function searches the string for a match, and returns a Match object if there is a match.
split:	Returns a list where the string has been split at each match
sub:	Replaces one or many matches with a string
'''

# findall
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# search
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
x = re.search("Portugal", txt)
print(x)


# split
x = re.split("\s",txt)
print(x)
x = re.split("\s",txt,1)
print(x)

# sub()
x = re.sub("\s","9",txt)
print(x)
x = re.sub("\s","9",txt,2)
print(x)


# row string
# print(r"\n")
# finditer
# patt = re.compile(r"fass")
# patt = re.compile(r".adm")
# patt = re.compile(r"^Tata")
# patt = re.compile(r"$Tata")   #not return
# patt = re.compile(r"iin$")
# patt = re.compile(r"ai*")
# patt = re.compile(r"ai+")
# patt = re.compile(r"ai{2}")
# patt = re.compile(r"(ai){2}")
# patt = re.compile(r"(ai){1}")
# patt = re.compile(r"ai{1}|t")
# patt = re.compile(r"ai{1}|Fax")

# special sequence
# patt = re.compile(r"\ATata")
# patt = re.compile(r"\AFax")   # no return
# patt = re.compile(r"\bTata")
# patt = re.compile(r"Fax\b")
# patt = re.compile(r"27\b")
# patt = re.compile(r"\d{5}-\d{4}")
patt = re.compile(r"^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$")



matches = patt.finditer(mystr)

for match in matches:
  print(match)
  # print(mystr)



