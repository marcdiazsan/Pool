import pygame
import numpy as np
import math

 #definiendo la clase Ball
class Player(pygame.sprite.Sprite):
    
    def __init__(self, number,bola,carambolas):
        super().__init__()
        self.number = number
        self.bola=bola
        self.num_carambolas = carambolas
