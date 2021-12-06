''' holds Sparkle class '''
import pygame
import os
import random

from const import IMG_PATHS
class Sparkle:
    '''
    A visual element
    '''

    def __init__(self, pos, row):  
        self.name = "sparkle"    
        self.ttl = 1000
        self.pos = pos
        self.vel = (1,1)
        
        path = IMG_PATHS[row]
        files = []
        for file in os.listdir(path):
            files.append(os.path.join(path, file))
        
        raw_img = pygame.image.load(random.choice(files))
        
        self.img = pygame.transform.scale(
            raw_img, (200, 200))


    def draw(self, screen):
        screen.blit(self.img, self.pos)
        

    def tick(self, delta):
        self.ttl -= delta*1000
        #self.pos += self.vel
        
