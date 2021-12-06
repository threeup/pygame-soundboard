''' holds MidiboardCtrlr class '''
import pygame
import pygame.midi
from ctrlr import Ctrlr


class MidiBoardCtrlr(Ctrlr):
    '''
    A class which manipulates midi board
    '''

    def __init__(self):
        Ctrlr.__init__(self)
        self.time = 0
        self.key_velocities = {}
        # self.print_device_info()
        pygame.midi.init()
        input_id = pygame.midi.get_default_input_id()
        self.inpdevice = None
        if input_id >= 0:
            self.inpdevice = pygame.midi.Input(input_id)

    def print_device_info(self):
        pygame.midi.init()
        for i in range(pygame.midi.get_count()):
            r = pygame.midi.get_device_info(i)
            (interf, name, input, output, opened) = r

            in_out = ""
            if input:
                in_out = "(input)"
            if output:
                in_out = "(output)"

            print("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
                  (i, interf, name, opened, in_out))
        pygame.midi.quit()

    def handle_event(self, event):
        BLUE = (0,   0, 255)
        # if event.type == pygame.MIDIIN:
        #     if event.status == 144:
        #         # pygame.midi.midis2events.NOTE_ON:
        #         self.key_velocities.update({event.data1: event.data2})
        #     elif event.status == 128:
        #         # pygame.midi.midis2events.NOTE_OFF:
        #         self.key_velocities.pop(event.data1)

    def draw(self, screen):
        BLUE = (0,   0, 255)

    def tick(self, delta):
        self.time += delta*1000
        if self.inpdevice is not None and self.inpdevice.poll():
            midi_events = self.inpdevice.read(10)
            midi_evs = pygame.midi.midis2events(
                midi_events, self.inpdevice.device_id)
            for ev in midi_evs:
                pygame.fastevent.post(ev)
