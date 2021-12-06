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

        self.font = pygame.font.SysFont(None, 48)
        self.sounds = []
        self.is_playing = []
        self.channels = []
        for i in range(8):
            self.channels.append(pygame.mixer.Channel(i))

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

    def draw(self, screen, get_current):
        debug = None
        main_row, first_col = get_current(0)
        main_row, last_col = get_current(3)
        for idx_bank in range(len(self.is_playing)):
            playing = self.is_playing[idx_bank]
            for idx_slot in range(len(playing)):
                (left_coord, size_coord) = rect_to_draw(
                    idx_bank, idx_slot, 1, 1, self)
                spot = pygame.Rect(left_coord, size_coord)
                spot = spot.inflate(-8, -8)
                amt = 25
                if(self.is_playing[idx_bank][idx_slot]):
                    amt = 85
                if idx_bank == main_row and idx_slot >= first_col and idx_slot < last_col:
                    amt *= 3
                    relative_slot = idx_slot-first_col
                    if relative_slot % 3 == 0:
                        pygame.draw.rect(screen, (amt, amt, 0), spot)
                    elif relative_slot % 3 == 1:
                        pygame.draw.rect(screen, (0, amt, 0), spot)
                    else:
                        pygame.draw.rect(screen, (0, 0, amt), spot)
                else:
                    if idx_slot % 2 == 0:
                        pygame.draw.rect(screen, (amt, amt, amt), spot)
                    else:
                        pygame.draw.rect(
                            screen, (amt-10, amt-10, amt-10), spot)
        # if debug != None:
        #     debugtext = "box" + str(debug.center) + "sz"+str(debug.size)
        #     img = self.font.render(debugtext, True,  (200, 255, 200))
        #     screen.blit(img, (20, 20))

    def play(self, bank, slot):
        if self.is_playing[bank][slot]:
            return False

        chidx = slot % 8
        self.channels[chidx].play(self.sounds[bank][slot])
        self.is_playing[bank][slot] = True
        return True

    def stop(self, bank, slot):
        if self.is_playing[bank][slot]:
            chidx = slot % 8
            self.channels[chidx].stop()
            self.is_playing[bank][slot] = False

    def stop_all(self):
        for idx_bank in range(len(self.is_playing)):
            bank = self.sounds[idx_bank]
            for idx_slot in range(len(bank)):
                self.stop(idx_bank, idx_slot)

    def tick(self, delta):
        for idx_bank in range(len(self.is_playing)):
            bank = self.sounds[idx_bank]
            for idx_slot in range(len(bank)):
                if self.is_playing[idx_bank][idx_slot]:
                    chidx = idx_slot % 8
                    if not self.channels[chidx].get_busy():
                        self.stop(idx_bank, idx_slot)

        if not pygame.mixer.get_busy():
            self.stop_all()
