import pygame
import random
import time

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


def words(background):
    # Screen dimensions
    scr_wid = 1200  # (px)
    scr_hgt = 600  # (px)

    # Create the screen
    scr = pygame.display.set_mode((scr_wid, scr_hgt))
    pygame.display.set_caption('Making a customized background')

    #makes the custom word
    custom_font = pygame.font.Font('assests/fonts/Black_Crayon.ttf', 128)
    text = custom_font.render('Chomp', True, (255, 69, 0))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2))

    pygame.display.flip()
    print('SPLASH SCREEN')
    time.sleep(1)
    print('Running Game')


class Fish:

    def __init__(self, scr, color='green', x_spd=.2, y_spd=.1):
        water = pygame.image.load('assests/sprites/water.png').convert()
        sand = pygame.image.load('assests/sprites/sand.png').convert()
        sandtop = pygame.image.load('assests/sprites/sand_top.png').convert()
        seagrass = pygame.image.load('assests/sprites/seagrass.png').convert()
        waves = pygame.image.load('assests/sprites/waves.png').convert()
        fname = f'assests/sprites/{color}_fish.png'
        self.fish_img = pygame.image.load(fname).convert()
        self.fish_img.set_colorkey((0, 0, 0))
        self.fish_x = random.randint(0, scr.get_width() - self.fish_img.get_width())
        self.fish_y = random.randint(0, scr.get_height() - self.fish_img.get_height())
        self.up = False
        self.forward = True
        self.fish_xspeed = scr.get_width()/(5*60)
        self.fish_yspeed = scr.get_height()/(5*60)
        self.fish_ybound = scr.get_height() - sand.get_height() - sandtop.get_height() - seagrass.get_height()
        self.num_update_run = 0
        self.num_update_run2 = random.randint(200,500)


    def update_pos(self, scr):

        #increment
        self.num_update_run += 1
        if (self.num_update_run >= self.num_update_run2):
            self.up = not self.up
            self.forward = not self.forward
            self.fish_img = pygame.transform.flip(self.fish_img, True, False)
            self.num_update_run2 = random.randint(200,500)
            self.num_update_run = 0



        # update fish position
        if self.forward:
            self.fish_x += self.fish_xspeed
        else:
            self.fish_x -= self.fish_xspeed
        if self.up:
            self.fish_y -= self.fish_yspeed
        else:
            self.fish_y += self.fish_yspeed


        # check position of the fish
        if self.fish_x > scr.get_width() - self.fish_img.get_width():
            self.forward = False
            self.fish_img = pygame.transform.flip(self.fish_img, True, False)
        if self.fish_x < 0:
            self.forward = True
            self.fish_img = pygame.transform.flip(self.fish_img, True, False)
        if self.fish_y > (self.fish_ybound):
            self.up = True
        if self.fish_y < 0:
            self.up = False


        # draws the fish
        scr.blit(self.fish_img, (self.fish_x, self.fish_y))

class C_Fish(Fish):

    def __init__(self, screen, color):
        super().__init__(screen, color)
        puffer = pygame.image.load('assests/sprites/puffer_fish.png').convert()
        self.fish_img = pygame.image.load(puffer).convert()