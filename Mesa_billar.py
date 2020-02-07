import pygame,sys
from pygame.locals import*
from random import randint
from Ball import Ball,Choques
from Player import Player
from Cue import Cue
import numpy as np
import math

#definiendo colores
negro=(0,0,0)
blanco=(255,255,255)
amarillo=(255,128,0)
rojo=(255,0,0)
Color = (150,70,0)
verdeMesa=(0,143,57)
verdePared=(40,114,51)
radio=14
lenghtCue=320
widthCue=9
#Ventana del Juego
pygame.init()
ventana = pygame.display.set_mode((1500, 600))
pygame.display.set_caption("Billar")
bola8= pygame.image.load("descarga.png")
pygame.display.set_icon(bola8)


carryOn=True
clock=pygame.time.Clock()

#Lados de la mesa
lado1= pygame.Rect(0,0,20,600)
lado2= pygame.Rect(0,0,1200,20)
lado3= pygame.Rect(1180,20,20,600)
lado4= pygame.Rect(0,580,1200,20)
side=pygame.Rect(1200,0,300,600)
bar=pygame.Rect(1320,200,40,200)

elementos= pygame.sprite.Group()

#Introduciendo las bolas 
bolaBlanca= Ball(blanco,radio,0,0,345,105)
elementos.add(bolaBlanca)

bolaAmarilla= Ball(amarillo,radio,0,0,345,245)
elementos.add(bolaAmarilla)

bolaRoja= Ball(rojo,radio,0,0,1000,500)
elementos.add(bolaRoja)

tacoBillar=Cue(Color,lenghtCue,widthCue,bolaAmarilla,100,100)

#sideWindow=Side_Window(negro)
#elementos.add(sideWindow)

bolaJugador=bolaAmarilla
bolas=[bolaBlanca,bolaAmarilla,bolaRoja]

countCarambola=0
c=0
while carryOn:
    ventana.fill(verdeMesa)
    pygame.draw.rect(ventana,verdePared, lado1)
    pygame.draw.rect(ventana,verdePared, lado2)
    pygame.draw.rect(ventana,verdePared, lado3)
    pygame.draw.rect(ventana,verdePared, lado4)
    pygame.draw.rect(ventana,negro, side)
    pygame.draw.rect(ventana,blanco,bar)
    if bolaBlanca.mag_vel<=0.05 and bolaAmarilla.mag_vel<=0.05 and bolaRoja.mag_vel<=0.05:
        carryOn=True
        tacoBillar.Golpear()
        tacoBillar.Draw(ventana)
    else:
        for bola in bolas:
            bola.updateVel()
            if bola.mag_vel != 0:
                bola.update()
                if bola.rect.x>1150:
                    bola.velocity[0] = -bola.velocity[0]
                    bola.wall+=1
                if bola.rect.x<22:
                    bola.velocity[0] = -bola.velocity[0]
                    bola.wall+=1
                if bola.rect.y>550:
                    bola.velocity[1] = -bola.velocity[1]
                    bola.wall+=1
                if bola.rect.y<22:
                    bola.velocity[1] = -bola.velocity[1]
                    bola.wall+=1

        for i in range(0,2):
            for j in range(i+1,3):
                choque=Choques(bolas[i],bolas[j])
                if choque.Norm_r<=2*radio:
                    choque.hacerChoques(bolas[i], bolas[j])
                    if bolas[i]==bolaJugador or bolas[j]==bolaJugador:
                        bolas[i].hit+=1
                        bolas[j].hit+=1
                        
    pygame.display.update()
    elementos.draw(ventana)
    pygame.display.flip()
    clock.tick(40)
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False
c=0
for bola in bolas:
    if bola.hit >=1:
        pass
    else:
        c+=1
if c==0 and bolaJugador.wall>=3:
    countCarambola+=1
print(countCarambola)

pygame.quit()




