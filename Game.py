import pygame
import random
from Basket import Basket
from Apple import Apple
from PoisonedApple import PoisonedApple
from BonusApple import BonusApple
from Menu import Menu
from Banana import Banana
from Orange import Orange
from PoisonedOrange import PoisonedOrange
from PoisonedBanana import PoisonedBanana
from BonusBanana import BonusBanana
from BonusOrange import BonusOrange

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((400, 400))
        self.background = pygame.transform.scale(pygame.image.load("assets/farm.jpg"), (400, 400))
        self.basket = Basket(200, 390)
        self.apples = []
        self.previous_time = pygame.time.get_ticks()
        self.fruit_spawn_time = 2000
        self.font = pygame.font.SysFont(None, 36)
        self.running = True
        self.score = 0
        self.level = 1
        self.level_up_score = 10
        self.lives = 3

    def reset(self):
        self.basket = Basket(200, 390)
        self.apples = []
        self.previous_time = pygame.time.get_ticks()
        self.score = 0
        self.running = True
        self.lives = 3

    def increase_difficulty(self):
        if self.score >= self.level_up_score * self.level:
            self.level += 1
            self.fruit_spawn_time -= 400
            self.level_up_score = self.level_up_score * 2

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.basket.move(keys)
            self.screen.blit(self.background, (0, 0))
            self.basket.draw(self.screen)

            current_time = pygame.time.get_ticks()

            if current_time - self.previous_time > self.fruit_spawn_time:

                if self.level >= 3:
                    apple_type = random.choice(
                        ['normal', 'bonus', 'poisoned', 'banana', 'orange', 'bonus_banana', 'bonus_orange',
                         'poisoned_banana', 'poisoned_orange'])
                elif self.level >= 2:
                    apple_type = random.choice(
                        ['normal', 'bonus', 'poisoned', 'banana', 'bonus_banana', 'bonus_orange', 'poisoned_banana',
                         'poisoned_orange'])
                else:
                    apple_type = random.choice(['normal', 'bonus', 'poisoned', 'banana'])

                if apple_type == 'poisoned':
                    self.apples.append(PoisonedApple(400))
                elif apple_type == 'bonus':
                    self.apples.append(BonusApple(400))
                elif apple_type == 'banana':
                    self.apples.append(Banana(400))
                elif apple_type == 'orange':
                    self.apples.append(Orange(400))
                elif apple_type == 'bonus_banana':
                    self.apples.append(BonusBanana(400))
                elif apple_type == 'bonus_orange':
                    self.apples.append(BonusOrange(400))
                elif apple_type == 'poisoned_banana':
                    self.apples.append(PoisonedBanana(400))
                elif apple_type == 'poisoned_orange':
                    self.apples.append(PoisonedOrange(400))
                else:
                    self.apples.append(Apple(400))


                self.previous_time = current_time


            for apple in self.apples[:]:
                apple.fall()

                if apple.rect.colliderect(self.basket.rect):
                    if apple.apple_type == 'normal':
                        self.score += 1
                    elif apple.apple_type == 'bonus':
                        self.score += 5
                    elif apple.apple_type == 'poisoned':
                        self.lives -= 1
                    elif apple.apple_type == 'banana':
                        self.score += 2
                    elif apple.apple_type == 'orange':
                        self.score += 3
                    elif apple.apple_type == 'bonus_banana':
                        self.score += 4
                    elif apple.apple_type == 'bonus_orange':
                        self.score += 6
                    elif apple.apple_type == 'poisoned_banana':
                        self.lives -= 1
                    elif apple.apple_type == 'poisoned_orange':
                        self.lives -= 1
                    self.apples.remove(apple)
                    continue

                if apple.rect.top > 400:
                    self.apples.remove(apple)
                    if apple.apple_type == "normal" or apple.apple_type == "banana" or apple.apple_type == "orange":
                        self.lives -= 1

                apple.draw(self.screen)

            self.increase_difficulty()

            score_text = self.font.render(f"Счет: {self.score}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            level_text = self.font.render(f"Уровень: {self.level}", True, (0, 0, 0))
            self.screen.blit(level_text, (10, 40))

            lives_text = self.font.render(f"Жизни: {self.lives}", True, (255, 0, 0))
            self.screen.blit(lives_text, (300, 10))

            if self.lives <= 0:
                self.running = False

            pygame.display.flip()

        game_over_text = self.font.render("Игра окончена", True, (255, 0, 0))
        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - 80, self.screen.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    game = Game()
    menu = Menu(game)

    menu.run()

    if game.running:
        game.run()

    pygame.quit()
