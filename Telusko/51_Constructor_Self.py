

class compter:
    def __init__(self):
        self.age = 29
        self.name = "Navin"

    def update(self):
        self.age = 32

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = compter()
print(id(c1))   #address
c1.age = 30
c2 = compter()
print(id(c2))   #address

# c1.name = "rashi"
# c1.age = 12

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

# c1.update()

print(c1.name, c1.age)
print(c2.name, c2.age)