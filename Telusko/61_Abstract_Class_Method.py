
'''
what is Abstract class and why need it ?

python doesn't supported bia default abstract class

'''

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        # print("Running")
        pass

    '''
       this method is called declaration not definition
        is called as Abstract method

        this declaration of Abstraction method is called as Abstract classes
    '''

class Laptop(Computer):

    def process(self):
        print("It's Running")




class Programmer:
    def work(self,com):
        print("solving Bugs")
        com.process()


#
# com = Computer()
# com.process()
com1 = Laptop()
com1.process()
pro1 = Programmer()
pro1.work(com1)




