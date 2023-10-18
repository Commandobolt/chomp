import pygame
import sys

# Initialize Pygame
pygame.init()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning make_background.py.')
print('-------------------------------------------\n')

# Screen dimensions
scr_wid = 800  # (px)
scr_hgt = 600  # (px)

# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Making a customized background')


#load images
water = pygame.image.load('assests/sprites/water.png').convert()
sand = pygame.image.load('assests/sprites/sand.png').convert()
img_px = 64

#drawing the water (duplicaitng the image until it fills up screen)
for x in range(0, scr_wid, img_px):
    for y in range(0, scr_hgt, img_px):
        scr.blit(water,(x,y))

#drawing the sand
for x in range(0, scr_wid, img_px):
        scr.blit(sand,(x, scr_hgt - img_px))


running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()


