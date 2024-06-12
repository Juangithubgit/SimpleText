import pygame


def string_to_display(list_):
    s = '|'
    s = s.join(list_)
    return s


def display_lines(surface, text, font, color, location):
    h = font.get_height()
    count = 0
    x1, y1 = location
    multi_text = text.split("|")
    for i, words in enumerate(multi_text):
        num = str(i + 1)
        text_surface = font.render(words, True, color)
        number_of_line = font.render(num, True, (100, 200, 10))
        if count <= 24:
            surface.blit(text_surface, (x1, (y1 + (i*h))))
            surface.blit(number_of_line, (x1 - 30, (y1 + i*h)))
        count += 1


class Menu:

    def __init__(self, x, y, text):
        self.x = x
        self.font = pygame.font.SysFont('Times New Roman', 16)
        self.y = y
        self.image = "menu.png"
        self.image = pygame.image.load(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.text = text

    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    def open(self, screen, event, frame_1, input, guide):
        help_list = []
        help_list_repeat_values = []
        if input == "":
            user_input = [""]
        else:
            user_input = [x for x in input]

        mouse = pygame.mouse.get_pos()
        x, y = mouse

        if event == pygame.MOUSEBUTTONDOWN and x <= 749 and y <= 200:
            frame_1 = False
        if frame_1:
            pygame.draw.rect(screen, "white", (549, 1, 200, 200))
            text = self.font.render(self.text, True, "black", "white")
            text_rect = text.get_rect()
            text_rect.center = (649, 100)
            screen.blit(text, text_rect)

        elif not frame_1:
            for letter in user_input:
                for word in guide:
                    word_split = [t for t in word]
                    if letter in word_split and word not in help_list_repeat_values:
                        help_list.append(word + "--> " + guide[word])
                        help_list_repeat_values.append(word)

            if len(help_list) >= 1:
                help_list = string_to_display(help_list)
            else:
                help_list = "Nothing Found"

            pygame.draw.rect(screen, "white", (549, 1, 200, 600))

            if help_list == "Nothing Found":
                text = self.font.render(help_list, True, "black", "white")
                text_rect = text.get_rect()
                text_rect.center = (649, 100)
                screen.blit(text, text_rect)
            else:
                display_lines(screen, help_list, self.font, "black", (560, 50))
