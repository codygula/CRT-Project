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

mainMenu = ["Space Rock", "Lofi", "Playlists", "Podcasts", "Settings", "Option 6", "Option 7"]
settingsMenu = ["CRT Timeout", "Settings 2", "Settings 3", "Settings 4", "Back"]
CRTTimeout = ["5", "10", "30", "60", "Back"]
back = [""]

options = mainMenu
selected_option = 0
option_spacing = 50
option_offsets = [0] * len(options)


# Status Display


# Create the screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Interactive Menu")

# options: "mainMenu", "Back"
menu_state = "mainMenu"
prev_state = []

def changeSetting(setting, value):
    print("changeSetting() Called")


# Main loop
running = True
while running:
    # print("prev_state = " + prev_state)

    if menu_state == "mainMenu":
        options = mainMenu
    elif menu_state == "settings":
        options = settingsMenu
    elif menu_state == "back":
        options = prev_state
    elif menu_state == "CRT Timeout":
        options = CRTTimeout

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
                if options[selected_option] == "Settings":
                    menu_state = "settings"
                    prev_state.append("mainMenu")
                if options[selected_option] == "Back" or event.key == pygame.K_b:
                    screen.fill(BLACK)
                
                    print(menu_state)
                    print(prev_state)
                    menu_state = prev_state.pop()
                if options[selected_option] == "CRT Timeout":
                    screen.fill(BLACK)
                    print("CRT TIMEOUT")
                    menu_state = "CRT Timeout"
                    prev_state.append("settings")





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
    # screen.blit("highScore", (0,30))
    pygame.display.flip()

 

# Quit Pygame
pygame.quit()
# sys.exit()