class ShoppingList:
    def __init__(self):
        self.ingredientList = []
    def add_list(self, ingredients):
        for item in ingredients:
            self.ingredientList.append(item)
    def remove_item(self, item):
        self.ingredientList.remove(item)