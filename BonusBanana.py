import pygame
import random
from Banana import Banana

class BonusBanana(Banana):
    def __init__(self, screen_width):
        super().__init__(screen_width)
        self.apple_type = 'bonus_banana'
        self.image = pygame.transform.scale(pygame.image.load("assets/bonusbanana.png"), (60, 60))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
