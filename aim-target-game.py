import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer Debug")

clock = pygame.time.Clock()

# -----------------------------
# TARGET (START CENTERED)
# -----------------------------
radius = 40
target_x = WIDTH // 2
target_y = HEIGHT // 2

score = 0
font = pygame.font.SysFont(None, 50)

running = True

while running:
    clock.tick(60)

    # VERY CLEAR BACKGROUND
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            dx = mx - target_x
            dy = my - target_y

            if dx*dx + dy*dy <= radius*radius:
                score += 1
                # move slightly, NOT random (for debugging)
                target_x += 80
                if target_x > WIDTH:
                    target_x = 100

    # -----------------------------
    # DRAW TARGET (FORCED VISIBLE)
    # -----------------------------
    pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), radius)

    # crosshair so you KNOW it's rendering
    pygame.draw.line(screen, (0, 255, 0), (0, target_y), (WIDTH, target_y), 2)
    pygame.draw.line(screen, (0, 255, 0), (target_x, 0), (target_x, HEIGHT), 2)

    # SCORE
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
