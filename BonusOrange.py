import pygame
import random
from Orange import Orange

class BonusOrange(Orange):
    def __init__(self, screen_width):
        super().__init__(screen_width)
        self.apple_type = 'bonus_orange'
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
