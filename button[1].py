import pygame
import random


class Button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["button-1.png", "button-2.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.different = True


    def switch_image(self):
        image_number = 0
        if not self.different:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.image_size = self.image.get_size()
        self.different = not self.different



