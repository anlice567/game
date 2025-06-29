import pygame
from Apple import Apple
import random

class BonusApple(Apple):
    def __init__(self, screen_width):
        super().__init__(screen_width)
        self.apple_type = 'bonus'
        self.image = pygame.transform.scale(pygame.image.load("assets/bonusapple.png"), (60, 60))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
