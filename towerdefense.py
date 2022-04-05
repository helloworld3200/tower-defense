import pygame
from pygame.locals import *
running = True
root = pygame.display.set_mode((0, 0, pygame.FULLSCREEN))
clock = pygame.time.Clock()
fps = 60
while running:
    pygame.display.update()
    root.fill((0, 255, 0))
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(root, (169, 169, 169), 0, root.get_size()[1], 3000, 200)
    
pygame.quit()
pygame.display.quit()