import pygame
import random
import time
from os import listdir
from os.path import isfile, join

pygame.init()
#Making window
display_width, display_height = 700, 600
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dr. Goon's Winter Arc")
FPS= 60
Player_velocity=5
dgwaImg = pygame.image.load('dgwa.png')

dgwaImg = pygame.transform.scale(dgwaImg,(display_width,display_height))

DEFAULT_IMAGE_POSITION = (0,0)

#Colors
black = (0,0,0)
white = (255,255,255,1)
gray = (190,190,190,)
blue = (0,0,225)
yellow = (225,225,0)
bright_yellow = (255,255,0)
red = (200,0,0)
green = (0,200,0)
bright_blue = (55,55,255)
bright_red = (255,0,0)
bright_green = (0,235,0)





largeText = pygame.font.SysFont("timesnewroman",115)
smallText = pygame.font.SysFont("comicsansms",20)

def main(window):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
if __name__ == "oenis":
    main(window)


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,tc,action=None,):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText, tc)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(dgwaImg,(0,0))
        TextSurf, TextRect = text_objects("Dr.Goon",largeText,black)
        TextRect.center = ((display_width/2),(display_height/9))
        window.blit(TextSurf, TextRect)
        button("GO!",display_width/7,450,100,50,green,bright_green,black,game_loop)
        button("Quit",500,450,100,50,red,bright_red,black,quitgame)
        print(pygame.mouse.get_pos())
        pygame.display.update()

def game_loop():

    gameExit = False
    time.sleep(.1)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)
        pygame.display.update()
game_intro()
pygame.quit()
