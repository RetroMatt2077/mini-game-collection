import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

# -----------------------------
# PADDLE
# -----------------------------
paddle = pygame.Rect(WIDTH//2 - 60, HEIGHT - 40, 120, 15)
paddle_speed = 8

# -----------------------------
# BALL
# -----------------------------
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)
ball_dx = 5
ball_dy = -5

# -----------------------------
# BRICKS
# -----------------------------
brick_rows = 5
brick_cols = 10
brick_w = WIDTH // brick_cols
brick_h = 30

bricks = []

def create_bricks():
    b = []
    for row in range(brick_rows):
        for col in range(brick_cols):
            rect = pygame.Rect(col * brick_w, row * brick_h + 50, brick_w - 2, brick_h - 2)
            b.append(rect)
    return b

bricks = create_bricks()

# -----------------------------
# SCORE
# -----------------------------
score = 0
font = pygame.font.SysFont(None, 36)

def reset():
    global ball, ball_dx, ball_dy, bricks, score
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_dx = 5
    ball_dy = -5
    bricks = create_bricks()
    score = 0

# -----------------------------
# GAME LOOP
# -----------------------------
running = True

while running:
    clock.tick(60)
    screen.fill((10, 10, 20))

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -----------------------------
    # INPUT
    # -----------------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed

    # clamp paddle
    paddle.x = max(0, min(WIDTH - paddle.width, paddle.x))

    # -----------------------------
    # BALL MOVE
    # -----------------------------
    ball.x += ball_dx
    ball.y += ball_dy

    # wall bounce
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1

    if ball.top <= 0:
        ball_dy *= -1

    # bottom = lose/reset
    if ball.bottom >= HEIGHT:
        reset()

    # -----------------------------
    # PADDLE COLLISION
    # -----------------------------
    if ball.colliderect(paddle):
        ball_dy *= -1
        ball.y = paddle.y - ball.height

    # -----------------------------
    # BRICK COLLISION
    # -----------------------------
    hit_index = ball.collidelist(bricks)

    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_dy *= -1
        score += 10

    # -----------------------------
    # WIN CONDITION
    # -----------------------------
    if len(bricks) == 0:
        reset()

    # -----------------------------
    # DRAW BRICKS
    # -----------------------------
    for b in bricks:
        pygame.draw.rect(screen, (0, 200, 255), b)

    # paddle + ball
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    # score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
