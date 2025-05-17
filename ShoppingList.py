# shopping_list.py

class ShoppingList:
    __instance = None

    @staticmethod
    def get_instance():
        return ShoppingList.__instance

    @staticmethod
    def delete_instance():
        ShoppingList.__instance = None

    def __init__(self):
        if ShoppingList.__instance is not None:
            raise Exception("ShoppingList already exists!")
        else:
            self.items = []
    def add_ingredient(self, ingredient):
        """Add an ingredient object to the shopping list if its name is not already present."""
        if not any(item.name == ingredient.name for item in self.items):
            self.items.append(ingredient)
        else:
            print(f"Ingredient '{ingredient.name}' already in the shopping list.")

    def delete_ingredient(self, ingredient):
        """Delete an ingredient object from the shopping list by matching its name."""
        for item in self.items:
            if item.name == ingredient.name:
                self.items.remove(item)
                break
        else:
            print(f"Ingredient '{ingredient.name}' not found in the shopping list.")

    def __str__(self):
        return "Shopping List: [" + ", ".join(item.name for item in self.items) + "]"
