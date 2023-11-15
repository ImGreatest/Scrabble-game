import sys
import math
from itertools import permutations
import pygame


class Menu:
    def __init__(self, game, event, controller):
        self.game = game
        self.event = event
        self.controller = controller

        self.middle_w, self.middle_h, self.full_w, self.full_h, self.go_display = self.game.d_wide / 2, self.game.d_high / 2, self.game.d_wide, self.game.d_high, True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.label_rules_x, self.label_rules_y = self.middle_w, self.middle_h - 400
        self.middle_b_x, self.middle_b_y = self.middle_w, self.middle_h + 350
        self.left_arrow_x, self.left_arrow_y = self.middle_w - 700, self.middle_h + 350
        self.right_arrow_x, self.right_arrow_y = self.middle_w + 700, self.middle_h + 350

        pygame.mouse.set_visible(True)

    def go_cursor(self):
        self.game.draw_text('*', 17, self.cursor_rect.x, self.cursor_rect.y)

    def b_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()

    def noheap(self):
        status = False
        self.cur_x += 10
        self.cur_y += 4
        new_list = [self.game.pos_list[d: d + 2] for d in range(0, len(self.game.pos_list), 2)]
        self.pos_with_new_list = new_list
        j, i, b = -1, 0, math.trunc(len(self.game.pos_list) / 2)
        while i != b:
            i += 1
            j += 1
            if len(new_list) >= 1:
                if new_list[j:i] == [[self.cur_x, self.cur_y]]:
                    status = True
                    break
        return status


# First Page
class SplashScreenPage(Menu):
    def __init__(self, game, event, controller):
        Menu.__init__(self, game, event, controller)
        self.i = 1
        self.splash_screen_label_size = 25

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.controller.movement(False)
            self.action_movement()
            self.game.display.fill(self.game.black)
            self.game.draw_text('SCRABBLE', self.splash_screen_label_size, self.middle_w, self.middle_h)
            if self.game.language == 'en':
                self.game.draw_text('press start', self.game.font_size, self.middle_b_x, self.middle_b_y)
            self.game.display.blit(self.game.animation1[self.i], (self.middle_w - 128, self.middle_h - 300))
            self.i += 1
            if self.i == 20:
                self.i = 6
            self.b_screen()
            pygame.time.wait(20)

    def action_movement(self):
        if self.controller.return_button or self.controller.space_button:
            
            self.game.curr_menu = self.game.main_menu
            self.go_display = False
        if self.controller.delete_button:
            sys.exit()


# Page main menu
class MainMenu(Menu):
    def __init__(self, game, event, keyboard):
        Menu.__init__(self, game, event, keyboard)
        self.title = "Start"
        self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.controller.movement(False)
            # self.check_movement()
            self.game.display.fill(self.game.black)
            self.game.draw_text('Main Menu', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
            self.game.draw_text("Start", self.game.font_size, self.middle_w + 20, self.middle_h)
            self.game.draw_text("Settings", self.game.font_size, self.middle_w + 20, self.middle_h + 40)
            self.game.draw_text("Rules", self.game.font_size, self.middle_w + 20, self.middle_h + 80)
            self.game.draw_text("Records", self.game.font_size, self.middle_w + 20, self.middle_h + 120)
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_up:
            if self.title == 'Start':
                self.title = 'Records'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 120)
            elif self.title == 'Records':
                self.title = 'Rules'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 80)
            elif self.title == 'Rules':
                self.title = 'Settings'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 40)
            elif self.title == 'Settings':
                self.title = 'Start'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)
            self.game.menu_effect.play()

        elif self.game.arrow_down:
            if self.title == 'Start':
                self.title = 'Settings'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 40)
            elif self.title == 'Settings':
                self.title = 'Rules'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 80)
            elif self.title == 'Rules':
                self.title = 'Records'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 120)
            elif self.title == 'Records':
                self.title = 'Start'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.start_b or self.game.space_b:
            if self.title == 'Start':
                self.game.random_letter(7)
                # self.game.curr_menu = self.game.start
            elif self.title == 'Settings':
                self.game.curr_menu = self.game.settings
            elif self.title == 'Rules':
                self.game.curr_menu = self.game.rules
            elif self.title == 'Records':
                self.game.curr_menu = self.game.record_page
            self.game.open_new_page.play()
            self.go_display = False
        if self.game.exit_b:
            self.exit_status()


