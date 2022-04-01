import pygame
from pygame.locals import *
running = True
root = pygame.display.set_mode((0, 0, pygame.FULLSCREEN))
clock = pygame.time.Clock()
fps = 60
while running:
    pygame.display.update()
    root.fill((0, 255, 0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False