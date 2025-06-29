import pygame
class Basket:
    def __init__(self, width, height):
        self.image = pygame.transform.scale(pygame.image.load("assets/basket.png"), (100, 60))
        self.rect = self.image.get_rect()
        (self.
         rect).centerx = width // 2
        self.rect.bottom = height - 10
        self.speed = 4
        self.stopped = False

    def move(self, keys):
        if not self.stopped:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        if keys[pygame.K_SPACE]:
            self.stopped = True
        else:
            self.stopped = False

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 400:
            self.rect.right = 400

    def draw(self, screen):
        screen.blit(self.image, self.rect)
