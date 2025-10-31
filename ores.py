import random

class Ore:
    def __init__(self,type,amount):
        self.amount = amount
        self.type = type 

class Azurite(Ore):
    def __init__(self):
        super().__init__("azurite",random.randint(0,100))# seperate them for different animations maybe or different purposes.