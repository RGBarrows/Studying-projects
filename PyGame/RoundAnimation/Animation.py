#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import math

SIZE = width, height = (300,300)
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
FPS = 60

def draw(x, y):
    pygame.draw.circle(SCREEN, (235, 115, 124), (x, y), 20)

new_pos_y = 0
position = 0
running = True
while running:
    events = pygame.event.get()
    if any(event.type == pygame.QUIT for event in events):
        running = False

    SCREEN.fill((255, 255, 255))
    current_width, current_height = pygame.display.get_surface().get_size()
    pos_x = int((25 * math.cos(position)) + current_width * 0.5)
    pos_y = int((25 * math.sin(position)) + new_pos_y)
    
    draw(pos_x, pos_y)
    position += 0.07

    if new_pos_y <= 250:
        new_pos_y += 1
    
    CLOCK.tick(FPS)
    pygame.display.flip()
