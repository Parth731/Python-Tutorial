
import random
# import aklearn

random_number = random.randint(0,5)
# print(random_number)
# rand = random.random()
# rand = random.random() * 100
# print(rand)

lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
choice = random.choice(lst)
print(choice)


import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)

import json
lst = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(lst)