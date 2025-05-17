class RecipeBook:
    def __init__(self):
        self.recipeList = []
    def add_recipe(self, recipe):
        self.recipeList.append(recipe)
    def available_recipes(self):
        available = []
        unavailable = []
        for recipe in self.recipeList:
            flag = True
            for ingredient in recipe:
                if not ingredient.have_ingredient():
                    flag = False
            if flag:
                available.append(recipe)
            else:
                unavailable.append(recipe)
        return available, unavailable
    def priority_recipe(self):
        self.recipeList = sorted(self.available_recipes()[0])
        self.recipeList.append(sorted(self.available_recipes()[1]))

