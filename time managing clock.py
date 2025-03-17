import os, sys
import pygame

from pygame.locals import *
from io import open
from statistics import mode, multimode
import random
import math
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Hogwarts Adventure')
window = pygame.display.set_mode((1800, 900), pygame.RESIZABLE)
screen = pygame.display.get_surface()
text_font= pygame.font.SysFont("Candara", 25, bold=True)



mainClock.tick(60)
animation_cooldown=600
last_update=pygame.time.get_ticks()

def draw_text(text, font, text_color, x, y):
  img=font.render(text, True, text_color)
  textrect=img.get_rect()
  screen.blit(img, (x, y))

X=400; Y=100; w=600; h=600; stA=math.pi/2; endA=math.pi/2; linewidth=400


running=True


while running==True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         quit()
     #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    
    current_time = pygame.time.get_ticks()
    if current_time-last_update >= animation_cooldown:
        stA-=2*math.pi/60
        last_update=current_time
        pygame.draw.circle(screen, "yellow", (700,400),(300))
        pygame.draw.line(screen, "black", (700,400), (700,700), width=4)
        pygame.draw.arc(screen, "black", (X,Y,w,h), stA, endA, linewidth)
        pygame.display.update()
        if -stA>=(3*endA+math.pi/60):
         stA=math.pi/2
         pygame.draw.circle(screen, "yellow", (700,400),(300))
         pygame.display.update()

    screen.fill("white")
    pygame.draw.circle(screen, "yellow", (700,400),(300))
    pygame.draw.line(screen, "black", (700,400), (700,700), width=4)
    pygame.draw.arc(screen, "black", (X,Y,w,h), stA, endA, linewidth)

    mx, my = pygame.mouse.get_pos()

    pygame.display.update()
    


