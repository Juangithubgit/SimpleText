import pygame


class Menu:

    def __init__(self, x, y, choice,  screen):
        self.x = x
        self.font = pygame.font.SysFont('Times New Roman', 30)
        self.y = y
        self.image = "menu.png"
        self.image = pygame.image.load(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.choice = choice

    def open(self, screen):
        pygame.draw.rect(screen, "white", (549, 1, 200, 200))
        text = self.font.render(self.choice, True, "black", "white")
        text_rect = text.get_rect()
        text_rect.center = ((649), 100)
        screen.blit(text, text_rect)

    def change_to_help_box(self, input, guide, screen):
        pygame.draw.rect(screen, "white", (549, 1, 200, 200))
        for thing in guide:
                key = guide.get(thing)
                data[i] = data[i].replace(thing, key)


