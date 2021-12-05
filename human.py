''' holds HumanCtrlr class '''
import pygame
from ctrlr import Ctrlr


class HumanCtrlr(Ctrlr):
    '''
    A class which manipulates controlled entities
    '''

    def __init__(self):
        Ctrlr.__init__(self)
        self.button_count = 4
        self.pressed = []
        self.duration = []
        for _ in range(self.button_count):
            self.pressed.append(False)
            self.duration.append(0)

    def handle_event(self, event):
        if event.type == pygame.JOYBUTTONDOWN:
            for idx in range(self.button_count):
                if event.button == idx:
                    self.pressed[idx] = True
        elif event.type == pygame.JOYBUTTONUP:
            for idx in range(self.button_count):
                if event.button == idx:
                    self.pressed[idx] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.pressed[0] = True
            elif event.key == pygame.K_y:
                self.pressed[1] = True
            elif event.key == pygame.K_g:
                self.pressed[2] = True
            elif event.key == pygame.K_b:
                self.pressed[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                self.pressed[0] = False
            elif event.key == pygame.K_y:
                self.pressed[1] = False
            elif event.key == pygame.K_g:
                self.pressed[2] = False
            elif event.key == pygame.K_b:
                self.pressed[3] = False

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        BLUE = (0,   0, 255)
        pygame.draw.circle(screen, BLUE, pos, 20)

    def tick(self, delta):
        for i in range(self.button_count):
            if self.pressed[i]:
                self.duration[i] += delta*1000

    def post_tick(self):
        for i in range(self.button_count):
            if not self.pressed[i]:
                self.duration[i] = 0
