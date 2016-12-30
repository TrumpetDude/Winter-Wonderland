#By all means, change any of the variables with comments attached,
#but leave the uncommented ones alone
import pygame, sys
from pygame.locals import *
from random import randint
import os
if not(os.path.isfile(os.path.dirname(os.path.realpath(__file__))+'/blizzardHighScore.txt')):
    hsfile = open('blizzardHighScore.txt','w')
    hsfile.write('0')
    hsfile.close()
pygame.init()
window = pygame.display.set_mode((1300,700))
pygame.display.set_caption("Blizzard","Blizzard")
snowflake1 = pygame.image.load("snowflake1.gif")
snowflake2 = pygame.transform.rotate(pygame.image.load("snowflake1.gif"),90)
snowflake3 = pygame.image.load("snowflake2.gif")
snowflake4 = pygame.transform.rotate(pygame.image.load("snowflake2.gif"),90)
snowflake5 = pygame.image.load("snowflake3.gif")
snowflake6 = pygame.transform.rotate(pygame.image.load("snowflake3.gif"),90)
snowflakeImages = [snowflake1, snowflake2, snowflake3, snowflake4, snowflake5, snowflake6]
match = pygame.image.load("match.gif")
burntOut1 = pygame.image.load("burntOut1.gif")
burntOut2 = pygame.image.load("burntOut2.gif")
burntOut3 = pygame.image.load("burntOut3.gif")
burntOut4 = pygame.image.load("burntOut4.gif")
speedBoost = pygame.image.load("lightning.gif")
speedDuration = 500                             #Number of ticks speed powerup lasts
speedStart = -speedDuration - 1
speedOnScreen = False
speedFrequency = 2500                           #How often speed powerup appears (smaller = more often)
shield = pygame.image.load("shield.gif")
shieldDuration = 500                            #Number of ticks shield powerup lasts (smaller = more often)
shieldStart = -shieldDuration - 1
shieldOnScreen = False
shieldFrequency = 2500                          #How often sheild powerup appears
matchX = randint(0,1285)
snowflakes = []
baseSpeed = 7                                   #Bigger = faster match
snowSpeed = 3                                   #Bigger = faster snow
snowFrequency = 25                              #Smaller = more snow
increaseRate = 200                              #Smaller = faster increase
tiltAmount = 16                                 #Bigger = more tilt
tiltSpeed = 2                                   #Bigger = faster tilting


