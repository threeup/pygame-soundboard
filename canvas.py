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

        raw_bg_img = pygame.image.load("hexgame.jpg")
        self.bg = pygame.transform.scale(
            raw_bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.music = music

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        RED = (255, 0,   0)
        #row_len = len(self.music.sounds[self.current_row])
        (left_coord, size_coord) = rect_to_draw(
            self.current_row, self.current_col, 3, 1, self.music)
        row = pygame.Rect(left_coord, size_coord)
        pygame.draw.rect(screen, RED, row)
        pygame.draw.rect(screen, (0, 0, 0), row.inflate(-15, -15))

    def slide_row(self):
        row_len = len(self.music.sounds[self.current_row])
        self.current_col = (self.current_col + 1) % (row_len-2)

    def advance_row(self):
        self.current_row = (self.current_row + 1) % len(self.music.sounds)

    def get_current(self, offset):
        return (self.current_row, self.current_col+offset)
