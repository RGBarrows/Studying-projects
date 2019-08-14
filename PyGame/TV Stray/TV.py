import pygame
import random

size = width, height = (300,300)
screen = pygame.display.set_mode(size)

def draw():
    for i in range(20000):
        screen.fill(pygame.Color("black"), (random.random() * width,
                                            random.random() * height,
                                            1, 1))

running = True
while running:
    screen.fill((255, 255, 255))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    draw()

    pygame.display.flip()

pygame.quit()
