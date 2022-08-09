import pygame, sys

pygame.init()

display_width = 480
display_height = 320
fps = 30

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/bg_image.png')
bg_surface = pygame.transform.scale(bg_surface, (480, 320))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0,0))

    pygame.display.update()
    clock.tick(fps)