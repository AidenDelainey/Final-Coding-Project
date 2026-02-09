##----------------------##
#) game name            (#
#) Aiden Delainey       (#
#) feb 2/2026           (#
#) ver 0.0.1            (#
##----------------------##

################ imports ###############
import matplotlib.pyplot as plt
import pygame, random
from os import path

############## seting up files #################
img_dir = path.join(path.dirname(__file__), 'image')
snd_dir = path.join(path.dirname(__file__), 'sound')
fnt_dir = path.join(path.dirname(__file__), 'font')

############## setting up screen #####################

WIDTH = 1000
HEIGHT = 600
FPS = 30

########### initilize pygame #############
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

font_name = 'pixel font.ttf'

################### functions #####################
def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


############## set up game ################
running = True
screen.fill((20,20,20))
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    verty = random.randrange(-50, HEIGHT)
    vertx = random.randrange(0, WIDTH)
    R = random.randrange(10,255)
    G = random.randrange(10,255)
    B = random.randrange(10,255)
    print(verty, vertx)
    draw_text(screen, 'Hello World', 100, vertx , verty, (R,G,B))
    pygame.display.flip()
    
pygame.quit()


############ licences #############
# Copyright 2021 The Pixelify Sans Project Authors (https://github.com/eifetx/Pixelify-Sans)