def drawText(window, text, size, color, centerX, centerY):
    font=pygame.font.Font("DickensianChristmas.ttf", size)
    renderedText=font.render(str(text),True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

def gameOver(window, snowflakes):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    hsfile = open('blizzardHighScore.txt','r')
    if score > int(hsfile.read()):
        beatHS = True
        drawText(window, "NEW HIGHSCORE!", 80, (0,0,0), 650, 450)
        hsfile.close()
        hsfile = open('blizzardHighScore.txt','w')
        hsfile.write(str(score))
        hsfile.close()
    else:
        hsfile.close()
        beatHS = False
        hsfile = open('blizzardHighScore.txt')
        highScore = hsfile.read()
        hsfile.close()
        drawText(window, "HIGHSCORE: "+highScore, 80, (0,0,0), 650, 450)
    for flake in snowflakes:
        window.blit(flake[0], (flake[1],flake[2]))
    drawText(window, score, 96, (0,0,0), 650, 50)
    drawText(window, "GAME OVER!", 120, (0,0,0), 650, 350)
    #Burning out animation
    window.blit(burntOut1, (matchX,592))
    pygame.display.update()
    pygame.time.delay(200)
    pygame.draw.line(window, (200,200,200), (matchX+7.5, 592), (matchX+7.5, 700), 15)
    window.blit(burntOut2, (matchX,592))
    pygame.display.update()
    pygame.time.delay(200)
    pygame.draw.line(window, (200,200,200), (matchX+7.5, 592), (matchX+7.5, 700), 15)
    window.blit(burntOut3, (matchX,592))
    pygame.display.update()
    pygame.time.delay(200)
    pygame.draw.line(window, (200,200,200), (matchX+7.5, 592), (matchX+7.5, 700), 15)
    window.blit(burntOut4, (matchX,592))
    pygame.display.update()
    while True:
        window.fill((200,200,200))
        window.blit(burntOut4, (matchX,592))
        drawText(window, score, 96, (0,0,0), 650, 50)
        drawText(window, "GAME OVER!", 120, (0,0,0), 650, 350)
        if beatHS:
            drawText(window, "NEW HIGHSCORE!", 80, (0,0,0), 650, 450)
        else:
            drawText(window, "HIGHSCORE: "+highScore, 80, (0,0,0), 650, 450)
        if randint(1,round(snowFrequency)) == 1:
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
            window.blit(flake[0], (flake[1],flake[2]))
            if flake[2] > 700:
                snowflakes.remove(flake)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit(0)

def done(window):
    if ticks <= shieldStart+shieldDuration:
        window.blit(pygame.transform.scale(shield, (55,60)), (1240,0))
        pygame.draw.line(window,(0,0,0),(1270,75),(1270, 75+shieldDuration-(ticks-shieldStart)),25)
    if ticks <= speedStart+speedDuration:
        window.blit(pygame.transform.scale(speedBoost, (60,60)), (0,0))
        pygame.draw.line(window,(0,0,0),(30,75),(30, 75+speedDuration-(ticks-speedStart)),25)
    pygame.draw.line(window,(255,255,255),(0,350),(1300,350),200)
    drawText(window, "Are you sure you want to quit? Your score will not be saved.",32,(160,160,160),650,300)
    drawText(window, "YES                                         NO",32,(160,160,160),650,402)
    pygame.draw.rect(window, (160,160,160), (395,375,100,50), 5)
    pygame.draw.rect(window, (160,160,160), (815,375,100,50), 5)
    window.blit(pygame.transform.rotate(match, degrees),(matchX, 592))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        mousePos=pygame.mouse.get_pos()
        mousePressed=pygame.mouse.get_pressed()
        if mousePos[1]>375 and mousePos[1]<425 and mousePos[0]>815 and mousePos[0]<915 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            break
        if mousePos[1]>375 and mousePos[1]<425 and mousePos[0]>395 and mousePos[0]<495 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            pygame.quit()
            sys.exit(0)
score = 0
degrees = 0   
ticks = 0
while True:
    ticks += 1
    window.fill((200,200,200))

    if ticks%increaseRate == 0:
        snowFrequency *= 0.925
        snowSpeed += 0.125
        speed += 0.15

    if randint(1,speedFrequency) == 1 and not(speedOnScreen):
        speedOnScreen = True
        speedX = randint(0,1180)
        speedY = -120

    if randint(1,shieldFrequency) == 1 and not(shieldOnScreen):
        shieldOnScreen = True
        shieldX = randint(0,1180)
        shieldY = -120

    if speedOnScreen:
        speedY += snowSpeed
        window.blit(speedBoost, (speedX,speedY))
        if 700 > speedY > 472 and matchX+15 > speedX > matchX-120:
            speedStart = ticks
            speedOnScreen = False
        if speedY > 700:
            speedOnScreen = False

    if shieldOnScreen:
        shieldY += snowSpeed
        window.blit(shield, (shieldX,shieldY))
        if 700 > shieldY > 472 and matchX+15 > shieldX > matchX-107:
            shieldStart = ticks
            shieldOnScreen = False
        if shieldY > 700:
            shieldOnScreen = False

    if ticks > shieldStart+shieldDuration:
        invincible = False
    else:
        invincible = True
        window.blit(pygame.transform.scale(shield, (55,60)), (1240,0))
        pygame.draw.line(window,(0,0,0),(1270,75),(1270, 75+shieldDuration-(ticks-shieldStart)),25)
    
    drawText(window, score, 96, (0,0,0), 650, 50)
    if randint(1,round(snowFrequency)) == 1:
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
            if invincible:
                snowflakes.remove(flake)
                score += 2
            else:
                gameOver(window, snowflakes)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            done(window)
    if ticks > speedStart+speedDuration:        
        speed = baseSpeed
        tilt = tiltAmount
    else:
        speed = baseSpeed*2
        tilt = tiltAmount*1.5
        window.blit(pygame.transform.scale(speedBoost, (60,60)), (0,0))
        pygame.draw.line(window,(0,0,0),(30,75),(30, 75+speedDuration-(ticks-speedStart)),25)
    keys = pygame.key.get_pressed()
    if (keys[K_a] or keys[K_LEFT]):
        if degrees > -tilt:
            degrees -= tiltSpeed
        matchX -= speed
    if (keys[K_d] or keys[K_RIGHT]):
        if degrees < tilt:
            degrees += tiltSpeed
        matchX += speed
    if not (keys[K_a] or keys[K_LEFT] or keys[K_d] or keys[K_RIGHT]):
        if degrees > 0:
            degrees -= tiltSpeed
            matchX += tiltSpeed*2
        if degrees < 0:
            degrees += tiltSpeed

    window.blit(pygame.transform.rotate(match, degrees),(matchX, 592))

    if matchX < 15:
        matchX += 1300
    elif matchX > 1285:
        matchX -= 1300
    pygame.display.update()
