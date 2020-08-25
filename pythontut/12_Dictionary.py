
# Dictionary is nothing but key value pairs
dl = {}
print(type(dl))
d2 = {"harry" : "Burgar", "Rohan":"Fiish", "parth" : "Bhindi" ,
        "shubham": {"B" : "maggie", "L" :"roti", "D":"chicken"}}
d2["Ankit"]="Junk Food"
d2[420] = "Kabab"
print(d2["harry"])
print(d2["parth"])
print(d2["shubham"]["B"])
print(d2)
del d2[420]
print(d2)

#copy the dictionary
#deep copy
# d3 = d2.copy()
# print(d3)
# del d3["harry"]
# print(d3)
# print(d2)

#shallow copy
# d3 = d2
# print(d3)
# del d3["harry"]
# print(d3)
# print(d2)

#get()
print(d2.get("harry"))
d2.update({"Leena":"Trofee"})
print(d2)
print(d2.keys())
print(d2.items())
print(d2.values())









