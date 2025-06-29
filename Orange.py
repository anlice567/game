import pygame
import random
from Apple import Apple

class Orange(Apple):
    def __init__(self, screen_width):
        super().__init__(screen_width)
        self.apple_type = 'orange'
        self.image = pygame.transform.scale(pygame.image.load("assets/orange.png"), (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def fall(self):
        self.rect.y += 4

    def draw(self, screen):
        screen.blit(self.image, self.rect)
