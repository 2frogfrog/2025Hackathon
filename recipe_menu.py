# recipe_menu.py

import pygame

def run(screen):
    # Get screen size
    width, height = screen.get_size()

    # Set font (scale based on height)
    font_size = max(int(height * 0.05), 24)
    font = pygame.font.SysFont(None, font_size)

    # Render "Recipe" text
    text = font.render("Recipe", True, (0, 0, 0))  # Black text
    text_rect = text.get_rect(center=(width // 2, height // 2))

    # Main loop for recipe menu
    running = True
    while running:
        screen.fill((255, 255, 255))  # White background
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        pygame.display.flip()
