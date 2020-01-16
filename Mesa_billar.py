import pygame,sys
from pygame.locals import*
from random import randint
from Ball import Ball,Choques
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
bolaBlanca= Ball(blanco,radio,0.0,0.0)
bolaBlanca.velocity=np.array([13.0,7.0])
bolaBlanca.rect.x = 345
bolaBlanca.rect.y = 105
elementos.add(bolaBlanca)

bolaAmarilla= Ball(amarillo,radio,0.0,0.0)
bolaAmarilla.velocity=np.array([21.0,-6.0])
bolaAmarilla.rect.x = 345
bolaAmarilla.rect.y = 245
elementos.add(bolaAmarilla)

bolaRoja= Ball(rojo,radio,0.0,0.0)
bolaRoja.velocity=np.array([3.0,-8.0])
bolaRoja.rect.x = 1000
bolaRoja.rect.y = 500
elementos.add(bolaRoja)

bolas=[bolaBlanca,bolaAmarilla,bolaRoja]
print(bolas[0])
    
while carryOn:
    for event in pygame.event.get():
        countChoques=0
        countCarambolas=0
        for bola in bolas:
            bola.update()
        if event.type == pygame.QUIT:
            carryOn=False
        for bola in bolas:
            if bola.rect.x>1152:
                bola.velocity[0] = -bola.velocity[0]
            if bola.rect.x<20:
                bola.velocity[0] = -bola.velocity[0]
            if bola.rect.y>552:
                bola.velocity[1] = -bola.velocity[1]
            if bola.rect.y<20:
                bola.velocity[1] = -bola.velocity[1]

        for i in range(0,2):
            for j in range(i+1,3):
                choque=Choques(bolas[i],bolas[j])
                if choque.Norm_r<=2*radio:
                    choque.hacerChoques(bolas[i], bolas[j])
                    if bolas[i]==bolaBlanca or bolas[j]==bolaBlanca:
                        

            
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
pygame.quit()




