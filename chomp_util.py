import pygame
import random

def make_background(surface):
    #load images
    water = pygame.image.load('assests/sprites/water.png').convert()
    sand = pygame.image.load('assests/sprites/sand.png').convert()
    sandtop = pygame.image.load('assests/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assests/sprites/seagrass.png').convert()
    waves = pygame.image.load('assests/sprites/waves.png').convert()
    img_px = 64


    #set dark pixels as transparent
    sandtop.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))
    waves.set_colorkey((0,0,0))

    #drawing the water (duplicaitng the image until it fills up screen)
    for x in range(0, surface.get_width(), water.get_width()):
        for y in range(0, surface.get_height(), water.get_height()):
            surface.blit(water,(x,y))

    #drawing base sand
    for x in range(0, surface.get_width() - water.get_width()):
        surface.blit(sand,(x, surface.get_height() - water.get_height()))

    #draw top sand
    for x in range(0, surface.get_width(), water.get_width()):
        surface.blit(sandtop,(x, surface.get_height() - sand.get_height() - sandtop.get_height()))

    #draw seagrass
    for _ in range(0, 5):
        x = random.randint(0, surface.get_width() - seagrass.get_width())
        surface.blit(seagrass, (x, surface.get_height() - sand.get_height() - sandtop.get_height() - seagrass.get_height() + 5))

    for x in range(0, surface.get_width(), water.get_width()):
        surface.blit(waves, (x, waves.get_height() + 5))