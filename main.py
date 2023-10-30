import pygame
import sys
import random
from chomp_util import *
import time

# Initialize Pygame
pygame.init()

#Create Pygame clock
clock = pygame.time.Clock()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning main.py.')
print('-------------------------------------------\n')

# Screen dimensions
scr_wid = 1200  # (px)
scr_hgt = 600  # (px)

# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Making a customized background')

#make static background
background = scr.copy()
make_background(background)

#Show splash screen
words(background)

#update display
pygame.display.flip()


bob = Fish(scr, 'orange', .4, .2)
chad = Fish(scr, 'green')
bo = Fish(scr, 'orange', .3, .1)
mary = C_Fish(scr)

running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(f'User pressed {event.key}')

        if event.type == pygame.KEYUP:
            print(f'User pressed {event.key}')


        if event.type == pygame.QUIT:
            running = False



    #draw the background
    scr.blit(background, (0,0))

    #update fish position
    bob.update_pos(scr)
    chad.update_pos(scr)
    bo.update_pos(scr)
    mary.update_pos(scr)

    # Update the display (sends it to the screen).
    pygame.display.flip()

    clock.tick(60)

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()


