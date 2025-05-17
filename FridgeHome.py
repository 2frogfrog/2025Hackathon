import pygame
import sys

import recipe_menu

pygame.init()

# Initialize fullscreen before getting resolution
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Fridge Inventory App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)

# Fonts
font_size = max(int(HEIGHT * 0.025), 12)
font = pygame.font.SysFont(None, font_size)

# Button drawing function
def draw_button(text, rect, color=GRAY):
    pygame.draw.rect(screen, color, rect, border_radius=10)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        label = font.render(line, True, BLACK)
        label_rect = label.get_rect(center=(rect.centerx, rect.centery - (len(lines) - 1) * 10 + i * 20))
        screen.blit(label, label_rect)

# Main loop
def main():
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        # Dynamic dimensions
        left_panel_width = int(WIDTH * 0.25)
        right_panel_width = int(WIDTH * 0.3)
        padding = int(WIDTH * 0.02)

        # Left panel
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, left_panel_width, HEIGHT))

        recipes_button = pygame.Rect(padding, int(HEIGHT * 0.2), left_panel_width - 2 * padding, 40)
        shopping_button = pygame.Rect(padding, int(HEIGHT * 0.3), left_panel_width - 2 * padding, 40)

        draw_button("Recipes", recipes_button)
        draw_button("Shopping\nLists", shopping_button)

        pygame.draw.circle(screen, GRAY, (left_panel_width // 2, int(HEIGHT * 0.5)), 30)
        pygame.draw.polygon(screen, BLACK, [
            (left_panel_width // 2 - 10, int(HEIGHT * 0.5) - 10),
            (left_panel_width // 2 + 10, int(HEIGHT * 0.5)),
            (left_panel_width // 2 - 10, int(HEIGHT * 0.5) + 10)
        ])

        # Ingredient area (centered)
        center_x = WIDTH // 2
        ingredient_radius = 20
        pygame.draw.circle(screen, RED, (center_x - 100, int(HEIGHT * 0.3)), ingredient_radius)
        screen.blit(font.render("5", True, BLACK), (center_x - 80, int(HEIGHT * 0.3) - 10))

        pygame.draw.circle(screen, GREEN, (center_x + 100, int(HEIGHT * 0.3)), ingredient_radius)
        screen.blit(font.render("2", True, BLACK), (center_x + 120, int(HEIGHT * 0.3) - 10))

        pygame.draw.circle(screen, BLUE, (center_x, int(HEIGHT * 0.45)), ingredient_radius)
        screen.blit(font.render("1", True, BLACK), (center_x + 20, int(HEIGHT * 0.45) - 10))

        pygame.draw.circle(screen, BLACK, (center_x, int(HEIGHT * 0.65)), 25, 2)
        pygame.draw.line(screen, BLACK, (center_x - 10, int(HEIGHT * 0.65)), (center_x + 10, int(HEIGHT * 0.65)), 2)
        pygame.draw.line(screen, BLACK, (center_x, int(HEIGHT * 0.65) - 10), (center_x, int(HEIGHT * 0.65) + 10), 2)

        # Right panel
        right_panel_x = WIDTH - right_panel_width
        pygame.draw.rect(screen, LIGHT_GRAY, (right_panel_x, int(HEIGHT * 0.1), right_panel_width, int(HEIGHT * 0.7)))
        screen.blit(font.render("Broccoli:", True, BLACK), (right_panel_x + 10, int(HEIGHT * 0.12)))
        screen.blit(font.render("Quantity: 1", True, BLACK), (right_panel_x + 10, int(HEIGHT * 0.16)))
        screen.blit(font.render("Exp. Date: March 23rd, 2025", True, BLACK), (right_panel_x + 10, int(HEIGHT * 0.2)))
        screen.blit(font.render("3 days left", True, RED), (right_panel_x + 10, int(HEIGHT * 0.24)))
        screen.blit(font.render("Calories per serving: 70", True, BLACK), (right_panel_x + 10, int(HEIGHT * 0.28)))
        screen.blit(font.render("Days till exp: 8 days", True, BLACK), (right_panel_x + 10, int(HEIGHT * 0.32)))

        draw_button("-", pygame.Rect(right_panel_x + 10, int(HEIGHT * 0.4), 60, 40))
        draw_button("+", pygame.Rect(right_panel_x + 90, int(HEIGHT * 0.4), 60, 40))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if recipes_button.collidepoint(event.pos):
                    recipe_menu.run(screen,)
                elif shopping_button.collidepoint(event.pos):
                    print("shopping")

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
