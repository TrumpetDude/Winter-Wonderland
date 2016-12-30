#Get it? Present time? Like, the present time, but also, you know, presents? It's a pun, see. Present time. Present. Hahahaha.
from datetime import datetime
import pygame, sys
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((1300,300))

pygame.display.set_caption("Present Time!","Present Time!")
zero = pygame.image.load("0.gif")
one = pygame.image.load("1.gif")
two = pygame.image.load("2.gif")
three = pygame.image.load("3.gif")
four = pygame.image.load("4.gif")
five = pygame.image.load("5.gif")
six = pygame.image.load("6.gif")
seven = pygame.image.load("7.gif")
eight = pygame.image.load("8.gif")
nine = pygame.image.load("9.gif")
colon = pygame.image.load("-.gif")

r = 0
g = 0
b = 0

brightness = 127

def checkForQuit():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit(0)
def drawTime(window):
    time = str(datetime.now().time())[0:8]           
    for x in range(0,8):
        if time[x] == ":":
            window.blit(colon, ((50+150*x),50))
        elif time[x] == "0":
            window.blit(zero, ((50+150*x),50))
        elif time[x] == "1":
            window.blit(one, ((50+150*x),50))
        elif time[x] == "2":
            window.blit(two, ((50+150*x),50))
        elif time[x] == "3":
            window.blit(three, ((50+150*x),50))
        elif time[x] == "4":
            window.blit(four, ((50+150*x),50))
        elif time[x] == "5":
            window.blit(five, ((50+150*x),50))
        elif time[x] == "6":
            window.blit(six, ((50+150*x),50))
        elif time[x] == "7":
            window.blit(seven, ((50+150*x),50))
        elif time[x] == "8":
            window.blit(eight, ((50+150*x),50))
        elif time[x] == "9":
            window.blit(nine, ((50+150*x),50))
            
for b in range(brightness+1):
        window.fill((r,g,b))
        drawTime(window)
        pygame.display.update()
        checkForQuit()
                
while True:
    for r in range(brightness+1):
        window.fill((r,g,b))
        drawTime(window)
        pygame.display.update()
        checkForQuit()
    for b in range(brightness,-1,-1):
        window.fill((r,g,b))
        drawTime(window)
        pygame.display.update()
        checkForQuit()
    for g in range(brightness+1):
        window.fill((r,g,b))
        drawTime(window)
        pygame.display.update()
        checkForQuit()
    for r in range(brightness,-1,-1):
        window.fill((r,g,b))
        drawTime(window)
        pygame.display.update()
        checkForQuit()
    for b in range(brightness+1):
        window.fill((r,g,b))
        drawTime(window)
        pygame.display.update()
        checkForQuit()
    for g in range(brightness,-1,-1):
        window.fill((r,g,b))
        drawTime(window)
        pygame.display.update()
        checkForQuit()
