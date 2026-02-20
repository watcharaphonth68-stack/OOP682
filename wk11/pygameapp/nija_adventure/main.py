import sys, os
import pygame

from shars.sara import Hero

class ninjaA(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.caption = "Ninja Adventure"
        self.hero = Hero('hero', "ninja/Attack_000.png", 50 , 50)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.running = True
        pygame.display.set_caption(self.caption)
    def handle_close(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
    def draw_text(self, text, position, color=(0, 0, 0)):
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, position)
    def start(self):
        start = pygame.time.get_ticks()
        elapsed_time = 0
        while self.running:
            elapsed_time = pygame.time.get_ticks() - start
            self.handle_close()
            self.screen.fill((255, 255, 255))
            self.draw_text("Welcome to Ninja Adventure!", (400, 300))
            self.hero.update(elapsed_time)
            self.hero.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            start = pygame.time.get_ticks()
        pygame.quit()
    
if __name__ == "__main__":
    game = ninjaA()
    game.start()