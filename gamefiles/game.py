import random
import pygame.transform
from gamefiles.ui.menu import *
from tools.jsonManager import *
from tools.color import *
from tools.event import *
from tools.sound import *


class Game:
    def __init__(self):
        pygame.init()

        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        pygame.display.set_caption("Scrabble-Game")

        self.font_size, self.font_size_Upper = 18, 20
        self.running = True

        self.event = Event(self)
        self.controller_event = ControllerEvent(self)

        self.color = Color()
        self.white, self.black = self.color.white, self.color.black
        # self.save_settings = SaveSettings(self)

        self.d_wide, self.d_high = 1920, 1080
        self.display = pygame.Surface((self.d_wide, self.d_high))
        self.screen = pygame.display.set_mode((self.d_wide, self.d_high))

        self.json_manager = JsonSettingsManager()

        self.splash_screen = SplashScreenPage(self, self.event, self.controller_event)
        self.main_menu = MainMenu(self, self.event, self.controller_event)
        self.curr_menu = self.splash_screen

        self.language = 'en'

        self.volume_pin1_w, self.volume_pin1_h = (self.d_wide / 2) + 50, (self.d_high / 2) - 160
        self.volume_pin2_w, self.volume_pin2_h = (self.d_wide / 2) + 50, (self.d_high / 2) - 65
        self.volume_music, self.volume_effects = 1, 1

        self.music = Music()
        self.music.record_music()

        self.letter_list_image = [pygame.image.load(f"assets/jpg/letters/{j}.jpg") for j in range(27)]
        self.j = 1
        for j in range(27):
            self.letter_list_image[j] = pygame.transform.scale(self.letter_list_image[j], (50, 50))

        # lamp animation
        self.animation1 = [pygame.image.load(f"assets/animation/Light animation/{i}.jpg") for i in range(0, 21)]
        self.i = 1
        for i in range(20):
            self.animation1[i] = pygame.transform.scale(self.animation1[i], (250, 250))

    @staticmethod
    def restart_game():
        pygame.display.quit()
        pygame.display.init()

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font("Font.ttf", size)
        # font = pygame.font.Font("Font.ttf", size)
        text_sur = font.render(text, True, self.white)
        rect = text_sur.get_rect()
        rect.center = (x, y)
        self.display.blit(text_sur, rect)
