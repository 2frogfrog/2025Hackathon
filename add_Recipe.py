# add_recipe.py

import pygame
from Recipe import Recipe
from Ingredient import Ingredient

pygame.init()

class TextInput:
    def __init__(self, rect, font, prompt=""):
        self.rect = pygame.Rect(rect)
        self.color = (255, 255, 255)
        self.border_color = (0, 0, 0)
        self.text = ""
        self.font = font
        self.active = False
        self.prompt = prompt

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, 2)
        txt_surface = self.font.render(f"{self.prompt}{self.text}", True, (0, 0, 0))
        screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))

    def get_value(self):
        return self.text


def run(screen, recipe_book):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    # Input fields with larger sizes
    name_input = TextInput((100, 100, 800, 60), font, "Name: ")  # Larger width and height
    ingredients_input = TextInput((100, 180, 800, 60), font, "Ingredients (name:shelfLife:doesExpire:qty:unit): ")  # Larger width and height
    steps_input = TextInput((100, 260, 800, 100), font, "Steps: ")  # Larger width and height

    inputs = [name_input, ingredients_input, steps_input]

    # Submit button
    submit_button = pygame.Rect(100, 400, 200, 60)  # Larger button

    running = True
    while running:
        screen.fill((240, 240, 240))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            for input_box in inputs:
                input_box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN and submit_button.collidepoint(event.pos):
                name = name_input.get_value().strip()
                ingredients_text = ingredients_input.get_value()
                steps = steps_input.get_value().strip()

                ingredient_objs = []
                for raw in ingredients_text.split(","):
                    try:
                        n, sl, de, q, qu = raw.strip().split(":")
                        ingredient = Ingredient(n.strip(), int(sl), de.strip() == "True", float(q), qu.strip())
                        ingredient_objs.append(ingredient)
                    except ValueError:
                        print(f"Error parsing ingredient: {raw}")

                if name and ingredient_objs:
                    new_recipe = Recipe(name)
                    new_recipe.add_ingredient(ingredient_objs)
                    recipe_book.add_recipe(new_recipe)
                    print(f"✅ Added recipe: {name}")
                    running = False
                else:
                    print("⚠️ Missing name or valid ingredients.")

        # Draw input boxes
        for input_box in inputs:
            input_box.draw(screen)

        # Draw submit button
        pygame.draw.rect(screen, (180, 180, 180), submit_button)
        submit_text = font.render("Submit", True, (0, 0, 0))
        screen.blit(submit_text, submit_text.get_rect(center=submit_button.center))

        pygame.display.flip()
        clock.tick(60)