# Page settings
class SettingsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'music'
        self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)
        self.i_music = pygame.image.load('assets/jpg/image/single music.png').convert_alpha()
        self.i_o_s = pygame.image.load('assets/jpg/image/single o_s.png').convert_alpha()
        self.i_back = pygame.image.load('assets/jpg/image/single back arrow.png').convert_alpha()
        self.i_exit = pygame.image.load('assets/jpg/image/single next arrow.png').convert_alpha()
        self.i_music_active = pygame.image.load('assets/jpg/active image/music active.png').convert_alpha()
        self.i_o_s_active = pygame.image.load('assets/jpg/active image/o_s active.png').convert_alpha()
        self.i_back_active = pygame.image.load('assets/jpg/active image/back arrow active.png').convert_alpha()
        self.i_next_active = pygame.image.load('assets/jpg/active image/next arrow active.png').convert_alpha()
        self.i_music = pygame.transform.scale(self.i_music, (45, 45))
        self.i_o_s = pygame.transform.scale(self.i_o_s, (50, 50))
        self.i_back = pygame.transform.scale(self.i_back, (60, 60))
        self.i_exit = pygame.transform.scale(self.i_exit, (100, 100))
        self.i_music_active = pygame.transform.scale(self.i_music_active, (45, 45))
        self.i_o_s_active = pygame.transform.scale(self.i_o_s_active, (50, 50))
        self.i_back_active = pygame.transform.scale(self.i_back_active, (60, 60))
        self.i_next_active = pygame.transform.scale(self.i_next_active, (100, 100))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.game.movement_button()
            self.movement_in_menu()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.draw_text("Settings menu", self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.draw_text("music", self.game.font_size, self.middle_w, self.middle_h)
                self.game.draw_text("other", self.game.font_size, self.middle_w, self.middle_h + 40)
                self.game.draw_text('back', self.game.font_size, self.middle_w, self.middle_h + 80)
                self.game.draw_text("exit", self.game.font_size, self.middle_w, self.middle_h + 120)
            self.game.display.blit(self.i_music, (self.middle_w - 95, self.middle_h - 20))
            self.game.display.blit(self.i_o_s, (self.middle_w - 95, self.middle_h + 20))
            self.game.display.blit(self.i_back, (self.middle_w - 100, self.middle_h + 50))
            self.game.display.blit(self.i_exit, (self.middle_w - 120, self.middle_h + 70))
            if self.title == 'music':
                self.game.display.blit(self.i_music_active, (self.middle_w - 95, self.middle_h - 20))
            elif self.title == 'other':
                self.game.display.blit(self.i_o_s_active, (self.middle_w - 95, self.middle_h + 20))
            elif self.title == 'back':
                self.game.display.blit(self.i_back_active, (self.middle_w - 100, self.middle_h + 50))
            else:
                self.game.display.blit(self.i_next_active, (self.middle_w - 120, self.middle_h + 70))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_down:
            if self.title == 'music':
                self.title = 'other'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 40)
            elif self.title == 'other':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 80)
            elif self.title == 'back':
                self.title = 'exit'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 120)
            elif self.title == 'exit':
                self.title = 'music'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)
            self.game.menu_effect.play()

        elif self.game.arrow_up:
            if self.title == 'music':
                self.title = 'exit'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 120)
            elif self.title == 'exit':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 80)
            elif self.title == 'back':
                self.title = 'other'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 40)
            elif self.title == 'other':
                self.title = 'music'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)
            self.game.menu_effect.play()

    def check_movement(self):
        if self.game.start_b or self.game.space_b:
            if self.title == 'music':
                self.game.open_new_page.play()
                self.game.curr_menu = self.game.music_menu
            elif self.title == 'exit':
                self.exit_status()
            elif self.title == 'other':
                self.game.open_new_page.play()
                self.game.curr_menu = self.game.other_settings
            elif self.title == 'back':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
        self.go_display = False
        if self.game.exit_b:
            self.exit_status()
        if self.game.esc_b:
            self.game.back_menu_effect.play()
            self.game.curr_menu = self.game.main_menu


