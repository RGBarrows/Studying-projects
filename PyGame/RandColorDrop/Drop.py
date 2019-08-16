#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random

SIZE = width, height = 300, 600
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
FPS = 60

def drop_element(x, y):
    SCREEN.fill(
        pygame.Color(
            random.randint(0, 255), random.randint(0, 255),
            random.randint(0, 255)
            ),
        pygame.Rect(x, y, 10, 10)
    )

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_pos = event.pos[0]
            y_pos = event.pos[1]

            drop_element(x_pos, y_pos)
    
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
