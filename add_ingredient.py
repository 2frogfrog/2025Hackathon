# add_ingredient.py

import pygame

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
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_value(self):
        return self.text


def run(screen, on_submit):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    name_input = TextInput((100, 100, 600, 50), font, "Ingredient Name: ")
    quantity_input = TextInput((100, 180, 600, 50), font, "Quantity: ")

    inputs = [name_input, quantity_input]

    submit_button = pygame.Rect(100, 260, 150, 50)

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
                quantity = quantity_input.get_value().strip()

                if name and quantity:
                    print(f"✅ Ingredient added: {name} ({quantity})")
                    on_submit(name, quantity)  # Call the callback
                    running = False
                else:
                    print("⚠️ Please fill in both fields.")

        for input_box in inputs:
            input_box.draw(screen)

        pygame.draw.rect(screen, (180, 180, 180), submit_button)
        submit_text = font.render("Submit", True, (0, 0, 0))
        screen.blit(submit_text, submit_text.get_rect(center=submit_button.center))

        pygame.display.flip()
        clock.tick(60)
