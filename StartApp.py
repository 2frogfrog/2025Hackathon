import pygame
import FridgeHome
from Fridge import Fridge
from RecipeBook import RecipeBook
from ShoppingList import ShoppingList


class StartGame:
    pygame.init()
    fridge = Fridge()
    recipeBook = RecipeBook()
    shoppingList = ShoppingList()
    FridgeHome.run(recipeBook)