''' holds MusicCtrlr class '''
import pygame
import os
from ctrlr import Ctrlr

from const import BANK_PATHS
from lib import rect_to_draw


class MusicCtrlr(Ctrlr):
    '''
    A class which represents the music
    '''

    def __init__(self):
        Ctrlr.__init__(self)

        self.sounds = []
        self.is_playing = []

        all_files = []
        for path in BANK_PATHS:
            cur_files = []
            for file in os.listdir(path):
                cur_files.append(os.path.join(path, file))
            all_files.append(cur_files)

        for bank in all_files:
            bank_sounds = []
            toggles = []
            for f in bank:
                snd = pygame.mixer.Sound(f)
                snd.set_volume(0.35)
                bank_sounds.append(snd)
                toggles.append(False)
            self.sounds.append(bank_sounds)
            self.is_playing.append(toggles)

    def draw(self, screen):

        for idx_bank in range(len(self.is_playing)):
            playing = self.is_playing[idx_bank]
            for idx_slot in range(len(playing)):
                (left_coord, size_coord) = rect_to_draw(
                    idx_bank, idx_slot, 1, 1, self)
                spot = pygame.Rect(left_coord, size_coord)
                spot = spot.inflate(-15, -15)
                if(playing[idx_slot]):
                    pygame.draw.rect(screen, (0, 255, 0), spot)
                elif idx_slot % 2 == 0:
                    pygame.draw.rect(screen, (0, 35, 0), spot)
                else:
                    pygame.draw.rect(screen, (20, 20, 20), spot)

    def play(self, bank, slot):
        if not self.is_playing[bank][slot]:
            self.sounds[bank][slot].play()
            self.is_playing[bank][slot] = True

    def stop(self, bank, slot):
        if self.is_playing[bank][slot]:
            self.sounds[bank][slot].stop()
            self.is_playing[bank][slot] = False

    def stop_all(self):
        for idx_bank in range(len(self.is_playing)):
            bank = self.sounds[idx_bank]
            for idx_slot in range(len(bank)):
                self.stop(idx_bank, idx_slot)
