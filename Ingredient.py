from operator import truediv

from FridgeHome import Fridge


class Ingredient:
    def __init__(self,name,shelfLife,doesExpire,quantity,quantityUnit):
        self.doesExpire = doesExpire
        self.name = name
        self.shelfLife = shelfLife
        self.quantity = quantity
        self.quantityUnit = quantityUnit
    def have_ingredient(self):
        for item in Fridge.ingredient_list:
            if self.name == item.name and self.quantity <= item.quantity:
                return True
        return False
