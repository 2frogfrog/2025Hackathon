from operator import truediv
from datetime import date


class Ingredient:
    def __init__(self,name,shelfLife,doesExpire,quantity,quantityUnit):
        self.doesExpire = doesExpire
        self.name = name
        self.shelfLife = shelfLife
        self.quantity = quantity
        self.quantityUnit = quantityUnit
        self.expiring = False
        self.dateAdded = date.today()
    def have_ingredient(self, fridge):
        for item in fridge.ingredient_list:
            if self.name == item.name and self.quantity <= item.quantity:
                return True
        return False
    def update_ingredient(self):
        self.shelfLife -= (date.today() - self.dateAdded).days
        if self.shelfLife <= 3:
            self.expiring = True
    def __lt__(self, other):
        return self.shelfLife < other.shelfLife