from ShoppingList import ShoppingList


class Recipe:
    ingredientList = []
    missing = []
    def add_ingredient(self, ingredients):
        for item in ingredients:
            self.ingredientList.append(item)
    def can_make(self):
        for item in self.ingredientList:
            if not item.have_ingredient():
                    self.missing.append(item)
        if len(self.missing) == 0:
            return True
        else:
            return False, self.missing
    def add_list(self):
        ShoppingList.add_List(self.missing)
    def get_priority(self):
        priority = 0
        for item in self.ingredientList:
            if item.expiring:
                priority += 1
        return priority

    def __lt__(self, other):
        return self.get_priority() < other.get_priority()

