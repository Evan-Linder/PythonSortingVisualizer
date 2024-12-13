import pygame
import random

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
GRAY = (200,200,200)

font = pygame.font.Font(None, 36)

# Generate random bar heights
barAmt = 30  
bar_heights = [random.randint(20, 350) for _ in range(barAmt)]

# bar input field
input_box = pygame.Rect(WIDTH // 2 - 50, 20, 100, 40) # centered horizontally
input_text = ""
input_active = False

# message box
message = "Bar amount: 30"
message_color = BLACK


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


# function to draw the bar input field
def draw_bar_input(screen, input_box, input_text, font, active):
    pygame.draw.rect(screen, BLACK if active else GRAY, input_box, 2)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

# function to draw the message box
def draw_message_box(screen, message, font, color):
    if message:

        text_surface = font.render(message, True, color)
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()

        message_box = pygame.Rect((WIDTH - text_width) // 2 - 10, 70, text_width + 20, text_height + 10)
        
        pygame.draw.rect(screen, WHITE, message_box)
        pygame.draw.rect(screen, WHITE, message_box, 2)

        screen.blit(text_surface, (message_box.x + 5, message_box.y + 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Check if the user clicked inside input box
            if input_box.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False

        # check for key presses
        elif event.type == pygame.KEYDOWN:
            if input_active:

                # check for submit press (return)
                if event.key == pygame.K_RETURN:
                
                # use a try/catch to ensure input is within range
                    try:

                        num_bars = int(input_text)
                        if 1 <= num_bars <= 30:
                            message = "Bar amount: " + input_text
                            bar_heights = [random.randint(20, 350) for _ in range(num_bars)]

                        else:
                            message = "Input must be between 1 and 30"
                    
                    except ValueError:
                        message = "Invalud input. Enter a integer."
                    input_text = "" 

                # check for backspace
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                
                # add key to input
                else:
                    input_text += event.unicode

    
    screen.fill(WHITE)

    draw_bars(screen, bar_heights, WIDTH, HEIGHT, BLUE)
    draw_bar_input(screen, input_box, input_text, font, input_active)
    draw_message_box(screen, message, font, message_color)
    
    pygame.display.flip()

pygame.quit()


