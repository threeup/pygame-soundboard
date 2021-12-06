import pygame
from boss import BossCtrlr
from human import HumanCtrlr
from canvas import CanvasCtrlr
from midiboard import MidiBoardCtrlr
from music import MusicCtrlr
from sparkle import Sparkle
from const import SCREEN_WIDTH, SCREEN_HEIGHT

from lib import center_to_draw

def main():
    '''main'''
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)
    pygame.init()
    pygame.fastevent.init()
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    joysticks = [pygame.joystick.Joystick(x) for x in range(joystick_count)]
    for j in range(joystick_count):
        joysticks[j].init()

    pygame.display.update()

    # controller
    music = MusicCtrlr()
    human = HumanCtrlr()
    boss = BossCtrlr()
    canvas = CanvasCtrlr(music)
    midibo = MidiBoardCtrlr()
    sparkles = []

    while boss.running:
        # Scan the buttons
        for event in pygame.event.get():
            boss.handle_event(event)
            human.handle_event(event)
            midibo.handle_event(event)

        delta = clock.tick(30)/1000.0

        canvas.tick(delta)
        human.tick(delta)
        midibo.tick(delta)
        music.tick(delta)
        for sparkle in sparkles:
            sparkle.tick(delta)
        sparkles = list(filter(lambda s: s.ttl>0, sparkles))
                

        if human.duration[0] > 1 and not human.pressed[0]:
            print(human.duration[0])
            if human.duration[0] > 500:
                canvas.advance_row()
                canvas.slide_row() 
            else:
                canvas.slide_row() 
        else:
            bank = None
            slot = None
            if human.pressed[1]:
                (bank,slot)=canvas.get_current(0)
            if human.pressed[2]:
                (bank,slot)=canvas.get_current(1)
            if human.pressed[3]:
                (bank,slot)=canvas.get_current(2)
                
            if bank is not None and slot is not None:
                launch = music.play(bank,slot)
                if launch:
                    pos = center_to_draw(
                        bank, slot, 1, 1, music)
                    s = Sparkle(pos,bank)
                    sparkles.append(s)

        canvas.drawbg(screen)
        musicbgrect =  pygame.Rect((0,0), (SCREEN_WIDTH, SCREEN_HEIGHT))
        musicbgsurf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        music.drawbg(musicbgsurf)
        screen.blit(musicbgsurf, musicbgrect)
        human.draw(screen)
        midibo.draw(screen)
        canvas.drawfg(screen)
        music.drawfg(screen, canvas.get_current)
        for sparkle in sparkles:
            sparkle.draw(screen)
            
        pygame.display.update()

        human.post_tick()


if __name__ == "__main__":
    main()
