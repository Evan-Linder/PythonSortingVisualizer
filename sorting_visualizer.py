import pygame
from bar_renderer import *

pygame.init()

WIDTH, HEIGHT = 1000,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
RED = (220, 20, 60)
GREEN = (0, 255, 0)

# Generate random bar heights
barAmt = 30  
bar_heights = [random.randint(20, 350) for _ in range(barAmt)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_bars(screen, bar_heights, WIDTH, HEIGHT, BLUE)
    pygame.display.flip()

pygame.quit()


