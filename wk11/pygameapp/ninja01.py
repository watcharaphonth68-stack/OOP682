import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Pygame 02 - FPS")
running = True
clock = pygame.time.Clock()
ninja_a000 = pygame.image.load("ninja/Attack__000.png")
ninja_a_pos = pygame.Rect(0, 0, 128, 128)  # Define a rectangle for the source area of the second image
ninja_a002 = pygame.Rect(50, 50, 128, 128)  # Define a rectangle for the source area of the third image

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         ninja_a_pos.x += 5  # Move to the next frame in the sprite sheet
        #     elif event.key == pygame.K_LEFT:
        #         ninja_a_pos.x -= 5  # Move to the previous frame in the sprite sheet
        #     elif event.key == pygame.K_UP:
        #         ninja_a_pos.y -= 5  # Move up in the sprite sheet
        #     elif event.key == pygame.K_DOWN:
        #         ninja_a_pos.y += 5  # Move down in the sprite sheet
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and ninja_a_pos.x + ninja_a_pos.width < 1280:  # Check if the right arrow key is pressed and if we haven't reached the end of the sprite sheet
        ninja_a_pos.x += 5  # Move to the next frame in the sprite sheet
    if key[pygame.K_LEFT] and ninja_a_pos.x > 0:  # Check if the left arrow key is pressed and if we haven't reached the beginning of the sprite sheet
        ninja_a_pos.x -= 5  # Move to the previous frame in the sprite sheet
    if key[pygame.K_UP] and ninja_a_pos.y > 0:  # Check if the up arrow key is pressed and if we haven't reached the top of the sprite sheet
        ninja_a_pos.y -= 5  # Move up in the sprite sheet
    if key[pygame.K_DOWN] and ninja_a_pos.y + ninja_a_pos.height < 720:  # Check if the down arrow key is pressed and if we haven't reached the bottom of the sprite sheet
        ninja_a_pos.y += 5  # Move down in the sprite sheet
    clock.tick(60)
    screen.fill((255,255,255))
    font = pygame.font.SysFont("Arial", 36)
    text = font.render( f'{clock.get_fps():.0f}', True , (0,0,0))
    screen.blit(text, (300,230))
    screen.blit(ninja_a000, ninja_a_pos, ninja_a002)  # Blit the specified area of the sprite sheet onto the screen
    pygame.display.update()

pygame.quit()