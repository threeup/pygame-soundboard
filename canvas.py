''' holds CanvasCtrlr class '''
import pygame
from ctrlr import Ctrlr
from lib import rect_to_draw
from const import SCREEN_WIDTH, SCREEN_HEIGHT


class CanvasCtrlr(Ctrlr):
    '''
    A class which represents the canvas
    '''

    def __init__(self, music):
        Ctrlr.__init__(self)
        self.current_col = 0
        self.current_row = 0
        self.slide_expire = -1

        raw_bg_img = pygame.image.load("bg2.jpg")
        self.bg = pygame.transform.scale(
            raw_bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.music = music

    def drawbg(self, screen):
        screen.blit(self.bg, (0, 0))

    def drawfg(self, screen):
        RED = (255, 0,   0)
        ORANGE = (255, 120,   0)
        (left_coord, size_coord) = rect_to_draw(
            self.current_row, self.current_col, 3, 1, self.music)
        row = pygame.Rect(left_coord, size_coord)
        pygame.draw.rect(screen, (255,255,255), row.inflate(20, 20))
        pygame.draw.rect(screen, ORANGE, row.inflate(10, 10))
        pygame.draw.rect(screen, RED, row.inflate(2, 2))
        pygame.draw.rect(screen, (0, 0, 0), row.inflate(-15, -15))

    def slide_row(self):
        if self.slide_expire > 0:
            return
        row_len = len(self.music.sounds[self.current_row])
        self.current_col = (self.current_col + 1) % (row_len-2)
        self.slide_expire = 500

    def advance_row(self):
        self.current_row = (self.current_row + 1) % len(self.music.sounds)

    def get_current(self, offset):
        return (self.current_row, self.current_col+offset)

    
    def tick(self, delta):
        if self.slide_expire > 0:
            self.slide_expire -= delta*1000
