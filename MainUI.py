import pygame

import sys

 

# Initialize Pygame

pygame.init()
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
# Font

FONT = pygame.font.Font(None, 36)

# Menu options

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 2", "Option 3", "Option 4"]
selected_option = 0
option_spacing = 50
option_offsets = [0] * len(options)

# Create the screen

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Interactive Menu")

 

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(options)
            elif event.key == pygame.K_RETURN:
                print("Selected:", options[selected_option])
                # Add your code here for what happens when an option is selected

    # Clear the screen
    screen.fill(BLACK)

    # Update option offsets
    for i in range(len(options)):
        target_offset = (i - selected_option) * option_spacing
        option_offsets[i] += (target_offset - option_offsets[i]) * 0.001

 
    # Display options
    for i, option in enumerate(options):
        if i == selected_option:
            text_color = WHITE
        else:
            text_color = GRAY
        text = FONT.render(option, True, text_color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + option_offsets[i]))
        screen.blit(text, text_rect)


    # Update the display
    pygame.display.flip()

 

# Quit Pygame
pygame.quit()
sys.exit()