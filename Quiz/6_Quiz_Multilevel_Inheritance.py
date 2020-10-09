
class Electronics_device:
    power_source = "Alternative current or Direct current"
    use = "Automates works and make the work very faster and efficient"
    start = "it is kind of device which uses"

    def printdetails(self):
        return f"{self.start} {self.power_source} {self.use}".capitalize()

class pocket_gadget(Electronics_device):
    power_source = "Direct current"
    addon_features = "it's portable and look super awesome"

    def printdetails(self):
        return f"{self.start} {self.power_source} {self.use}," \
               f"{self.addon_features}".capitalize()


class Phone(pocket_gadget):
    use = "Its main feature is calling other person's phone to talk"

    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, " \
               f"{self.addon_features}".capitalize()


computer = Electronics_device()
milband = pocket_gadget()
redmi = Phone()

print(computer.printdetails())
print(milband.printdetails())
print(redmi.printdetails())

