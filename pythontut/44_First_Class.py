
class Student:
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1

larry.std = 9
larry.subject = ["hindi", "physics"]

print(harry.name)
print(harry.std)
print(harry.section, larry.std, larry.subject)
