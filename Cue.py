import pygame
import numpy as np
import math
Negro = (0,0,0)
friction_coeff =0.05

 #definiendo la clase Cue
class Cue(pygame.sprite.Sprite):
    
    def __init__(self, color, radio, vel_x, vel_y):
        super().__init__()
        
        self.image = pygame.Surface([2*radio, 2*radio])
        self.image.fill(Negro)
        self.image.set_colorkey(Negro)
        pygame.draw.circle(self.image,color,[radio,radio],radio)
        self.velocity = np.array([vel_x,vel_y])
        self.mag_vel= math.sqrt(vel_x**2+vel_y**2)
        self.rect = self.image.get_rect()
        self.centerPosition= np.array([self.rect.x+radio, self.rect.y+radio])
        self.wall = 0
        self.hit = 0
        
    def update(self):
        norma = math.sqrt(self.velocity[0]**2+self.velocity[1]**2)
        cte=1-(friction_coeff)/(2*norma)
        cte2=1-(friction_coeff)/(norma)
        if cte2>0:
           self.rect.x += round(cte*self.velocity[0])
           self.rect.y += round(cte*self.velocity[1])
           self.velocity*=cte2
           self.mag_vel = math.sqrt(self.velocity[0]**2+self.velocity[1]**2)
