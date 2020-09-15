
# threading
from threading import *     # threading
from time import sleep  #sleep()


class Hello(Thread):

    def run(self):
        # for x in range(500): #start
        for x in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        # for x in range(500):  #start
        for x in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

# t1.run()
# t2.run()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()


print("Bye")   # bye print is responsible for main thread

'''
t1.start()
t2.start()
output:

Hello
HiBye

Hello
Hi
Hello
Hi
Hello
Hi
Hello
Hi
'''



