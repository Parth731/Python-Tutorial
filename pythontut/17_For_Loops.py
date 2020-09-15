

list1 = ["Harry", "Larry", "Mari", "carry"]

for item in list1:
    print(item)

list2 = [ ["Harry",1],
             ["Larry", 2],
            ["Mari",3],
            ["carry", 4]]

for item, lollypop in list2:
    print(item," and loolly is ",lollypop)

dic = dict(list2)
print(dic)

for item in dic.items():
    print(item) #item is print

for item in dic:
    print(item) #key value is print





