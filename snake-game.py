import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cell = 20

snake = [(100, 100)]
direction = (cell, 0)

food = (random.randrange(0, WIDTH, cell), random.randrange(0, HEIGHT, cell))

def new_food():
    return (random.randrange(0, WIDTH, cell), random.randrange(0, HEIGHT, cell))

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -cell)
            if event.key == pygame.K_DOWN:
                direction = (0, cell)
            if event.key == pygame.K_LEFT:
                direction = (-cell, 0)
            if event.key == pygame.K_RIGHT:
                direction = (cell, 0)

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if new_head == food:
        food = new_food()
    else:
        snake.pop()

    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        running = False

    pygame.draw.rect(screen, (255, 0, 0), (*food, cell, cell))

    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, cell, cell))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
