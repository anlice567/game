import pygame
from Banana import Banana
import random

class PoisonedBanana(Banana):
    def __init__(self, screen_width):
        super().__init__(screen_width)
        self.apple_type = 'poisonedbanana'
        self.image = pygame.transform.scale(pygame.image.load("assets/poisonedbanana.png"), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def fall(self):
        self.rect.y += 6

    def draw(self, screen):
        screen.blit(self.image, self.rect)
