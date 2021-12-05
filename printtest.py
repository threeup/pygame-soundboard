import pygame
from const import SCREEN_WIDTH, SCREEN_HEIGHT


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
    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 48)
    print("testing 1")
    img = font.render(sysfont, True,  (0, 55, 0))
    count = 0
    tick = 0
    while True:
        
        screen.blit(img, (20, 20))
        count += 1
        pygame.display.update()
        if count >= 1000:
            print("tick")
            print(tick)
            tick += 1
            count = 0

    
if __name__ == "__main__":
    main()
