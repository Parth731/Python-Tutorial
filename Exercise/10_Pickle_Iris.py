
import requests
import pickle


data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

# l1 = data.split("\n")
# print(l1)

l2 = [item.split(",") for item in data.split("\n") if len(item)!=0]
print(l2)

# string
# l3 = [[item] for item in data.split("\n") if len(item)!=0]
# print(l3)

# to write this pickle from file
with open("myIris.pkl","wb") as fop:
    pickle.dump(l2,fop)
    fop.close()

# to read this pickle from file
with open("myIris.pkl","rb") as fop:
    data = pickle.load(fop)
    print()
    print("data: ",data)


