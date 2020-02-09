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

#definiendo caracteristicas de los objetos
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
bolaBlanca= Ball(blanco,radio,0,0,345,270)
elementos.add(bolaBlanca)

bolaAmarilla= Ball(amarillo,radio,0,0,845,288)
elementos.add(bolaAmarilla)

bolaRoja= Ball(rojo,radio,0,0,845,252)
elementos.add(bolaRoja)

#defino los dos tacos, uno para blanco y otro para amarilla
tacoBlanco=Cue(Color,lenghtCue,widthCue,bolaBlanca,100,100)
tacoAmarillo=Cue(Color,lenghtCue,widthCue,bolaAmarilla,100,100)

#lo guardo todo en un vector 0 es blanco y 1 es amarillo
tacoBillar = [tacoBlanco,tacoAmarillo] 


bolas=[bolaBlanca,bolaAmarilla,bolaRoja]

EnTurno = False #inicia sin estar en turno
turno = 0 #inicializo jugador blanco

countCarambola = [0,0] #inicializo carmbolas
while carryOn:

    #dibujar los objetos estáticos en la pantalla
    ventana.fill(verdeMesa)
    pygame.draw.rect(ventana,verdePared, lado1)
    pygame.draw.rect(ventana,verdePared, lado2)
    pygame.draw.rect(ventana,verdePared, lado3)
    pygame.draw.rect(ventana,verdePared, lado4)
    pygame.draw.rect(ventana,negro, side)
    pygame.draw.rect(ventana,blanco,bar)

    #Mensajes en la pantalla
    font1 = pygame.font.Font(None, 60)
    font2 = pygame.font.Font(None, 50)
    font3 = pygame.font.Font(None, 80)
    text = font1.render(str(countCarambola[0]), 2, blanco)
    ventana.blit(text, (1280,100))
    text = font1.render(str(countCarambola[1]), 1, amarillo)
    ventana.blit(text, (1380,100))
    text = font2.render("Carambolas",1,blanco)
    ventana.blit(text, (1240,50))

    
    if bolaBlanca.mag_vel<=0.05 and bolaAmarilla.mag_vel<=0.05 and bolaRoja.mag_vel<=0.05:
        if(EnTurno == True):
            c=0
            for bola in bolas:
                if bola.hit >=1:
                    pass
                else:
                    c+=1
            #mensaje de anotacion de un punto
            if c==0 and tacoBillar[turno].target_ball.wall>=3:
                countCarambola[turno]+=1
                text = font3.render("Jugador "+str(turno+1)+" ha anotado un punto", 2, blanco)
                ventana.blit(text, (400,250))
                pygame.display.flip()
                pygame.time.wait(3000)

            #mensaje de juego ganado    
            if countCarambola[0]==3 or countCarambola[1]==3:
                text = font3.render("Jugador "+str(turno+1)+" tiene 3 puntos y ha ganado!", 2, blanco)
                ventana.blit(text, (370,250))
                pygame.display.flip()
                pygame.time.wait(3000)
                carryOn=False

            #reinicio de contadores
            for bola in bolas:
                bola.hit=0
                bola.walls=0
            turno = (turno+1)%2 #cambio turno antes de dibujar el taco solo si antes estaba en turno
            EnTurno = False #deja de estar en turno

        #golpear bola con el taco definido
        tacoBillar[turno].Golpear()
        tacoBillar[turno].Draw(ventana)
        
    else:
        EnTurno = True #si entra a este else es porque comienza el turno
        for bola in bolas:
            bola.updateVel()
            if bola.mag_vel != 0:
                bola.update()
                if bola.rect.x>1149:
                    bola.velocity[0] = -bola.velocity[0]
                    bola.wall+=1
                if bola.rect.x<23:
                    bola.velocity[0] = -bola.velocity[0]
                    bola.wall+=1
                if bola.rect.y>549:
                    bola.velocity[1] = -bola.velocity[1]
                    bola.wall+=1
                if bola.rect.y<23:
                    bola.velocity[1] = -bola.velocity[1]
                    bola.wall+=1
                    
        #choques entre bolas
        for i in range(0,2):
            for j in range(i+1,3):
                choque=Choques(bolas[i],bolas[j])
                if choque.Norm_r<=2*radio:
                    choque.hacerChoques(bolas[i], bolas[j])
                    if bolas[i]==tacoBillar[turno].target_ball or bolas[j]==tacoBillar[turno].target_ball:#miro si se estrello con la bola target del taco
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

pygame.quit()
