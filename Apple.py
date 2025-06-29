import pygame
import random

class Apple:
    def __init__(self, screen_width,apple_type="normal"):
        self.image = pygame.transform.scale(pygame.image.load("assets/apple.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.apple_type = apple_type
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, self.screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def fall(self):
        self.rect.y += 4

    def draw(self, screen):
        screen.blit(self.image, self.rect)
