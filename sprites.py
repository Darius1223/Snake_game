"""
Спрайты
"""
import pygame.draw
import random

import settings
from settings import *


class Apple:
    def __init__(self):
        self.x = random.randrange(0, WIDTH, SEGMENT_SIZE)
        self.y = random.randrange(0, HEIGHT, SEGMENT_SIZE)
        self.size = SEGMENT_SIZE
        self.color = APPLE_COLOR

    def draw(self, display):
        pygame.draw.rect(
            display,
            self.color,
            (self.x, self.y, self.size, self.size)
        )

    def respawn(self):
        self.x = random.randrange(0, WIDTH, SEGMENT_SIZE)
        self.y = random.randrange(0, HEIGHT, SEGMENT_SIZE)


class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        # head
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.color = GREEN_COLOR
        self.size = SEGMENT_SIZE

        self.dx = 1
        self.dy = 0

        self.body = []

    def draw(self, display):
        pygame.draw.rect(
            display,
            self.color,
            (self.x, self.y, self.size, self.size)
        )
        for segment in self.body:
            pygame.draw.rect(
                display,
                self.color,
                (segment.x, segment.y, self.size, self.size)
            )

        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('Hello Привет', True,
                          (180, 0, 0))

    def movement(self, apple):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.dy != 1:
            self.dx = 0
            self.dy = -1
        if keys[pygame.K_DOWN] and self.dy != -1:
            self.dx = 0
            self.dy = 1
        if keys[pygame.K_LEFT] and self.dx != 1:
            self.dx = -1
            self.dy = 0
        if keys[pygame.K_RIGHT] and self.dx != -1:
            self.dx = 1
            self.dy = 0

        if self.body:
            for index in range(len(self.body[1:])):
                self.body[len(self.body) - index - 1].x = self.body[len(self.body) - index - 2].x
                self.body[len(self.body) - index - 1].y = self.body[len(self.body) - index - 2].y

            self.body[0].x = self.x
            self.body[0].y = self.y

        if self.x == apple.x and self.y == apple.y:
            apple.respawn()
            new_segment = Segment(self.x, self.y)
            self.body.append(new_segment)

        self.x += self.dx * self.size
        self.y += self.dy * self.size

        if self.body:
            for segment in self.body:
                if self.x == segment.x and self.y == segment.y:
                    self.x = WIDTH // 2
                    self.y = WIDTH // 2
                    self.body = []
