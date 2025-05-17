# recipe_menu.py

import pygame

import add_Recipe
from Recipe import Recipe  # Make sure this path is correct

def run(screen, recipe_book):
    width, height = screen.get_size()
    font_size = max(int(height * 0.03), 20)
    font = pygame.font.SysFont(None, font_size)

    # Define the + (add) button
    plus_button = pygame.Rect(width - 70, 20, 50, 50)

    running = True
    while running:
        screen.fill((255, 255, 255))  # White background

        # Draw title
        title = font.render("Recipes", True, (0, 0, 0))
        screen.blit(title, (30, 20))

        # Draw + button
        pygame.draw.rect(screen, (200, 200, 200), plus_button, border_radius=10)
        plus = font.render("+", True, (0, 0, 0))
        screen.blit(plus, plus.get_rect(center=plus_button.center))

        # Draw each recipe name
        for i, recipe in enumerate(recipe_book.recipeList):
            y = 100 + i * 50
            name_text = getattr(recipe, "name", f"Recipe {i+1}")
            label = font.render(name_text, True, (0, 0, 0))
            screen.blit(label, (40, y))

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if plus_button.collidepoint(event.pos):
                    # Create and add a dummy recipe with a name
                    add_Recipe.run(screen, recipe_book)

        pygame.display.flip()
