import pygame

class Menu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, 36)
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.display_menu()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.game.screen.get_width() // 2 - 80 <= mouse_x <= self.game.screen.get_width() // 2 + 80 and self.game.screen.get_height() // 2 + 20 <= mouse_y <= self.game.screen.get_height() // 2 + 60:
                    self.game.reset()
                    self.running = False

    def display_menu(self):
        self.game.screen.fill((255, 255, 255))
        title = self.font.render("       Ферма", True, (0, 0, 0))
        self.game.screen.blit(title, (self.game.screen.get_width() // 2 - 100, self.game.screen.get_height() // 2 - 50))

        start_button = self.font.render("Начать игру", True, (0, 0, 255))
        self.game.screen.blit(start_button, (self.game.screen.get_width() // 2 - 80, self.game.screen.get_height() // 2 + 20))

        pygame.display.flip()
