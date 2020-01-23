import pygame,sys
from pygame.locals import*
from random import randint
from Ball import Ball,Choques
from Player import Player
import numpy as np
import math

#definiendo colores
blanco=(255,255,255)
amarillo=(255,128,0)
rojo=(255,0,0)
verdeMesa=(0,143,57)
verdePared=(40,114,51)
radio=14
#Ventana del Juego
pygame.init()
ventana = pygame.display.set_mode((1200, 600))
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

elementos= pygame.sprite.Group()

#Introduciendo las bolas 
bolaBlanca= Ball(blanco,radio,11.0,7.0)
bolaBlanca.rect.x = 345
bolaBlanca.rect.y = 105
elementos.add(bolaBlanca)

bolaAmarilla= Ball(amarillo,radio,-8.0,-12.0)
bolaAmarilla.rect.x = 345
bolaAmarilla.rect.y = 245
elementos.add(bolaAmarilla)

bolaRoja= Ball(rojo,radio,5.0,15.0)
bolaRoja.rect.x = 1000
bolaRoja.rect.y = 500
elementos.add(bolaRoja)

bolaJugador=bolaBlanca
bolas=[bolaBlanca,bolaAmarilla,bolaRoja]

countCarambola=0
    
while carryOn:
    if bolaBlanca.mag_vel<=0.05 and bolaAmarilla.mag_vel<=0.05 and bolaRoja.mag_vel<=0.05:
        carryOn=False
    else:
        for bola in bolas:
            bola.update()
            if bola.rect.x>1152:
                bola.velocity[0] = -bola.velocity[0]
                bola.wall+=1
            if bola.rect.x<20:
                bola.velocity[0] = -bola.velocity[0]
                bola.wall+=1
            if bola.rect.y>552:
                bola.velocity[1] = -bola.velocity[1]
                bola.wall+=1
            if bola.rect.y<20:
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
                        
   
    ventana.fill(verdeMesa)

        #dibujando todo
    pygame.draw.rect(ventana,verdePared, lado1)
    pygame.draw.rect(ventana,verdePared, lado2)
    pygame.draw.rect(ventana,verdePared, lado3)
    pygame.draw.rect(ventana,verdePared, lado4)
        
    pygame.display.update()
    elementos.draw(ventana)
    pygame.display.flip()
    clock.tick(40)
    click = pygame.mouse.get_pressed()
    print(click[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("pressed")
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