# Page other settings
class OtherSettings(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'volume music'
        self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 150)
        self.volume_line = pygame.image.load('assets/jpg/Sound.png').convert_alpha()
        self.volume_pin = pygame.image.load('assets/jpg/Pin_sound.png').convert_alpha()
        self.volume_pin = pygame.transform.scale(self.volume_pin, (125, 125))
        self.full_volume = pygame.image.load('assets/jpg/image/single full volume.png').convert_alpha()
        self.empty_volume = pygame.image.load('assets/jpg/image/single empty volume.png').convert_alpha()
        self.third_volume = pygame.image.load('assets/jpg/image/single third volume.png').convert_alpha()
        self.half_volume = pygame.image.load('assets/jpg/image/single half volume.png').convert_alpha()
        self.i_back = pygame.image.load('assets/jpg/image/single back arrow.png').convert_alpha()
        self.i_language = pygame.image.load('assets/jpg/image/single language.png').convert_alpha()
        self.full_volume_active = pygame.image.load(
            'assets/jpg/active image/full volume active.png').convert_alpha()
        self.trird_volume_active = pygame.image.load(
            'assets/jpg/active image/third volume active.png').convert_alpha()
        self.half_volume_active = pygame.image.load(
            'assets/jpg/active image/half volume active.png').convert_alpha()
        self.empty_volume_active = pygame.image.load(
            'assets/jpg/active image/empty volume active.png').convert_alpha()
        self.i_back_active = pygame.image.load('assets/jpg/active image/back arrow active.png').convert_alpha()
        self.i_language_active = pygame.image.load('assets/jpg/active image/language active.png').convert_alpha()
        self.full_volume = pygame.transform.scale(self.full_volume, (50, 50))
        self.empty_volume = pygame.transform.scale(self.empty_volume, (50, 50))
        self.trird_volume = pygame.transform.scale(self.third_volume, (50, 50))
        self.half_volume = pygame.transform.scale(self.half_volume, (50, 50))
        self.i_back = pygame.transform.scale(self.i_back, (60, 60))
        self.i_language = pygame.transform.scale(self.i_language, (60, 60))
        self.i_back_active = pygame.transform.scale(self.i_back_active, (60, 60))
        self.i_language_active = pygame.transform.scale(self.i_language_active, (60, 60))
        self.full_volume_active = pygame.transform.scale(self.full_volume_active, (50, 50))
        self.empty_volume_active = pygame.transform.scale(self.empty_volume_active, (50, 50))
        self.trird_volume_active = pygame.transform.scale(self.trird_volume_active, (50, 50))
        self.half_volume_active = pygame.transform.scale(self.half_volume_active, (50, 50))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_menu()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.draw_text('Other settings', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.draw_text('volume music', self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.draw_text('volume effects', self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.draw_text('language en', self.game.font_size, self.middle_w, self.middle_h + 50)
                self.game.draw_text('back', self.game.font_size, self.middle_w, self.middle_h + 100)
            self.game.display.blit(self.volume_line, (self.middle_w - 130, self.middle_h - 185))
            self.game.display.blit(self.volume_pin, (self.game.volume_pin1_w, self.game.volume_pin1_h))
            self.game.display.blit(self.volume_line, (self.middle_w - 130, self.middle_h - 90))
            self.game.display.blit(self.volume_pin, (self.game.volume_pin2_w, self.game.volume_pin2_h))
            self.game.display.blit(self.i_language, (self.middle_w - 130, self.middle_h + 20))
            self.game.display.blit(self.i_back, (self.middle_w - 130, self.middle_h + 65))
            if self.title == 'volume music':
                if 0.56 <= self.game.volume_music <= 1:
                    self.game.display.blit(self.full_volume_active, (self.middle_w - 130, self.middle_h - 175))
                elif 0.23 <= self.game.volume_music < 0.56:
                    self.game.display.blit(self.half_volume_active, (self.middle_w - 130, self.middle_h - 175))
                elif 0 <= self.game.volume_music < 0.23:
                    self.game.display.blit(self.trird_volume_active, (self.middle_w - 130, self.middle_h - 175))
                elif self.game.volume_music < 0:
                    self.game.display.blit(self.empty_volume_active, (self.middle_w - 130, self.middle_h - 175))
            elif not self.title == 'volume music':
                if 0.56 <= self.game.volume_music <= 1:
                    self.game.display.blit(self.full_volume, (self.middle_w - 130, self.middle_h - 175))
                elif 0.23 <= self.game.volume_music < 0.56:
                    self.game.display.blit(self.half_volume, (self.middle_w - 130, self.middle_h - 175))
                elif 0 <= self.game.volume_music < 0.23:
                    self.game.display.blit(self.trird_volume, (self.middle_w - 130, self.middle_h - 175))
                elif self.game.volume_music < 0:
                    self.game.display.blit(self.empty_volume, (self.middle_w - 130, self.middle_h - 175))
            if self.title == 'volume effects':
                if 0.56 <= self.game.volume_effects <= 1:
                    self.game.display.blit(self.full_volume_active, (self.middle_w - 130, self.middle_h - 75))
                elif 0.23 <= self.game.volume_effects < 0.56:
                    self.game.display.blit(self.half_volume_active, (self.middle_w - 130, self.middle_h - 75))
                elif 0 <= self.game.volume_effects < 0.23:
                    self.game.display.blit(self.trird_volume_active, (self.middle_w - 130, self.middle_h - 75))
                elif self.game.volume_effects < 0:
                    self.game.display.blit(self.empty_volume_active, (self.middle_w - 130, self.middle_h - 75))
            elif not self.title == 'volume effects':
                if 0.56 <= self.game.volume_effects <= 1:
                    self.game.display.blit(self.full_volume, (self.middle_w - 130, self.middle_h - 75))
                elif 0.23 <= self.game.volume_effects < 0.56:
                    self.game.display.blit(self.half_volume, (self.middle_w - 130, self.middle_h - 75))
                elif 0 <= self.game.volume_effects < 0.23:
                    self.game.display.blit(self.trird_volume, (self.middle_w - 130, self.middle_h - 75))
                elif self.game.volume_effects < 0:
                    self.game.display.blit(self.empty_volume, (self.middle_w - 130, self.middle_h - 75))
            if self.title == 'language en':
                self.game.display.blit(self.i_language_active, (self.middle_w - 130, self.middle_h + 20))
            if self.title == 'back':
                self.game.display.blit(self.i_back_active, (self.middle_w - 130, self.middle_h + 65))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_up:
            if self.title == 'volume music':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 100)
            elif self.title == 'back':
                self.title = 'language en'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 50)
            elif self.title == 'language en':
                self.title = 'volume effects'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 50)
            elif self.title == 'volume effects':
                self.title = 'volume music'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 150)
            self.game.menu_effect.play()

        elif self.game.arrow_down:
            if self.title == 'volume music':
                self.title = 'volume effects'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 50)
            elif self.title == 'volume effects':
                self.title = 'language en'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 50)
            elif self.title == 'language en':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 100)
            elif self.title == 'back':
                self.title = 'volume music'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 150)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.start_b or self.game.space_b:
            if self.title == 'back':
                self.game.save_settings.save()
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.settings
                self.go_display = False
            if self.title == 'language en':
                self.game.accept_setting.play()
                if self.game.language == 'en':
                    self.game.language = 'ru'
                elif self.game.language == 'ru':
                    self.game.language = 'en'
        if self.game.arrow_left:
            if self.title == 'volume music':
                if self.game.volume_music > 0 and self.game.volume_pin1_w > 0:
                    self.game.accept_setting.play()
                    self.game.volume_music -= 0.1
                    self.game.volume_pin1_w -= 17.7
                    pygame.mixer.music.set_volume(self.game.volume_music)
                    # self.Game.save_settings.save()
            if self.title == 'volume effects':
                if self.game.volume_effects > 0 and self.game.volume_pin2_w > 0:
                    self.game.accept_setting.play()
                    self.game.volume_effects -= 0.1
                    self.game.volume_pin2_w -= 17.7
                    self.game.accept_setting.set_volume(self.game.volume_effects)
                    self.game.open_new_page.set_volume(self.game.volume_effects)
                    self.game.start_effect.set_volume(self.game.volume_effects)
                    self.game.back_menu_effect.set_volume(self.game.volume_effects)
                    self.game.menu_effect.set_volume(self.game.volume_effects)
                    self.game.paper_sound_var1.set_volume(self.game.volume_effects)
                    self.game.paper_sound_var2.set_volume(self.game.volume_effects)
                    self.game.paper_sound_var3.set_volume(self.game.volume_effects)
                    # self.Game.save_settings.save()
        if self.game.arrow_right:
            if self.title == 'volume music':
                if self.game.volume_music < 1 and not self.game.volume_music > 1:
                    self.game.accept_setting.play()
                    self.game.volume_music += 0.1
                    self.game.volume_pin1_w += 17.7
                    pygame.mixer.music.set_volume(self.game.volume_music)
                    self.game.save_settings.save()
            if self.title == 'volume effects' and not self.game.volume_music > 1:
                if self.game.volume_effects < 1:
                    self.game.accept_setting.play()
                    self.game.volume_effects += 0.1
                    self.game.volume_pin2_w += 17.7
                    self.game.accept_setting.set_volume(self.game.volume_effects)
                    self.game.open_new_page.set_volume(self.game.volume_effects)
                    self.game.start_effect.set_volume(self.game.volume_effects)
                    self.game.back_menu_effect.set_volume(self.game.volume_effects)
                    self.game.menu_effect.set_volume(self.game.volume_effects)
                    self.game.paper_sound_var1.set_volume(self.game.volume_effects)
                    self.game.paper_sound_var2.set_volume(self.game.volume_effects)
                    self.game.paper_sound_var3.set_volume(self.game.volume_effects)
                    # self.Game.save_settings.save()
        if self.game.esc_b:
            self.game.back_menu_effect.play()
            self.game.save_settings.save()
            self.game.curr_menu = self.game.settings
            self.go_display = False
        if self.game.exit_b:
            self.game.save_settings.save()
            self.exit_status()


