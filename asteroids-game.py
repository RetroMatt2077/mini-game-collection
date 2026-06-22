import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids Clean Mobile Controls")

clock = pygame.time.Clock()

# -----------------------------
# SHIP
# -----------------------------
ship_x = WIDTH // 2
ship_y = HEIGHT // 2
angle = 0
dx = 0
dy = 0

# -----------------------------
# GAME OBJECTS
# -----------------------------
asteroids = []
bullets = []

def spawn_asteroid():
    return [
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.uniform(-2, 2),
        random.uniform(-2, 2),
        40
    ]

for _ in range(5):
    asteroids.append(spawn_asteroid())

# -----------------------------
# INPUT STATE
# -----------------------------
move_active = False
rotate_active = False

move_x, move_y = 0, 0
rot_y = 0

fire_btn = pygame.Rect(WIDTH - 120, HEIGHT - 120, 100, 100)

fire_cooldown = 0
FIRE_RATE = 12

# -----------------------------
# WRAP
# -----------------------------
def wrap(x, y):
    return x % WIDTH, y % HEIGHT

# -----------------------------
# LOOP
# -----------------------------
running = True

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    fire_pressed = False

    # -----------------------------
    # EVENTS
    # -----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if fire_btn.collidepoint(mx, my):
                fire_pressed = True
            else:
                if mx < WIDTH // 2:
                    move_active = True
                else:
                    rotate_active = True

        if event.type == pygame.MOUSEBUTTONUP:
            move_active = False
            rotate_active = False

    mx, my = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    # -----------------------------
    # LEFT JOYSTICK = MOVEMENT
    # -----------------------------
    if move_active and mx < WIDTH // 2:
        move_x = mx - WIDTH // 4
        move_y = my - HEIGHT // 2

        if math.hypot(move_x, move_y) > 10:
            rad = math.atan2(move_y, move_x)

            dx += math.cos(rad) * 0.15
            dy += math.sin(rad) * 0.15

    # -----------------------------
    # RIGHT JOYSTICK = ROTATION
    # -----------------------------
    if rotate_active and mx > WIDTH // 2:
        rot_y = my - HEIGHT // 2
        angle += rot_y * 0.05  # smooth controlled rotation

    # -----------------------------
    # KEYBOARD FALLBACK
    # -----------------------------
    if keys[pygame.K_LEFT]:
        angle -= 4
    if keys[pygame.K_RIGHT]:
        angle += 4
    if keys[pygame.K_UP]:
        rad = math.radians(angle)
        dx += math.cos(rad) * 0.15
        dy += math.sin(rad) * 0.15

    # -----------------------------
    # FIRE SYSTEM
    # -----------------------------
    if fire_cooldown > 0:
        fire_cooldown -= 1

    if fire_pressed and fire_cooldown == 0:
        rad = math.radians(angle)

        bx = ship_x + math.cos(rad) * 20
        by = ship_y + math.sin(rad) * 20

        bullets.append([
            bx,
            by,
            math.cos(rad) * 8,
            math.sin(rad) * 8
        ])

        fire_cooldown = FIRE_RATE

    # -----------------------------
    # SHIP PHYSICS
    # -----------------------------
    ship_x += dx
    ship_y += dy
    ship_x, ship_y = wrap(ship_x, ship_y)

    dx *= 0.99
    dy *= 0.99

    # -----------------------------
    # BULLETS
    # -----------------------------
    new_bullets = []
    for b in bullets:
        b[0] += b[2]
        b[1] += b[3]

        if 0 <= b[0] <= WIDTH and 0 <= b[1] <= HEIGHT:
            new_bullets.append(b)

    bullets = new_bullets

    # -----------------------------
    # ASTEROIDS
    # -----------------------------
    new_asteroids = []

    for a in asteroids:
        a[0] += a[2]
        a[1] += a[3]
        a[0], a[1] = wrap(a[0], a[1])

        hit = False
        for b in bullets:
            if abs(a[0] - b[0]) < a[4] and abs(a[1] - b[1]) < a[4]:
                hit = True
                break

        if not hit:
            new_asteroids.append(a)

    asteroids = new_asteroids

    # -----------------------------
    # DRAW SHIP
    # -----------------------------
    shape = [(0, -12), (-8, 10), (8, 10)]
    pts = []

    for x, y in shape:
        r = math.radians(angle)
        rx = x * math.cos(r) - y * math.sin(r)
        ry = x * math.sin(r) + y * math.cos(r)
        pts.append((ship_x + rx, ship_y + ry))

    pygame.draw.polygon(screen, (255, 255, 255), pts)

    # -----------------------------
    # DRAW ASTEROIDS
    # -----------------------------
    for a in asteroids:
        pygame.draw.circle(screen, (150, 150, 150), (int(a[0]), int(a[1])), a[4])

    # -----------------------------
    # DRAW BULLETS
    # -----------------------------
    for b in bullets:
        pygame.draw.circle(screen, (255, 255, 0), (int(b[0]), int(b[1])), 3)

    # -----------------------------
    # FIRE BUTTON
    # -----------------------------
    pygame.draw.rect(screen, (255, 0, 0), fire_btn)
    font = pygame.font.SysFont(None, 30)
    txt = font.render("FIRE", True, (255, 255, 255))
    screen.blit(txt, (fire_btn.x + 20, fire_btn.y + 35))

    pygame.display.flip()

pygame.quit()
