

num  = int(input("Howmany number do you want to add in list: \n"))

com  = input("which Comprehensions do you want to use: \n"
                 "L for List Comprehensions \nS for set Comprehensions \n"
                 "D for Dictionary Comprehensions \n"
                 "G for generator Comprehensions \n")
lst = []
if com == "L":
    lst = [x for x in range(num)]
    print(lst)
elif com == "S":
    se = {x for x in range(num)}
    print(se)
elif com == "D":
    dic = {x: f"item{x}" for x in range(num)}
    print(dic)
elif com == "G":
    gen = (x for x in range(num))
    print(gen.__next__())
    print(gen.__next__())
