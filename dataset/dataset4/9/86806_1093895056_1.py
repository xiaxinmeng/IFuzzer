
import pygame
pygame.init()
pygame.display.set_mode((100, 100))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            print(event, event.key.__class__, event.key, key_name)
        elif event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            print(event, event.key.__class__, event.key, key_name)
