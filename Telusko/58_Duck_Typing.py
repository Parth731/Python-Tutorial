
# Duck typing

'''
duck test
 - if it look like a duck, swims like a duck, and quacks like a duck, then
 it probably is duck
'''

class PyCharm:
    def execute(self):
        print("compling")
        print("Running")

class myeditior:
    def execute(self):
        print("spell check")
        print("Convention check")
        print("compling")
        print("Running")

class laptop:
    def code(self,ide):
        ide.execute()

# ide = PyCharm()
# lap1 = laptop()
# lap1.code(ide)

ide1 =  PyCharm()
ide2 = myeditior()
lap1= laptop()
lap1.code(ide1)
lap1.code(ide2)
