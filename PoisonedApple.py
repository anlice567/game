import pygame
import random
from Apple import Apple

class PoisonedApple(Apple):
    def __init__(self, screen_width):
        super().__init__(screen_width, 'poisoned')
        self.image = pygame.transform.scale(pygame.image.load("assets/poisonapple.png"), (40, 40))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def fall(self):
        self.rect.y += 6

    def draw(self, screen):
        screen.blit(self.image, self.rect)
