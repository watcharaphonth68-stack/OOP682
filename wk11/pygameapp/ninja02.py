import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Pygame 02 - FPS")
running = True
clock = pygame.time.Clock()
ninja = pygame.image.load("ninja/Attack__000.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    screen.fill((255,255,255))
    font = pygame.font.SysFont("Arial", 36)
    text = font.render( f'{clock.get_fps():.0f}', True , (0,0,0))
    screen.blit(text, (300,230))
    screen.blit(ninja, (0,0))
    pygame.display.update()

pygame.quit()