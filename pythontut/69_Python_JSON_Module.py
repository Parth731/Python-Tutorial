
'''

JSON: Javascript object nation
https://www.w3schools.com/python/python_json.asp

free api

https://httpbin.org
https://financialmodelingprep.com/developer/docs/

more information for json.load() and json.load()
https://pynative.com/python-json-load-and-loads-to-parse-json/

different between json.load() and json.loads()

1. json.load() ->  method (without “s” in “load”) used to read JSON
encoded data from a file and convert it
into Python dictionary.

2. json.loads() -> method, which is used for parse valid JSON
String into Python
 dictionary.

json.loads()--------->  It is used to convert a json string to an dictonary
json.dump()---------> It is used to convert a dictonary to an json string.
josn.load()----------> It is used to read a file which contains an json object

what is key parameter in dumps?
Python me json object hamesa unordered hota hai isliye hum usme
sort_keys parameter=True pass
karte hai jisse ki json object me keys ordered collection me sort ho sake!

'''




import  json


# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using
# the json.loads() method.
# Convert from JSON to Python:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print(x)
# print(x["age"])     # error: string indices must be integers

# string converted json
parsed  = json.loads(x)
print(parsed)
print(parsed["age"])
print(type(parsed))

#################################

print("------------------ json load------------------------")
print("Started Reading JSON file")
with open("developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decoded JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")


#######################

print("----------------------------json loads() ------------------")

developerJsonString = """{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""

print("Started converting JSON string document to Python dictionary")
developerDict = json.loads(developerJsonString)

print("Printing key and value")
print(developerDict["name"])
print(developerDict["salary"])
print(developerDict["skills"])
print(developerDict["email"])
print(developerDict["projects"])

print("Done converting JSON string document to a dictionary")

print("-----------------------json dump()------------------")
# Convert from Python to JSON
data2 = {
    "channel_name" : "codewithharry",
    "cars" : ["bmw","audi A8", "ferrari"],
    "fridge" : ("roti",540),
    "isbad" : False
}

'''
python me True , False first letter capital hota hai
javascript me true,false first letter small hota hai
'''

jscomp = json.dumps(data2)
print(jscomp)
# print(jscomp["fridge"]) #java script convert


# If you have a Python object, you can convert it into a
# JSON string by using the json.dumps() method.

# Convert from Python to JSON:

# what is key parameter in dumps?
# Python me json object hamesa unordered hota hai isliye hum usme
# sort_keys parameter=True pass
# karte hai jisse ki json object me keys ordered collection me sort ho sake!
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}



y = json.dumps(x,sort_keys=True)
print(y)

