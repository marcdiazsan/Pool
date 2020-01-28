import pygame
import numpy as np
import math
Negro = (0,0,0)
Color = (200,200,200)

def normalize(v):
    norm = np.linalg.norm(v) 
    if norm == 0:
        return v 
    return v / norm


 #definiendo la clase Cue
class Cue(pygame.sprite.Sprite):
    
    def __init__(self,color, lenght,width, ball,pos_x,pos_y):
        super().__init__()
        self.color = color
        self.lenght= lenght
        self.width = width
        self.target_ball=ball
        self.start = np.array([0,0])
        self.end = np.array([0,0])
        self.c=0

    def Draw(self,screen):
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        Ball_x=self.target_ball.centerPosition[0]
        Ball_y=self.target_ball.centerPosition[1]
        a = np.array([Ball_x-Mouse_x,Ball_y-Mouse_y])
        theta=math.pi-math.acos((Ball_x-Mouse_x)/(math.sqrt(a[0]**2+a[1]**2)))
        if Ball_y>Mouse_y:
            self.start=np.array([Ball_x+math.cos(theta)*23,Ball_y-math.sin(theta)*23])
            self.end=np.array([Ball_x+math.cos(theta)*self.lenght,Ball_y-math.sin(theta)*self.lenght])
        else:
            self.start=np.array([Ball_x+math.cos(theta)*23,Ball_y+math.sin(theta)*23])
            self.end=np.array([Ball_x+math.cos(theta)*self.lenght,Ball_y+math.sin(theta)*self.lenght])
        pygame.draw.line(screen,self.color,(self.end[0],self.end[1]),(self.start[0],self.start[1]), self.width)

    def Golpear(self):
        click = pygame.mouse.get_pressed()
        if click[0]==1:
            self.c +=1
            if self.c > 50:
                self.c = 0
        elif click[0]==0 and self.c>0:
            n=normalize(self.start-self.end)
            self.target_ball.velocity[0]=n[0]*self.c
            self.target_ball.velocity[1]=n[1]*self.c
            self.target_ball.updateVel()
            print(self.c)
            self.c = 0
            
            
