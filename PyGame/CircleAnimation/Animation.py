#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

size = width, height = (300,300)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

def draw(x, y, height, size):
    pygame.draw.circle(screen, (235, 115, 124), (x, y), size)

size = 20
pos_y = 0
running = True
while running:
    events = pygame.event.get()
    if any(event.type == pygame.QUIT for event in events):
        running = False
    
    screen.fill((255, 255, 255))
    current_width, current_height = pygame.display.get_surface().get_size()
    
    pos_x = int(current_width * 0.5)
    max_y = int(current_height *0.5)
    draw(pos_x, pos_y, current_height, size)
    
    if pos_y < max_y:
        pos_y += 2
    else:
        size += 2

    clock.tick(fps)
    pygame.display.flip()
