import pygame
import random
import time

pygame.init()
#Making window
display_width, display_height = 700, 600
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dr. Goon's Winter Arc")
clock = pygame.time.Clock()

dgwaImg = pygame.image.load('Dr.goon title.png')
DEFAULT_IMAGE_SIZE = (700, 600)
dgwaImg = pygame.transform.scale(dgwaImg, DEFAULT_IMAGE_SIZE)

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
Mark = pygame.font.SysFont("arial",160)
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

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(dgwaImg,(0,0))
        TextSurf, TextRect = text_objects("Dr.Goon", largeText, black)
        TextRect.center = ((display_width/2),(display_height/6))
        window.blit(TextSurf, TextRect)
        print(pygame.mouse.get_pos())
        pygame.display.update()

def game_loop():

    pygame.mixer.music.load('Croc Legend Of The Gobbos - Main Menu (OST).mp3')
    pygame.mixer.music.play(-1) 
    gameExit = False
    time.sleep(.1)
    global turn
    turn=0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(gray)
game_intro()
pygame.quit()
