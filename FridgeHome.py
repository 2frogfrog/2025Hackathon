import pygame
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fridge Inventory App")

# Colors
WHITE = (255, 255, 256)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)

# Fonts
font = pygame.font.SysFont(None, 24)


# Button drawing function
def draw_button(text, rect, color=GRAY):
    pygame.draw.rect(screen, color, rect, border_radius=10)
    label = font.render(text, True, BLACK)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


# Main loop
def main():
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        # Left panel
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, 200, HEIGHT))
        draw_button("Recipes", pygame.Rect(30, 100, 140, 40))
        draw_button("Shopping\nLists", pygame.Rect(30, 160, 140, 40))
        pygame.draw.circle(screen, GRAY, (100, 250), 30)
        pygame.draw.polygon(screen, BLACK, [(90, 240), (110, 250), (90, 260)])

        # Center ingredient area
        pygame.draw.circle(screen, RED, (300, 150), 20)
        screen.blit(font.render("5", True, BLACK), (320, 140))

        pygame.draw.circle(screen, GREEN, (400, 150), 20)
        screen.blit(font.render("2", True, BLACK), (420, 140))

        pygame.draw.circle(screen, BLUE, (350, 250), 20)
        screen.blit(font.render("1", True, BLACK), (370, 240))

        pygame.draw.circle(screen, BLACK, (350, 350), 25, 2)
        pygame.draw.line(screen, BLACK, (340, 350), (360, 350), 2)
        pygame.draw.line(screen, BLACK, (350, 340), (350, 360), 2)

        # Right panel - item details
        pygame.draw.rect(screen, LIGHT_GRAY, (550, 50, 230, 400))
        screen.blit(font.render("Broccoli:", True, BLACK), (560, 60))
        screen.blit(font.render("Quantity: 1", True, BLACK), (560, 90))
        screen.blit(font.render("Exp. Date: March 23rd, 2025", True, BLACK), (560, 120))
        screen.blit(font.render("3 days left", True, RED), (560, 140))
        screen.blit(font.render("Calories per serving: 70", True, BLACK), (560, 170))
        screen.blit(font.render("Days till exp: 8 days", True, BLACK), (560, 200))

        draw_button("-", pygame.Rect(560, 250, 40, 40))
        draw_button("+", pygame.Rect(620, 250, 40, 40))

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)


main()
