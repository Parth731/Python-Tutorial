
# fequentaly used

# pickle.load() argument me bytes string object leta hai
# pickle.loads() argument me file object leta hai

import  pickle

# pickling a python object
# write file using pickle
# cars = ["Audi","BWM","Ferarri","Tesala"]
#
# file = "mycar.pkl"
# fileobj = open(file,"wb")
# pickle.dump(cars,fileobj)
# fileobj.close()

# read file using pickle
file = "mycar.pkl"
fileobj = open(file,"rb")
mycar = pickle.load(fileobj)    #load -> read
print(mycar)
print(type(mycar))


