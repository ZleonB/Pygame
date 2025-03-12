import os, sys
import pygame
from pygame.locals import *
from io import open
from statistics import mode, multimode
import random
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Hogwarts Adventure')
window = pygame.display.set_mode((1800, 900), pygame.RESIZABLE)
screen = pygame.display.get_surface()
text_font= pygame.font.SysFont("Candara", 25, bold=True)

atst=30         # Attack Stat #
swordstup=30
swordstlow=40

def draw_text(text, font, text_color, x, y):
  img=font.render(text, True, text_color)
  textrect=img.get_rect()
  screen.blit(img, (x, y))


container=pygame.Rect(300,200,1000,30)
attack=pygame.Rect(1300,700, 100,100)
screen.fill("white")
pygame.draw.rect(screen, "red", container)
pygame.draw.rect(screen, "blue", container, width=4)
button=pygame.draw.rect(screen, (124,134,210), attack)
draw_text("Hit!", text_font, (pygame.Color("black")), 1330,735)
#button.fill("red")
pygame.display.flip()

mx, my = pygame.mouse.get_pos()

running=True
click=False

health=1000

while running ==True:

  for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        
  if button.collidepoint((mx, my)):
            if click:
              click=False   
              screen.fill("white")
              health-=atst+(random.randint(swordstup,swordstlow))
              container=pygame.Rect(300,200,1000,30)
              button=pygame.draw.rect(screen, (124,134,210), attack)
              draw_text("Hit!", text_font, (pygame.Color("black")), 1330,735)
              #newcontainer=pygame.Rect(300,200,(1000-(atst+random.randint(swordst)),30))
              newcontainer=pygame.Rect(300,200,health,30)
              #pygame.draw.rect(screen, "red", container)
              pygame.draw.rect(screen, "white", container)
              pygame.draw.rect(screen, "red", newcontainer)
              pygame.draw.rect(screen, "blue", container, width=4)
              pygame.display.flip()
              draw_text("Health:  "+str(health), text_font, (pygame.Color("black")), 300,600)
              pygame.display.flip()
              if health<=0:
                screen.fill("white") 
                draw_text("You win!", text_font, (pygame.Color("black")), 300,600)
                pygame.display.flip()



  mx, my = pygame.mouse.get_pos()

  pygame.display.update()
  mainClock.tick(60)

