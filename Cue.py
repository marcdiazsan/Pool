import pygame
import numpy as np
import math
Negro = (0,0,0)
Color = (200,200,200)


 #definiendo la clase Cue
class Cue(pygame.sprite.Sprite):
    
    def __init__(self,color, lenght,width, ball,pos_x,pos_y):
        super().__init__()
        self.color = color
        self.lenght= lenght
        self.width = width
        self.target_ball=ball

    def Draw(self,screen):
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        Ball_x=self.target_ball.centerPosition[0]
        Ball_y=self.target_ball.centerPosition[1]
        a = np.array([Ball_x-Mouse_x,Ball_y-Mouse_y])
        theta=math.pi-math.acos((Ball_x-Mouse_x)/(math.sqrt(a[0]**2+a[1]**2)))
        if Ball_y>Mouse_y:
            start=np.array([Ball_x+math.cos(theta)*23,Ball_y-math.sin(theta)*23])
            end=np.array([Ball_x+math.cos(theta)*self.lenght,Ball_y-math.sin(theta)*self.lenght])
        else:
            start=np.array([Ball_x+math.cos(theta)*23,Ball_y+math.sin(theta)*23])
            end=np.array([Ball_x+math.cos(theta)*self.lenght,Ball_y+math.sin(theta)*self.lenght])
        pygame.draw.line(screen,self.color,(end[0],end[1]),(start[0],start[1]), self.width)

    def Golpear(self):
        norma = math.sqrt(self.velocity[0]**2+self.velocity[1]**2)
        cte=1-(friction_coeff)/(2*norma)
        cte2=1-(friction_coeff)/(norma)
        if cte2>0:
           self.rect.x += round(cte*self.velocity[0])
           self.rect.y += round(cte*self.velocity[1])
           self.velocity*=cte2
           self.mag_vel = math.sqrt(self.velocity[0]**2+self.velocity[1]**2)
