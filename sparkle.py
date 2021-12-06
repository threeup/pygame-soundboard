''' holds Sparkle class '''
import pygame
import os
import random
from lib import coord_add, coord_subtract

from const import IMG_PATHS
class Sparkle:
    '''
    A visual element
    '''

    def __init__(self, pos, row):  
        self.name = "sparkle"    
        self.ttl = 1000
        self.size = 128
        self.pos = coord_subtract(pos, (0.5*self.size,0.5*self.size))
        amtx = random.randrange(-5,5)
        amty = random.randrange(-5,5)
        if pos[1] < 300:
            self.vel = (amtx,abs(amty))
        elif pos[1] > 450:
            self.vel = (amtx,-abs(amty))
        else:
            self.vel = (amtx,amty)
        
        path = IMG_PATHS[row]
        files = []
        for file in os.listdir(path):
            files.append(os.path.join(path, file))
        
        raw_img = pygame.image.load(random.choice(files))
        
        self.img = pygame.transform.scale(
            raw_img, (self.size, self.size))


    def draw(self, screen):
        print(self.pos)
        screen.blit(self.img, self.pos)
        

    def tick(self, delta):
        self.ttl -= delta*1000
        self.pos = coord_add(self.pos, self.vel)
        
