import pygame.mixer
from tools.constants import *
from tools.jsonManager import *


class Music:
    def __init__(self):
        self.music = "assets/music/Start music.mp3"
        self.volume = 100

    def record_music(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()

    @staticmethod
    def off_music():
        pygame.mixer.music.pause()

    @staticmethod
    def on_music():
        pygame.mixer.music.unpause()


class Effects:
    def __init__(self):
        self.volume = 100

        self.move_cursor_effect = pygame.mixer.Sound('assets/music/sound/movement cursor.wav')
        self.lay_out_letter_effect = pygame.mixer.Sound('assets/music/sound/lay out boxs.wav')
        self.accept_setting = pygame.mixer.Sound('assets/music/sound/accept setting.wav')
        self.open_new_page = pygame.mixer.Sound('assets/music/sound/open new page.wav')
        self.start_effect = pygame.mixer.Sound('assets/music/sound/start effect .wav')
        self.back_menu_effect = pygame.mixer.Sound('assets/music/sound/menu back sound.wav')
        self.menu_effect = pygame.mixer.Sound('assets/music/sound/menu sound.wav')
        self.paper_sound_var1 = pygame.mixer.Sound('assets/music/sound/turn the page.wav')
        self.paper_sound_var2 = pygame.mixer.Sound('assets/music/sound/turn the page2.wav')
        self.paper_sound_var3 = pygame.mixer.Sound('assets/music/sound/turn the page3.wav')

    def change_volume_effects(self, value: int):
        self.volume = value
        pygame.mixer.music.set_volume(self.volume)
        self.accept_setting.set_volume(self.volume)
        self.open_new_page.set_volume(self.volume)
        self.start_effect.set_volume(self.volume)
        self.back_menu_effect.set_volume(self.volume)
        self.menu_effect.set_volume(self.volume)
        self.paper_sound_var1.set_volume(self.volume)
        self.paper_sound_var2.set_volume(self.volume)
        self.paper_sound_var3.set_volume(self.volume)
