import pygame
from math import pi
import random

def blink():
    pygame.draw.ellipse(screen, BLACK, [105, 74, 20, 2]) 
    pygame.draw.ellipse(screen, BLACK, [195, 74, 20, 2])

def sad():
    pygame.draw.arc(screen, BLACK, [90, 160, 150, 125], 0, pi, 4)

def smile():
    pygame.draw.arc(screen, BLACK, [90, 80, 150, 125], 2*pi/2, 2*pi, 4)
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [320, 240]
screen = pygame.display.set_mode(size)
 
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    screen.fill(WHITE)

    chance = random.random()
    print(chance)
    # Draw eyes
    if chance > 0.8:
        blink()
    else:
        pygame.draw.ellipse(screen, BLACK, [105, 50, 20, 50]) 
        pygame.draw.ellipse(screen, BLACK, [195, 50, 20, 50])

    # Draw mouth
    sad()
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()