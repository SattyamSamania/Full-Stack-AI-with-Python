class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....") 

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")                   