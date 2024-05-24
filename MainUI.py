import pygame
import random
import math
# Skeleton of what the UI should be


pygame.init()
pygame.display.set_caption('Linux Memory Use Utility')

screenX = 800
screenY = 600

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

score = 0
my_font = pygame.font.SysFont('Courier', 30)

highScore = my_font.render(f'HIGH SCORE: {score}', False, white)

screen = pygame.display.set_mode((screenX,screenY))
# clock = pygame.time.Clock()

# Display score and high score
pygame.font.init() 


running = True
while running:
    # FPS = 30 # frames per second setting
    # fpsClock = pygame.time.Clock()
    
    # Background color
    screen.fill((0,0,0))
   
    # Display score
    text_surface = my_font.render(f'SCORE: {score}', False, white)
    screen.blit(text_surface, (0,0))
    
    #display high score
    screen.blit(highScore, (0,30))
    
    # fpsClock.tick(FPS)
    pygame.display.update()