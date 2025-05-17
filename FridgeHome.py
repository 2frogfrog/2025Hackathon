import Ingredient

def run():
    return 0

class Fridge:
    def __init__(self):
        self.ingredient_list = []

    def addIngredient(self, name, doesExpire, shelfLife, quantity, quantityUnit):
        newIngredient = Ingredient(name,shelfLife,doesExpire,quantity,quantityUnit)
        self.ingredient_list.append(newIngredient)

