import Ingredient

def run():
    return 0

class Fridge:
    ingredient_list = []
    def addIngredient(self, name, doesExpire, shelfLife, quantity, quantityUnit):
        new_ingredient = Ingredient(name,shelfLife,doesExpire,quantity,quantityUnit)
        self.ingredient_list.append(new_ingredient)
        self.ingredient_list = sorted(self.ingredient_list)
    def update(self):
        for item in self.ingredient_list:
            item.update()