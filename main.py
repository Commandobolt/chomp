import pygame
import sys
from chomp_util import make_background

# Initialize Pygame
pygame.init()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning main.py.')
print('-------------------------------------------\n')

# Screen dimensions
scr_wid = 800  # (px)
scr_hgt = 600  # (px)

# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Making a customized background')

#make static background
background = scr.copy()
make_background(background)

running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scr.blit(background, (0,0))

    # Update the display
    pygame.display.flip()

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()


