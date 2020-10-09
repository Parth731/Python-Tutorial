
class dad:
    basketball = 6

class son(dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class grandson(son):
    dance = 6
    gultar = 1

    # def isdance(self):
    #     return f"Jackson Yeah!" \
    #            f"Yes I dance very awesomely {self.dance} no of times"

derry = dad()
larry = son()
harry = grandson()

print(harry.isdance())
print(harry.basketball)
print(harry.gultar)

'''
electronics device
pocket gadget
phone

'''