# Page with Records
class RecordPage(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'back'
        self.cursor_rect.midtop = (self.middle_w - (+ 100), self.middle_h + 100)
        self.i_back_active = pygame.image.load('assets/jpg/active image/back arrow active.png').convert_alpha()
        self.i_back_active = pygame.transform.scale(self.i_back_active, (60, 60))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.draw_text('records', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.draw_text(('1 ' + f'{self.game.record}'), self.game.font_size, self.middle_w,
                                    self.middle_h - 150)
                self.game.draw_text(('2 ' + f'{self.game.record2}'), self.game.font_size, self.middle_w,
                                    self.middle_h - 100)
                self.game.draw_text(('3 ' + f'{self.game.record3}'), self.game.font_size, self.middle_w,
                                    self.middle_h - 50)
                self.game.draw_text(('4 ' + f'{self.game.record4}'), self.game.font_size, self.middle_w, self.middle_h)
                self.game.draw_text(('5 ' + f'{self.game.record5}'), self.game.font_size, self.middle_w,
                                    self.middle_h + 50)
                self.game.draw_text('back', self.game.font_size, self.middle_w, self.middle_h + 100)
            self.game.display.blit(self.i_back_active, (self.middle_w - 100, self.middle_h + 70))
            self.go_cursor()
            self.b_screen()

    def check_movement(self):
        if self.game.esc_b:
            self.game.curr_menu = self.game.settings
            self.game.back_menu_effect.play()
            self.go_display = False
        if self.game.exit_b:
            self.exit_status()
        if self.game.start_b or self.game.space_b:
            if self.title == 'back':
                self.game.curr_menu = self.game.main_menu
                self.game.back_menu_effect.play()
                self.go_display = False


# Music Page
class MusicPage(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'Starter'
        self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 100)
        self.music_i = pygame.image.load('assets/jpg/image/single sound.png').convert_alpha()
        self.music_i_active = pygame.image.load('assets/jpg/active image/sound active.png').convert_alpha()
        self.back_i = pygame.image.load('assets/jpg/image/single back arrow.png').convert_alpha()
        self.back_active = pygame.image.load('assets/jpg/active image/back arrow active.png').convert_alpha()
        self.full_music = pygame.image.load('assets/jpg/image/single full volume.png').convert_alpha()
        self.full_music_active = pygame.image.load(
            'assets/jpg/active image/full volume active.png').convert_alpha()
        self.off_music = pygame.image.load('assets/jpg/image/single empty volume.png').convert_alpha()
        self.off_music_active = pygame.image.load(
            'assets/jpg/active image/empty volume active.png').convert_alpha()
        self.full_music = pygame.transform.scale(self.full_music, (50, 50))
        self.full_music_active = pygame.transform.scale(self.full_music_active, (50, 50))
        self.off_music = pygame.transform.scale(self.off_music, (50, 50))
        self.off_music_active = pygame.transform.scale(self.off_music_active, (50, 50))
        self.music_i = pygame.transform.scale(self.music_i, (60, 60))
        self.music_i_active = pygame.transform.scale(self.music_i_active, (60, 60))
        self.back_i = pygame.transform.scale(self.back_i, (60, 60))
        self.back_active = pygame.transform.scale(self.back_active, (60, 60))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_menu()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.draw_text("Music", self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.draw_text("Starter", self.game.font_size, self.middle_w, self.middle_h - 100)
                self.game.draw_text("theme 1", self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.draw_text("theme 2", self.game.font_size, self.middle_w, self.middle_h)
                self.game.draw_text("theme 3", self.game.font_size, self.middle_w, self.middle_h + 50)
                self.game.draw_text("off * on music", self.game.font_size, self.middle_w, self.middle_h + 100)
                self.game.draw_text("back", self.game.font_size, self.middle_w, self.middle_h + 150)
            if not self.title == 'back':
                self.game.display.blit(self.back_i, (self.middle_w - 130, self.middle_h + 117))
            else:
                self.game.display.blit(self.back_active, (self.middle_w - 130, self.middle_h + 117))
            if not self.title == 'Starter':
                self.game.display.blit(self.music_i, (self.middle_w - 140, self.middle_h - 130))
            else:
                self.game.display.blit(self.music_i_active, (self.middle_w - 140, self.middle_h - 130))
            if not self.title == 'theme 1':
                self.game.display.blit(self.music_i, (self.middle_w - 140, self.middle_h - 82))
            else:
                self.game.display.blit(self.music_i_active, (self.middle_w - 140, self.middle_h - 82))
            if not self.title == 'theme 2':
                self.game.display.blit(self.music_i, (self.middle_w - 140, self.middle_h - 32))
            else:
                self.game.display.blit(self.music_i_active, (self.middle_w - 140, self.middle_h - 32))
            if not self.title == 'theme 3':
                self.game.display.blit(self.music_i, (self.middle_w - 140, self.middle_h + 18))
            else:
                self.game.display.blit(self.music_i_active, (self.middle_w - 140, self.middle_h + 18))
            if not self.title == 'off * on music':
                if not self.game.music:
                    self.game.display.blit(self.off_music, (self.middle_w - 130, self.middle_h + 70))
                else:
                    self.game.display.blit(self.full_music, (self.middle_w - 130, self.middle_h + 70))
            else:
                if self.game.music:
                    self.game.display.blit(self.full_music_active, (self.middle_w - 130, self.middle_h + 70))
                else:
                    self.game.display.blit(self.off_music_active, (self.middle_w - 130, self.middle_h + 70))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_down:
            if self.title == 'Starter':
                self.title = 'theme 1'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 50)
            elif self.title == 'theme 1':
                self.title = 'theme 2'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h)
            elif self.title == 'theme 2':
                self.title = 'theme 3'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 50)
            elif self.title == 'theme 3':
                self.title = 'off * on music'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 100)
            elif self.title == 'off * on music':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 150)
            elif self.title == 'back':
                self.title = 'Starter'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 100)
            self.game.menu_effect.play()

        elif self.game.arrow_up:
            if self.title == 'Starter':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 150)
            elif self.title == 'back':
                self.title = 'off * on music'
                self.cursor_rect.midtop = (self.middle_w + (-125), self.middle_h + 100)
            elif self.title == 'off * on music':
                self.title = 'theme 3'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h + 50)
            elif self.title == 'theme 3':
                self.title = 'theme 2'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h)
            elif self.title == 'theme 2':
                self.title = 'theme 1'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 50)
            elif self.title == 'theme 1':
                self.title = 'Starter'
                self.cursor_rect.midtop = (self.middle_w + (- 125), self.middle_h - 100)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.exit_b:
            self.game.save_settings.save()
            self.exit_status()
        if self.game.esc_b:
            self.game.save_settings.save()
            self.game.back_menu_effect.play()
            self.game.curr_menu = self.game.settings
            self.go_display = False
        if self.game.start_b or self.game.space_b:
            if self.title == 'back':
                self.game.back_menu_effect.play()
                self.game.save_settings.save()
                self.game.curr_menu = self.game.settings
                self.go_display = False
            elif self.title == 'off * on music':
                self.game.accept_setting.play()
                self.music_status()
            elif self.title == 'Starter':
                self.game.accept_setting.play()
                self.game.p_music = 'music/Start music.mp3'
                pygame.mixer.music.load('assets/music/Start music.mp3')
                pygame.mixer.music.play()
                self.game.music = True
            elif self.title == 'theme 1':
                self.game.accept_setting.play()
                self.game.p_music = 'music/Theme 1.mp3'
                pygame.mixer.music.load('assets/music/Theme 1.mp3')
                pygame.mixer.music.play()
                self.game.music = True
            elif self.title == 'theme 2':
                self.game.accept_setting.play()
                self.game.p_music = 'music/Theme 2.mp3'
                pygame.mixer.music.load('assets/music/Theme 2.mp3')
                pygame.mixer.music.play()
                self.game.music = True
            elif self.title == 'theme 3':
                self.game.accept_setting.play()
                self.game.p_music = 'music/Theme 3.mp3'
                pygame.mixer.music.load('assets/music/Theme 3.mp3')
                pygame.mixer.music.play()
                self.game.music = True

    def music_status(self):
        if self.game.music:
            self.game.music = False
            pygame.mixer.music.pause()
        else:
            self.game.music = True
            pygame.mixer.music.unpause()
        pygame.time.delay(100)


