import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Time Test")

font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 40)

# -----------------------------
# GAME STATE
# -----------------------------
WAITING = 0
READY = 1
RESULT = 2

state = WAITING

start_time = 0
reaction_time = 0

# random delay timer
change_time = time.time() + random.uniform(2, 5)

# -----------------------------
# MAIN LOOP
# -----------------------------
running = True

while running:
    screen.fill((255, 0, 0))  # default RED = wait

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # TOO EARLY CLICK
            if state == WAITING:
                state = RESULT
                reaction_time = -1

            # VALID CLICK
            elif state == READY:
                reaction_time = int((time.time() - start_time) * 1000)
                state = RESULT

            # RESTART
            elif state == RESULT:
                state = WAITING
                change_time = time.time() + random.uniform(2, 5)

    # -----------------------------
    # STATE LOGIC
    # -----------------------------

    # WAITING STATE (red screen)
    if state == WAITING:
        if time.time() >= change_time:
            state = READY
            start_time = time.time()

    # READY STATE (green screen)
    if state == READY:
        screen.fill((0, 255, 0))

    # -----------------------------
    # DRAW TEXT
    # -----------------------------
    if state == WAITING:
        text = font.render("WAIT...", True, (255, 255, 255))
        screen.blit(text, (300, 250))

    elif state == READY:
        text = font.render("TAP NOW!", True, (0, 0, 0))
        screen.blit(text, (280, 250))

    elif state == RESULT:
        screen.fill((0, 0, 0))

        if reaction_time == -1:
            text = font.render("TOO SOON!", True, (255, 0, 0))
        else:
            text = font.render(f"{reaction_time} ms", True, (0, 255, 0))

        screen.blit(text, (250, 250))

        sub = small_font.render("Tap to retry", True, (200, 200, 200))
        screen.blit(sub, (290, 330))

    pygame.display.flip()

pygame.quit()
