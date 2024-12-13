import pygame
import random

# function to render the bars
def draw_bars(screen, bar_heights, screen_width, screen_height, color):
    bar_width = 20  
    spacing = 10  # Spacing between bars

    for i, bar_height in enumerate(bar_heights):

        # Calculate x and y for each bar
        x = (screen_width - (len(bar_heights) * (bar_width + spacing))) // 2 + i * (bar_width + spacing)
        y = screen_height - bar_height  

        # Draw the bar
        pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))




