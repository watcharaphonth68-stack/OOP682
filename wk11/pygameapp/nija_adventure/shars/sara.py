import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    def __init__(self, name ,filename, rows= 2, cols = 3 , width = 64, height = 64):
        super().__init__()
        self.name = name
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.row = self.col = 0
        self.rect = pygame.Rect(0, 0, width, height)
    
    def update(self, elapsed_time= 100):
        if elapsed_time > 300:
            self.col = (self.col + 1) % 3
            if self.col == 0:
                self.row = (self.row + 1) % 2
    
    def draw(self, surface):
        frame = self.sheet.subsurface(self.col * self.rect.width, self.row * self.rect.height, self.rect.width, self.rect.height)
        surface.blit(frame, self.rect)