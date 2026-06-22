import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_x = 100
bird_y = HEIGHT // 2
velocity = 0
gravity = 0.5

PIPE_W = 60
PIPE_GAP = 160
PIPE_SPEED = 3

pipes = []

def spawn_pipe():
    h = random.randint(120, 380)
    x = WIDTH + 100
    return [
        pygame.Rect(x, 0, PIPE_W, h),
        pygame.Rect(x, h + PIPE_GAP, PIPE_W, HEIGHT)
    ]

pipes.append(spawn_pipe())

def reset():
    global bird_y, velocity, pipes
    bird_y = HEIGHT // 2
    velocity = 0
    pipes = [spawn_pipe()]

running = True

while running:
    clock.tick(60)
    screen.fill((30, 30, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = -8

    # bird physics
    velocity += gravity
    bird_y += velocity
    bird = pygame.Rect(bird_x, int(bird_y), 30, 30)

    # move pipes
    updated = []

    for top, bottom in pipes:
        top.x -= PIPE_SPEED
        bottom.x -= PIPE_SPEED

        if top.right > -50:
            updated.append([top, bottom])

    pipes = updated

    # SAFE spawn (no pipes[-1] access)
    if len(pipes) == 0 or pipes[-1][0].x < WIDTH - 250:
        pipes.append(spawn_pipe())

    # collision
    for top, bottom in pipes:
        if bird.colliderect(top) or bird.colliderect(bottom):
            reset()
            break

    # bounds
    if bird.top < 0 or bird.bottom > HEIGHT:
        reset()

    # draw
    for top, bottom in pipes:
        pygame.draw.rect(screen, (0, 255, 0), top)
        pygame.draw.rect(screen, (0, 255, 0), bottom)

    pygame.draw.rect(screen, (255, 255, 0), bird)

    pygame.display.flip()

pygame.quit()
