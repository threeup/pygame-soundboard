import pygame
from boss import BossCtrlr
from human import HumanCtrlr
from canvas import CanvasCtrlr
from midiboard import MidiBoardCtrlr
from music import MusicCtrlr
from const import SCREEN_WIDTH, SCREEN_HEIGHT




def main():
    '''main'''
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

        if human.duration[0] > 1 and not human.pressed[0]:
            print(human.duration[0])
            if human.duration[0] > 500:
                canvas.advance_row()
            else:
                canvas.slide_row() 
        else:
            if human.pressed[1]:
                (bank,slot)=canvas.get_current(0)
                music.play(bank,slot)
            if human.pressed[2]:
                (bank,slot)=canvas.get_current(1)
                music.play(bank,slot)
            if human.pressed[3]:
                (bank,slot)=canvas.get_current(2)
                music.play(bank,slot)

        canvas.draw(screen)
        human.draw(screen)
        midibo.draw(screen)
        music.draw(screen, canvas.get_current)

        pygame.display.update()

        human.post_tick()


if __name__ == "__main__":
    main()
