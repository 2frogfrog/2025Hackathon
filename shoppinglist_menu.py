import pygame

def run(screen):
    pygame.display.set_caption("Shopping List")
    font = pygame.font.SysFont(None, 24)

    WHITE, BLACK, GRAY, LIGHT_GRAY = (255, 255, 255), (0, 0, 0), (200, 200, 200), (230, 230, 230)
    clock = pygame.time.Clock()

    name_input_rect = pygame.Rect(50, 20, 150, 30)
    amount_input_rect = pygame.Rect(220, 20, 80, 30)
    add_button_rect = pygame.Rect(320, 20, 30, 30)

    active_input = None
    name_text, amount_text = "", ""
    items = []

    class Item:
        def __init__(self, name, needed):
            self.name = name
            self.needed = needed
            self.current = 0
            self.checked = False

        def rects(self, index):
            y = 70 + index * 50
            return {
                "checkbox": pygame.Rect(10, y, 20, 20),
                "minus": pygame.Rect(270, y, 30, 30),
                "plus": pygame.Rect(310, y, 30, 30),
                "delete": pygame.Rect(360, y, 30, 30)
            }

    def draw_ui():
        screen.fill(WHITE)

        # Add button
        pygame.draw.rect(screen, LIGHT_GRAY, add_button_rect)
        screen.blit(font.render("+", True, BLACK), (add_button_rect.x + 8, add_button_rect.y + 5))

        # Text inputs
        for rect, user_text, placeholder, active in [
            (name_input_rect, name_text, "Name", active_input == "name"),
            (amount_input_rect, amount_text, "Amount", active_input == "amount")
        ]:
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
            color = BLACK if user_text else GRAY
            text = user_text if user_text else placeholder
            screen.blit(font.render(text, True, color), (rect.x + 5, rect.y + 5))

        # Items
        for i, item in enumerate(items):
            y = 70 + i * 50
            rect = item.rects(i)

            pygame.draw.rect(screen, WHITE, rect["checkbox"])
            pygame.draw.rect(screen, BLACK, rect["checkbox"], 2)
            if item.checked:
                pygame.draw.line(screen, BLACK, (rect["checkbox"].x, rect["checkbox"].y),
                                 (rect["checkbox"].x + 20, rect["checkbox"].y + 20), 2)
                pygame.draw.line(screen, BLACK, (rect["checkbox"].x + 20, rect["checkbox"].y),
                                 (rect["checkbox"].x, rect["checkbox"].y + 20), 2)

            screen.blit(font.render(item.name, True, BLACK), (40, y))
            amt_text = f"{item.current}/{item.needed} needed"
            screen.blit(font.render(amt_text, True, BLACK), (150, y))

            for b in ["minus", "plus", "delete"]:
                pygame.draw.rect(screen, LIGHT_GRAY, rect[b])
                symbol = "-" if b == "minus" else "+" if b == "plus" else "X"
                text = font.render(symbol, True, BLACK)
                screen.blit(text, text.get_rect(center=rect[b].center))

    running = True
    while running:
        draw_ui()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if name_input_rect.collidepoint(event.pos):
                    active_input = "name"
                elif amount_input_rect.collidepoint(event.pos):
                    active_input = "amount"
                elif add_button_rect.collidepoint(event.pos):
                    if name_text.strip() and amount_text.isdigit():
                        items.append(Item(name_text.strip(), int(amount_text)))
                        name_text, amount_text = "", ""
                        active_input = None
                else:
                    active_input = None
                    for i, item in enumerate(items):
                        rect = item.rects(i)
                        if rect["checkbox"].collidepoint(event.pos):
                            item.checked = not item.checked
                        elif rect["plus"].collidepoint(event.pos):
                            if item.current < item.needed:
                                item.current += 1
                        elif rect["minus"].collidepoint(event.pos):
                            if item.current > 0:
                                item.current -= 1
                        elif rect["delete"].collidepoint(event.pos):
                            items.pop(i)
                            break

            elif event.type == pygame.KEYDOWN and active_input:
                if event.key == pygame.K_BACKSPACE:
                    if active_input == "name":
                        name_text = name_text[:-1]
                    elif active_input == "amount":
                        amount_text = amount_text[:-1]
                else:
                    char = event.unicode
                    if active_input == "name":
                        name_text += char
                    elif active_input == "amount" and char.isdigit():
                        amount_text += char

        clock.tick(60)
