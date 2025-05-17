import pygame
import FridgeHome

class StartGame:
    pygame.init()
    SCREEN_WIDTH = 810
    SCREEN_HEIGHT = 810


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FridgeHome.run(screen)