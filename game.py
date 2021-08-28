import pygame
from settings import *
from sprites import Apple, Snake

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# sprite
apple = Apple()
snake = Snake()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    display.fill((BLACK_COLOR))

    # сетка
    for i in range(SEGMENTS_COUNT):
        for j in range(SEGMENTS_COUNT):
            pygame.draw.rect(
                display,
                GRAY_COLOR,
                (i * SEGMENT_SIZE, j * SEGMENT_SIZE, SEGMENT_SIZE, SEGMENT_SIZE),
                1
            )
    # apple
    apple.draw(display)
    # snake
    snake.draw(display)
    snake.movement(apple)

    clock.tick(FPS)
    pygame.display.flip()
