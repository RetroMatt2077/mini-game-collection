import pygame

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

count = 0
font = pygame.font.SysFont(None, 48)

button = pygame.Rect(100, 100, 200, 100)

running = True

while running:
    screen.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                count += 1

    pygame.draw.rect(screen, (0, 200, 255), button)

    text = font.render(str(count), True, (255, 255, 255))
    screen.blit(text, (170, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
