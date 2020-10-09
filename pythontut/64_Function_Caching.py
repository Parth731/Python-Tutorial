import  time
from  functools import lru_cache as e

@e(maxsize=4)   # maxsize is howmany value caching
def some_work(n):
    #some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)

    #  some_work(3) call hone ke bad maxsize letset 3(some_work 1,6,9) value ko caching karake memory
    # me store ke rakhega
    some_work(1)
    some_work(6)
    some_work(9)
    print("Done...Calling some again 1")
    # input()
    some_work(3)
    print("called again")

##############################