# Page of rules 1 - rules the Game
class Rules(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'go menu'
        self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill((0, 0, 0))
            if self.game.language == 'en':
                self.game.draw_text("Rules", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.draw_text(
                    "The playing field consists of 15 x 15 that is 225 squares on which the participants "
                    "of the Game lay out letters",
                    self.game.font_size, self.middle_w, self.middle_h - 350)
                self.game.draw_text(
                    "thereby making words At the beginning of the Game each player receives 7 random letters",
                    self.game.font_size, self.middle_w, self.middle_h - 300)
                self.game.draw_text("( there are 104 in total in the Game 131 in Scrabble )",
                                    self.game.font_size, self.middle_w, self.middle_h - 250)
                self.game.draw_text("Through the central cell of the playing field the first word is laid out"
                                    " horizontally or vertically", self.game.font_size, self.middle_w,
                                    self.middle_h - 200)
                self.game.draw_text("then the next player can add the word ( to the intersection ) from their letters",
                                    self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.draw_text("Words are laid out either from left to right or from top to bottom",
                                    self.game.font_size, self.middle_w, self.middle_h - 100)
                self.game.draw_text(
                    "Each player aims to win the Game by creating more words based on the available letter "
                    "tiles to score more points",
                    self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.draw_text("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
                self.game.draw_text("go menu", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
            if self.title != 'go menu':
                self.game.display.blit(self.up_menu, (self.middle_w - 825, self.middle_h + 300))
            else:
                self.game.display.blit(self.up_menu_active, (self.middle_w - 825, self.middle_h + 300))
            if self.title != 'next':
                self.game.display.blit(self.next, (self.middle_w + 585, self.middle_h + 300))
            else:
                self.game.display.blit(self.next_active, (self.middle_w + 585, self.middle_h + 300))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.esc_b:
            self.game.back_menu_effect.play()
            self.game.curr_menu = self.game.main_menu
            self.go_display = False
        elif self.game.arrow_right:
            if self.title == 'go menu':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()
        elif self.game.arrow_left:
            if self.title == 'go menu':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.start_b or self.game.space_b:
            if self.title == 'go menu':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
            elif self.title == 'next':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules_page2

            self.go_display = False
        if self.game.exit_b:
            self.exit_status()


# Page of rules 2 - Glossary
class RulesPage2(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'back'
        self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_menu()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.draw_text("Glossary", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.draw_text(
                    "It is allowed to use all the words given in the standard dictionary of the language "
                    "with the exception of *", self.game.font_size, self.middle_w, self.middle_h - 400)
                self.game.draw_text("words that are written with capital letters",
                                    self.game.font_size, self.middle_w - 335, self.middle_h - 350)
                self.game.draw_text("abbreviation", self.game.font_size, self.middle_w - 595, self.middle_h - 300)
                self.game.draw_text("words that are written with an apostrophe",
                                    self.game.font_size, self.middle_w - 350, self.middle_h - 250)
                self.game.draw_text("words that are written with a hyphen",
                                    self.game.font_size, self.middle_w - 394, self.middle_h - 200)
                self.game.draw_text("If a word does not have a nominative case or a singular number it is allowed to "
                                    "use this word in any case or number",
                                    self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.draw_text("Do not use a dictionary to look up words",
                                    self.game.font_size, self.middle_w - 530, self.middle_h - 50)
                self.game.draw_text("Dictionary is allowed only in the case of checking the existence of an "
                                    "already composed word", self.game.font_size, self.middle_w - 100, self.middle_h)
                self.game.draw_text("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.draw_text("go menu", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.draw_text("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
            if self.title != 'go menu':
                self.game.display.blit(self.up_menu, (self.middle_w - 125, self.middle_h + 300))
            else:
                self.game.display.blit(self.up_menu_active, (self.middle_w - 125, self.middle_h + 300))
            if self.title != 'next':
                self.game.display.blit(self.next, (self.middle_w + 585, self.middle_h + 300))
            else:
                self.game.display.blit(self.next_active, (self.middle_w + 585, self.middle_h + 300))
            if self.title != 'back':
                self.game.display.blit(self.back, (self.middle_w - 800, self.middle_h + 315))
            else:
                self.game.display.blit(self.back_active, (self.middle_w - 800, self.middle_h + 315))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_right:
            if self.title == 'back':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 350)
            elif self.title == 'go menu':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()
        elif self.game.arrow_left:
            if self.title == 'back':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 350)
            elif self.title == 'go menu':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.start_b or self.game.space_b:
            if self.title == 'back':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules
            elif self.title == 'next':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules_page3
            elif self.title == 'go menu':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
            self.go_display = False
        if self.game.esc_b:
            self.game.random_choose_sound()
            self.game.curr_menu = self.game.rules
            self.go_display = False
        if self.game.exit_b:
            self.exit_status()


# Page of rules 3 - Game Process
class RulesPage3(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'back'
        self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_menu()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.draw_text("Game process", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.draw_text("* At the beginning of the Game everyone is given 7 tiles "
                                    "Only one word is allowed per turn",
                                    self.game.font_size, self.middle_w - 100, self.middle_h - 400)
                self.game.draw_text("Each new word must touch or have a common letter ( or letters ) "
                                    "with previously composed words", self.game.font_size, self.middle_w - 80,
                                    self.middle_h - 350)
                self.game.draw_text("Words should be read from left to right ( horizontally ) and from "
                                    "top to bottom ( vertically )",
                                    self.game.font_size, self.middle_w - 117, self.middle_h - 300)
                self.game.draw_text("* The first composed word must go through the central cell",
                                    self.game.font_size, self.middle_w - 410, self.middle_h - 200)
                self.game.draw_text("* If the player does not want or cannot make a single word he has the right "
                                    "to change any number of his letters", self.game.font_size, self.middle_w,
                                    self.middle_h - 100)
                self.game.draw_text("* Any sequence of letters horizontally and vertically must be a word",
                                    self.game.font_size, self.middle_w - 335, self.middle_h)
                self.game.draw_text("* After each move you need to get new letters up to seven",
                                    self.game.font_size, self.middle_w - 430, self.middle_h + 100)
                self.game.draw_text("* If a player has used all seven tiles during a turn then an "
                                    "additional 50 points are awarded to him",
                                    self.game.font_size, self.middle_w - 105, self.middle_h + 200)
                self.game.draw_text("* The Game ends if you run out of chips in your hand and there are no "
                                    "more chips to draw",
                                    self.game.font_size, self.middle_w - 200, self.middle_h + 270)
                self.game.draw_text("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.draw_text("go menu", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.draw_text("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
            if self.title != 'go menu':
                self.game.display.blit(self.up_menu, (self.middle_w - 125, self.middle_h + 300))
            else:
                self.game.display.blit(self.up_menu_active, (self.middle_w - 125, self.middle_h + 300))
            if self.title != 'next':
                self.game.display.blit(self.next, (self.middle_w + 585, self.middle_h + 300))
            else:
                self.game.display.blit(self.next_active, (self.middle_w + 585, self.middle_h + 300))
            if self.title != 'back':
                self.game.display.blit(self.back, (self.middle_w - 800, self.middle_h + 315))
            else:
                self.game.display.blit(self.back_active, (self.middle_w - 800, self.middle_h + 315))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_right:
            if self.title == 'back':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 350)
            elif self.title == 'go menu':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()
        elif self.game.arrow_left:
            if self.title == 'back':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 350)
            elif self.title == 'go menu':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.start_b or self.game.space_b:
            if self.title == 'back':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules_page2
            elif self.title == 'next':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules_page4
            elif self.title == 'go menu':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
        self.go_display = False
        if self.game.esc_b:
            self.game.random_choose_sound()
            self.game.curr_menu = self.game.rules_page2
            self.go_display = False
        if self.game.exit_b:
            self.exit_status()


# Page of rules 4 - Tile Value
class RulesPage4(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'back'
        self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_w + 350)
        self.letters = pygame.image.load('assets/jpg/count letters.png').convert_alpha()

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_menu()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            self.game.display.blit(self.letters, (self.middle_w - 300, self.middle_h - 400))
            if self.game.language == 'en':
                self.game.draw_text("Chip distribution and letter values", self.game.font_size_Upper, self.middle_w,
                                    self.middle_h - 400)
                self.game.draw_text("go menu", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.draw_text("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
                self.game.draw_text("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
            if self.title != 'go menu':
                self.game.display.blit(self.up_menu, (self.middle_w - 125, self.middle_h + 300))
            else:
                self.game.display.blit(self.up_menu_active, (self.middle_w - 125, self.middle_h + 300))
            if self.title != 'next':
                self.game.display.blit(self.next, (self.middle_w + 585, self.middle_h + 300))
            else:
                self.game.display.blit(self.next_active, (self.middle_w + 585, self.middle_h + 300))
            if self.title != 'back':
                self.game.display.blit(self.back, (self.middle_w - 800, self.middle_h + 315))
            else:
                self.game.display.blit(self.back_active, (self.middle_w - 800, self.middle_h + 315))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_right:
            if self.title == 'back':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 350)
            elif self.title == 'go menu':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()
        elif self.game.arrow_left:
            if self.title == 'back':
                self.title = 'next'
                self.cursor_rect.midtop = (self.middle_w + 700 + (- 100), self.middle_h + 350)
            elif self.title == 'next':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_b_x + (- 100), self.middle_b_y)
            elif self.title == 'go menu':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.start_b or self.game.space_b:
            if self.title == 'back':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules_page3
            elif self.title == 'go menu':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
            elif self.title == 'next':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules_page5
        self.go_display = False
        if self.game.esc_b:
            self.game.random_choose_sound()
            self.game.curr_menu = self.game.rules_page3
            self.go_display = False
        if self.game.exit_b:
            self.exit_status()


# Page of rules 5 - Scoring and bonuses
class RulesPage5(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'back'
        self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_w + 350)

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_menu()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.draw_text("Scoring and bonuses", self.game.font_size_Upper, self.label_rules_x,
                                    self.label_rules_y)
                self.game.draw_text("Each letter is assigned a number of points from 1 to 10 Some squares on the "
                                    "board are painted in different colors ", self.game.font_size, self.middle_w,
                                    self.middle_h - 350)
                self.game.draw_text("The number of points a player receives for a laid out word is calculated as "
                                    "follows", self.game.font_size, self.middle_w - 225, self.middle_h - 300)
                self.game.draw_text("* if the box under the letter is empty the number of points written on the letter "
                                    "is added", self.game.font_size, self.middle_w - 173, self.middle_h - 200)
                self.game.draw_text('* if the square is blue the number of points of the letter is multiplied by 2',
                                    self.game.font_size,
                                    self.middle_w - 290, self.middle_h - 150)
                self.game.draw_text('* if the square is pink the score of the whole word is multiplied by 2',
                                    self.game.font_size,
                                    self.middle_w - 343, self.middle_h - 100)
                self.game.draw_text('* if the square is blue the score of the letter is multiplied by 3',
                                    self.game.font_size,
                                    self.middle_w - 380, self.middle_h - 50)
                self.game.draw_text('* if the square is red the score of the whole word is multiplied by 3',
                                    self.game.font_size,
                                    self.middle_w - 350, self.middle_h)
                self.game.draw_text("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.draw_text("go menu", self.game.font_size, self.middle_b_x, self.middle_b_y)
            if self.title != 'go menu':
                self.game.display.blit(self.up_menu, (self.middle_w - 125, self.middle_h + 300))
            else:
                self.game.display.blit(self.up_menu_active, (self.middle_w - 125, self.middle_h + 300))
            if self.title != 'back':
                self.game.display.blit(self.back, (self.middle_w - 800, self.middle_h + 315))
            else:
                self.game.display.blit(self.back_active, (self.middle_w - 800, self.middle_h + 315))
            self.go_cursor()
            self.b_screen()

    def movement_in_menu(self):
        if self.game.arrow_right:
            if self.title == 'back':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h + 350)
            elif self.title == 'go menu':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()

        elif self.game.arrow_left:
            if self.title == 'back':
                self.title = 'go menu'
                self.cursor_rect.midtop = (self.middle_b_x + (- 100), self.middle_b_y)
            elif self.title == 'go menu':
                self.title = 'back'
                self.cursor_rect.midtop = (self.middle_w - 700 + (- 100), self.middle_h + 350)
            self.game.menu_effect.play()

    def check_movement(self):
        self.movement_in_menu()
        if self.game.start_b or self.game.space_b:
            if self.title == 'back':
                self.game.random_choose_sound()
                self.game.curr_menu = self.game.rules_page4
            elif self.title == 'go menu':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
        self.go_display = False
        if self.game.exit_b:
            self.game.exit_the_game()
        if self.game.esc_b:
            self.game.random_choose_sound()
            self.game.curr_menu = self.game.rules_page4
            self.go_display = False
