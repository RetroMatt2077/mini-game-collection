import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 🔥 FIX: get real width from display surface (avoids mismatch bugs)
WIDTH, HEIGHT = screen.get_size()

PADDLE_W = 15
PADDLE_H = 100

# FIXED POSITIONS (GUARANTEED ON SCREEN)
left_x = 20
right_x = WIDTH - 35

left = pygame.Rect(left_x, HEIGHT//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)
right = pygame.Rect(right_x, HEIGHT//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)

ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)
ball_dx, ball_dy = 4, 3

def clamp_paddle(p):
    if p.top < 0:
        p.top = 0
    if p.bottom > HEIGHT:
        p.bottom = HEIGHT

running = True

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # LEFT PADDLE
    if keys[pygame.K_w]:
        left.y -= 6
    if keys[pygame.K_s]:
        left.y += 6

    # RIGHT PADDLE
    if keys[pygame.K_UP]:
        right.y -= 6
    if keys[pygame.K_DOWN]:
        right.y += 6

    clamp_paddle(left)
    clamp_paddle(right)

    # BALL
    ball.x += ball_dx
    ball.y += ball_dy

    # WALLS
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # COLLISION
    if ball.colliderect(left) or ball.colliderect(right):
        ball_dx *= -1

    # RESET
    if ball.left < 0 or ball.right > WIDTH:
        ball.center = (WIDTH//2, HEIGHT//2)

    # DRAW (FORCED VISIBILITY)
    pygame.draw.rect(screen, (255,255,255), left)
    pygame.draw.rect(screen, (255,255,255), right)
    pygame.draw.rect(screen, (255,255,255), ball)

    pygame.display.flip()

pygame.quit()
