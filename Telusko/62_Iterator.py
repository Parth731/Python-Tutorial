

nums = [7,8,9,5]

# iterated will not give all value. it will give one value at time.
it = iter(nums)

# print(it.__next__())
# print(it.__next__())
# print(next(it))
#
# for x in nums:
#     print(x)

##########################

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self): # give you object to iterator
        return self

    def __next__(self): # give next object or value
        if self.num <= 10:
            val = self.num  # val = 1
            self.num += 1   # self.num = 2
            return  val     #return 1
        else:
            raise StopIteration


values = TopTen()

# print(values.__next__())
# print(values.__next__())
print(next(values))
for x in values:
    print(x)

