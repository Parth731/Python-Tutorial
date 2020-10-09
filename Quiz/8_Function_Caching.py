import time
from functools import lru_cache

num = int(input("Please enter the max size for lru_cache:"))

@lru_cache(maxsize=num)
def some_thing(n):
    time.sleep(n)
    return n

if __name__ == '__main__':

    print("called")
    some_thing(5)
    some_thing(3)
    some_thing(9)
    some_thing(3)
    print("called again")
    some_thing(10)
    print("Calling some thing..")
