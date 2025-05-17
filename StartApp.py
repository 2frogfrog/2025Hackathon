import pygame
import sqlite3
import FridgeHome

class StartGame:
    pygame.init()
    SCREEN_WIDTH = 810
    SCREEN_HEIGHT = 810
    con = sqlite3.connect('food.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ingredients(name UNIQUE, expiration, calories)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS recipes(name UNIQUE, ingredients)")
    con.commit()
    con.close()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FridgeHome.run(screen)