class ShoppingList:
    ingredientList = []
    def add_List(self, ingredients):
        for item in ingredients:
            self.ingredientList.append(item)
    def remove_item(self, item):
        self.ingredientList.remove(item)