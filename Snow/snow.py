import pygame, sys
from pygame.locals import *
from random import randint
pygame.init()
window = pygame.display.set_mode((1300,700), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
pygame.display.set_caption("Snow","Snow")
window.fill((200,200,200))
snowflake1 = pygame.image.load("snowflake1.gif")
snowflake2 = pygame.transform.rotate(pygame.image.load("snowflake1.gif"),90)
snowflake3 = pygame.image.load("snowflake2.gif")
snowflake4 = pygame.transform.rotate(pygame.image.load("snowflake2.gif"),90)
snowflake5 = pygame.image.load("snowflake3.gif")
snowflake6 = pygame.transform.rotate(pygame.image.load("snowflake3.gif"),90)
snowflakeImages = [snowflake1, snowflake2, snowflake3, snowflake4, snowflake5, snowflake6]
match = pygame.image.load("match.gif")
matchX = randint(0,1285)
snowflakes = []
speed = 5#Bigger = faster
snowSpeed = 2 #Bigger = faster
snowFrequency = 25#Smaller = more snow
increaseRate = 250#Smaller = Faster
if snowFrequency < 2:
    snowFrequency = 2
score = 0

def drawText(window, text, size, color, centerX, centerY):
    font=pygame.font.Font("DickensianChristmas.ttf", size)
    renderedText=font.render(str(text),True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

def gameOver(window):
    for flake in snowflakes:
        window.blit(flake[0], (flake[1],flake[2]))
    drawText(window, score, 96, (0,0,0), 650, 50)
    drawText(window, "GAME OVER!", 120, (0,0,0), 650, 350)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit(0)
    
ticks = 0

while True:
    ticks += 1

    if ticks%increaseRate == 0 and snowFrequency > 10:
        snowFrequency -= 1
        snowSpeed += 0.1
        
    window.fill((200,200,200))
    drawText(window, score, 96, (0,0,0), 650, 50)
    if randint(1,snowFrequency) == 1:
        #                  IMAGE                          X-COORDINATE     Y-COORDINATE
        snowflakes.append([snowflakeImages[randint(0,5)], randint(0,1234), -64])
    for flake in snowflakes:
        if flake[0] == snowflake1:
            flake[2] += snowSpeed*0.8
            flake[1] += randint(-2,1)
        elif flake[0] == snowflake2:
            flake[2] += snowSpeed*0.8
            flake[1] += randint(-1,2)
        elif flake[0] == snowflake3 or flake[0] == snowflake4:
            flake[2] += snowSpeed*1.25
            flake[1] += randint(-1,1)
        else:
            flake[2] += snowSpeed
            flake[1] += randint(-2,2)
        #           IMAGE      LOCATION
        window.blit(flake[0], (flake[1],flake[2]))
        if flake[2] > 700:
            snowflakes.remove(flake)
            score += 1
        if 631 > flake[2] > 528 and matchX+15 > flake[1] > matchX-64:
            gameOver(window)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                matchX -= 15
        elif event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_d:
                matchX += 15

    keys = pygame.key.get_pressed()
    if (keys[K_a] or keys[K_LEFT]):
        window.blit(pygame.transform.rotate(match, -10),(matchX, 592))
        matchX -= speed
    if (keys[K_d] or keys[K_RIGHT]):
        window.blit(pygame.transform.rotate(match, 10),(matchX, 592))
        matchX += speed
    if not (keys[K_a] or keys[K_LEFT] or keys[K_d] or keys[K_RIGHT]):
        window.blit(match, (matchX, 592))

    if matchX < 15:
        matchX += 1300
    elif matchX > 1285:
        matchX -= 1300
    pygame.display.update()
