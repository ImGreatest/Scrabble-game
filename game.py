import random

import pygame.transform

from menu import *
from cfg import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Scrabble Game')
        self.pause_b, self.backspace_b, self.end_effects_b, self.end_music_b, self.space_b, self.arrow_left, self.arrow_right, self.arrow_up, self.arrow_down, self.start_b, self.esc_b, \
        self.exit_b = False, False, False, False, False, False, False, False, False, False, False, False
        self.q_b, self.w_b, self.e_b, self.r_b, self.t_b, self.y_b, self.u_b, self.i_b, self.o_b, self.p_b, self.a_b, \
        self.s_b, self.d_b, self.f_b, self.g_b, self.h_b, self.j_b, self.k_b, self.l_b, self.z_b, self.x_b, self.c_b, \
        self.v_b, self.b_b, self.n_b, self.m_b = False, False, False, False, False, False, False, False, False, False, \
                                                 False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False
        self.font_name = 'Font.TTF'
        self.font_size, self.font_size_Upper = 18, 20
        self.running = True
        self.white, self.black = (255, 255, 255), (0, 0, 0)
        #self.save_settings = SaveSettings(self)

        self.d_wide, self.d_high = 1920, 1080
        self.display = pygame.Surface((self.d_wide, self.d_high))
        self.screen = pygame.display.set_mode((self.d_wide, self.d_high))

        self.anyButton_page = AnyButtonPage(self)
        self.main_menu = MainMenu(self)
        self.settings = SettingsMenu(self)
        self.start = Start(self)
        self.music_menu = MusicPage(self)
        self.other_settings = OtherSettings(self)
        self.record_page = RecordPage(self)
        self.rules = Rules(self)
        self.rules_page2 = RulesPage2(self)
        self.rules_page3 = RulesPage3(self)
        self.rules_page4 = RulesPage4(self)
        self.rules_page5 = RulesPage5(self)
        #self.rules_page6 = RulesPage6(self)
        self.finish_page = FinishPage(self)
        self.curr_menu = self.anyButton_page

        # adding list for keeping layout letters on the board
        self.pos_list = []

        self.help_pos = []
        self.all_pos = []

        self.score = 0
        self.record_list = [0, 0, 0, 0, 0]
        self.record, self.record2, self.record3, self.record4, self.record5 = None, None, None, None, None

        self.letter_a, self.letter_b, self.letter_c, self.letter_d, self.letter_e, self.letter_f, \
        self.letter_g, self.letter_h, self.letter_i, self.letter_j, self.letter_k, self.letter_l, self.letter_m, \
        self.letter_s, self.letter_t, self.letter_u, self.letter_v, self.letter_w, self.letter_n, self.letter_o, \
        self.letter_p, self.letter_q, self.letter_r, self.letter_x, self.letter_y, self.letter_z = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
        self.letter_list_image = []
        self.counts_letters_in_letter_list = []
        self.letter_list = []
        self.pos_random_letter = [100, 200, 300, 400, 500, 600, 700]
        self.pos_random_letter_doubler = [100, 200, 300, 400, 500, 600, 700]
        self.count_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letter_list_img = []
        self.letter_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.contoids = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                         'y', 'z']
        self.vowel = ['a', 'e', 'i', 'o', 'u']
        self.count_letters_list = [9, 2, 2, 5, 13, 2, 3, 4, 8, 1, 1, 4, 2, 5, 8, 2, 1, 6, 5, 7, 4, 2, 2, 1, 2, 1]
        self.first_letters = True
        self.letter = None
        self.letter_img = None
        self.letter_img_doubler = None
        self.index_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.language = 'en'

        self.volume_pin1_w, self.volume_pin1_h = (self.d_wide / 2) + 50, (self.d_high / 2) - 160
        self.volume_pin2_w, self.volume_pin2_h = (self.d_wide / 2) + 50, (self.d_high / 2) - 65
        self.volume_music, self.volume_effects = 1, 1

        self.move_cursor_effect = pygame.mixer.Sound('music/sound/movement cursor.wav')
        self.lay_out_letter_effect = pygame.mixer.Sound('music/sound/lay out boxs.wav')
        self.accept_setting = pygame.mixer.Sound('music/sound/accept setting.wav')
        self.open_new_page = pygame.mixer.Sound('music/sound/open new page.wav')
        self.start_effect = pygame.mixer.Sound('music/sound/start effect .wav')
        self.back_menu_effect = pygame.mixer.Sound('music/sound/menu back sound.wav')
        self.menu_effect = pygame.mixer.Sound('music/sound/menu sound.wav')
        self.paper_sound_var1 = pygame.mixer.Sound('music/sound/turn the page.wav')
        self.paper_sound_var2 = pygame.mixer.Sound('music/sound/turn the page2.wav')
        self.paper_sound_var3 = pygame.mixer.Sound('music/sound/turn the page3.wav')

        pygame.mixer.music.set_volume(self.volume_music)
        self.accept_setting.set_volume(self.volume_effects)
        self.open_new_page.set_volume(self.volume_effects)
        self.start_effect.set_volume(self.volume_effects)
        self.back_menu_effect.set_volume(self.volume_effects)
        self.menu_effect.set_volume(self.volume_effects)
        self.paper_sound_var1.set_volume(self.volume_effects)
        self.paper_sound_var2.set_volume(self.volume_effects)
        self.paper_sound_var3.set_volume(self.volume_effects)

        self.sound_case = [self.paper_sound_var1, self.paper_sound_var2, self.paper_sound_var3]
        self.paper_sound = None
        self.music = True
        self.p_music = 'music/Start music.mp3'

        if self.music:
            pygame.mixer.music.load(self.p_music)
            pygame.mixer.music.play()
        else:
            if not self.music:
                pygame.mixer.music.pause()

        self.hide_list = []
        self.pos_x, self.pos_y = 55, 55
        self.size_box = 50
        self.cursor_board = pygame.image.load('jpg/cursor board.png').convert_alpha()
        self.score_panel = pygame.image.load('jpg/Score panel.png').convert_alpha()
        self.empty_box = pygame.image.load('jpg/boxs/empty - box.png').convert_alpha()
        self.tws_box = pygame.image.load('jpg/boxs/tws - box.png').convert_alpha()
        self.dls_box = pygame.image.load('jpg/boxs/bls - box.png').convert_alpha()
        self.dws_box = pygame.image.load('jpg/boxs/bws - box.png').convert_alpha()
        self.tls_box = pygame.image.load('jpg/boxs/tls - box.png').convert_alpha()
        self.start_box = pygame.image.load('jpg/boxs/start box.png').convert_alpha()
        self.score_panel = pygame.transform.scale(self.score_panel, (300, 300))
        self.cursor_board = pygame.transform.scale(self.cursor_board, (213,213))
        self.start_box = pygame.transform.scale(self.start_box, (self.size_box,self.size_box))
        self.empty_box = pygame.transform.scale(self.empty_box, (self.size_box,self.size_box))
        self.tws_box = pygame.transform.scale(self.tws_box, (self.size_box,self.size_box))
        self.dls_box = pygame.transform.scale(self.dls_box, (self.size_box,self.size_box))
        self.dws_box = pygame.transform.scale(self.dws_box, (self.size_box,self.size_box))
        self.tls_box = pygame.transform.scale(self.tls_box, (self.size_box,self.size_box))

        self.letter_list_image = [pygame.image.load(f"jpg/letters/{j}.jpg") for j in range(27)]
        self.j = 1
        for j in range(27):
            self.letter_list_image[j] = pygame.transform.scale(self.letter_list_image[j], (50, 50))

        # lamp animation
        self.animation1 = [pygame.image.load(f"video/Light animation/{i}.jpg") for i in range(0, 21)]
        self.i = 1
        for i in range(20):
            self.animation1[i] = pygame.transform.scale(self.animation1[i],(250, 250))

        self.remember_2pos = []

    def random_choose_sound(self):
        self.paper_sound = random.choice(self.sound_case)
        if self.paper_sound == self.paper_sound_var1:
            self.paper_sound_var1.play()
        elif self.paper_sound == self.paper_sound_var2:
            self.paper_sound_var2.play()
        elif self.paper_sound == self.paper_sound_var3:
            self.paper_sound_var3.play()

    def record_system(self):
        for i in range(3):
            if self.record_list[i] < self.record:
                self.record_list[i + 1] = self.record_list[i]
                self.record_list[i + 2] = self.record_list[i + 1]
                self.record_list[i] = self.record

    def hide_letter(self, letter):
        for i in range(len(self.letter_list)):
            if letter in self.letter_list[i] and self.counts_letters_in_letter_list[i] == 1:
                self.pos_random_letter[i] = -200
                break
            elif letter in self.letter_list[i] and self.counts_letters_in_letter_list[i] == 2:
                self.counts_letters_in_letter_list[i] -= 1
                self.remember_2pos.append(i)
                self.pos_random_letter[i] = -200
                print(self.remember_2pos)
                break

    def return_letter(self, letter):
        for i in range(len(self.letter_list)):
            if letter in self.letter_list[i] and self.counts_letters_in_letter_list[i] == 1:
                self.pos_random_letter[i] = self.pos_random_letter_doubler[i]
                break
            elif letter in self.letter_list[i] and self.counts_letters_in_letter_list[i] == 2:
                self.counts_letters_in_letter_list[self.remember_2pos[-1]] += 1
                self.pos_random_letter[self.remember_2pos[-1]] = self.pos_random_letter_doubler[self.remember_2pos[-1]]
                self.remember_2pos.pop()
                print(self.remember_2pos)
                break

    def random_letter(self, count):
        a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q, r, s, t, u, v, w, x, y, z = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        zx = 1
        for zx in range(count):
            self.letter = random.choice(self.letter_case)
            if len(self.letter_list) == 0:
                self.letter = random.choice(self.letter_case)
            elif len(self.letter_list) != 0:
                if self.letter_list[-1] in self.contoids:
                    self.letter = random.choice(self.vowel)
                elif self.letter_list[-1] in self.vowel:
                    self.letter = random.choice(self.contoids)

            if self.letter == 'a':
                self.letter_img = self.letter_list_image[1]
                self.letter_a = True
                if self.letter_a:
                    a += 1
                else:
                    a = 0
                self.count_letters[0] = a
                self.count_letters_list[0] -= a
            elif self.letter == 'b':
                self.letter_img = self.letter_list_image[2]
                self.letter_b = True
                if self.letter_b:
                    b += 1
                else:
                    b = 0
                self.count_letters[1] = b
                self.count_letters_list[1] -= b
            elif self.letter == 'c':
                self.letter_c = True
                self.letter_img = self.letter_list_image[3]
                if self.letter_c:
                    c += 1
                else:
                    c = 0
                self.count_letters[2] = c
                self.count_letters_list[2] -= c
            elif self.letter == 'd':
                self.letter_d = True
                self.letter_img = self.letter_list_image[4]
                if self.letter_d:
                    d += 1
                else:
                    d = 0
                self.count_letters[3] = d
                self.count_letters_list[3] -= d
            elif self.letter == 'e':
                self.letter_e = True
                self.letter_img = self.letter_list_image[5]
                if self.letter_e:
                    e += 1
                else:
                    e = 0
                self.count_letters[4] = e
                self.count_letters_list[4] -= e
            elif self.letter == 'f':
                self.letter_f = True
                self.letter_img = self.letter_list_image[6]
                if self.letter_f:
                    f += 1
                else:
                    f = 0
                self.count_letters[5] = f
                self.count_letters_list[5] -= f
            elif self.letter == 'g':
                self.letter_g = True
                self.letter_img = self.letter_list_image[7]
                if self.letter_g:
                    g += 1
                else:
                    g = 0
                self.count_letters[6] = g
                self.count_letters_list[6] -= g
            elif self.letter == 'h':
                self.letter_h = True
                self.letter_img = self.letter_list_image[8]
                if self.letter_h:
                    h += 1
                else:
                    h = 0
                self.count_letters[7] = h
                self.count_letters_list[7] -= h
            elif self.letter == 'i':
                self.letter_i = True
                self.letter_img = self.letter_list_image[9]
                if self.letter_i:
                    i += 1
                else:
                    i = 0
                self.count_letters[8] = i
                self.count_letters_list[8] -= i
            elif self.letter == 'j':
                self.letter_j = True
                self.letter_img = self.letter_list_image[10]
                if self.letter_j:
                    j += 1
                else:
                    j = 0
                self.count_letters[9] = j
                self.count_letters_list[9] -= j
            elif self.letter == 'k':
                self.letter_k = True
                self.letter_img = self.letter_list_image[11]
                if self.letter_k:
                    k += 1
                else:
                    k = 0
                self.count_letters[10] = k
                self.count_letters_list[10] -= k
            elif self.letter == 'l':
                self.letter_l = True
                self.letter_img = self.letter_list_image[12]
                if self.letter_l:
                    ll += 1
                else:
                    ll = 0
                self.count_letters[11] = ll
                self.count_letters_list[11] -= ll
            elif self.letter == 'm':
                self.letter_m = True
                self.letter_img = self.letter_list_image[13]
                if self.letter_m:
                    m += 1
                else:
                    m = 0
                self.count_letters[12] = m
                self.count_letters_list[12] -= m
            elif self.letter == 'o':
                self.letter_o = True
                self.letter_img = self.letter_list_image[15]
                if self.letter_o:
                    o += 1
                else:
                    o = 0
                self.count_letters[14] = o
                self.count_letters_list[14] -= o
            elif self.letter == 'n':
                self.letter_n = True
                self.letter_img = self.letter_list_image[14]
                if self.letter_n:
                    n += 1
                else:
                    n = 0
                self.count_letters[13] = n
                self.count_letters_list[13] -= n
            elif self.letter == 'p':
                self.letter_p = True
                self.letter_img = self.letter_list_image[16]
                if self.letter_p:
                    p += 1
                else:
                    p = 0
                self.count_letters[15] = p
                self.count_letters_list[15] -= p
            elif self.letter == 'q':
                self.letter_q = True
                self.letter_img = self.letter_list_image[17]
                if self.letter_q:
                    q += 1
                else:
                    q = 0
                self.count_letters[16] = q
                self.count_letters_list[16] -= q
            elif self.letter == 'r':
                self.letter_r = True
                self.letter_img = self.letter_list_image[18]
                if self.letter_r:
                    r += 1
                else:
                    r = 0
                self.count_letters[17] = r
                self.count_letters_list[17] -= r
            elif self.letter == 's':
                self.letter_s = True
                self.letter_img = self.letter_list_image[19]
                if self.letter_s:
                    s += 1
                else:
                    s = 0
                self.count_letters[18] = s
                self.count_letters_list[18] -= s
            elif self.letter == 't':
                self.letter_t = True
                self.letter_img = self.letter_list_image[20]
                if self.letter_t:
                    t += 1
                else:
                    t = 0
                self.count_letters[19] = t
                self.count_letters_list[19] -= t
            elif self.letter == 'u':
                self.letter_u = True
                self.letter_img = self.letter_list_image[21]
                if self.letter_u:
                    u += 1
                else:
                    u = 0
                self.count_letters[20] = u
                self.count_letters_list[20] -= u
            elif self.letter == 'v':
                self.letter_v = True
                self.letter_img = self.letter_list_image[22]
                if self.letter_v:
                    v += 1
                else:
                    v = 0
                self.count_letters[21] = v
                self.count_letters_list[21] -= v
            elif self.letter == 'w':
                self.letter_w = True
                self.letter_img = self.letter_list_image[23]
                if self.letter_w:
                    w += 1
                else:
                    w = 0
                self.count_letters[22] = w
                self.count_letters_list[22] -= w
            elif self.letter == 'x':
                self.letter_x = True
                self.letter_img = self.letter_list_image[24]
                if self.letter_x:
                    x += 1
                else:
                    x = 0
                self.count_letters[23] = x
                self.count_letters_list[23] -= x
            elif self.letter == 'y':
                self.letter_y = True
                self.letter_img = self.letter_list_image[25]
                if self.letter_y:
                    y += 1
                else:
                    y = 0
                self.count_letters[24] = y
                self.count_letters_list[24] -= y
            elif self.letter == 'z':
                self.letter_img = self.letter_list_image[26]
                self.letter_z = True
                if self.letter_z:
                    z += 1
                else:
                    z = 0
                self.count_letters[25] = z
                self.count_letters_list[25] -= z

            self.letter_list.append(self.letter)
            #self.del_letter_from_lists()
            self.letter_list_img.append(self.letter_img)

        if self.first_letters:
            for zz in range(26):
                if self.count_letters[zz] == 1:
                    continue
                elif self.count_letters[zz] == 2:
                    continue
                elif self.count_letters[zz] != 1 or 2:
                    self.count_letters[zz] = 0
            self.first_letters = False

        print(self.count_letters)
        print(self.letter_list)

        for j in range(len(self.letter_list)):
            self.counts_letters_in_letter_list.append(self.letter_list.count(self.letter_list[j]))
        print(self.counts_letters_in_letter_list)

        #for c in range(len(self.counts_letters_in_letter_list)):
        #    if self.counts_letters_in_letter_list[c] == 2:
        #        self.remember_2pos.append(c)

    def bag_letter(self):
        a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q, r, s, t, u, v, w, x, y, z = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        letter = None
        letter_img = None

        zx = 0
        for zx in range(1):
            letter = random.choice(self.letter_case)
            if len(self.letter_list) == 0:
                self.letter = random.choice(self.letter_case)
            if len(self.letter_list) != 0:
                if self.letter_list[-1] in self.contoids:
                    self.letter = random.choice(self.vowel)
                else:
                    self.letter = random.choice(self.contoids)
            if letter == 'a':
                self.letter_img_doubler = self.letter_list_image[1]
                self.letter_a = True
                self.count_letters[0] += 1
            elif letter == 'b':
                self.letter_img_doubler = self.letter_list_image[2]
                self.letter_b = True
                self.count_letters[1] += 1
            elif letter == 'c':
                self.letter_c = True
                self.letter_img_doubler = self.letter_list_image[3]
                self.count_letters[2] += 1
            elif letter == 'd':
                self.letter_d = True
                self.letter_img_doubler = self.letter_list_image[4]
                self.count_letters[3] += 1
            elif letter == 'e':
                self.letter_e = True
                self.letter_img_doubler = self.letter_list_image[5]
                self.count_letters[4] += 1
            elif letter == 'f':
                self.letter_f = True
                self.letter_img_doubler = self.letter_list_image[6]
                self.count_letters[5] += 1
            elif letter == 'g':
                self.letter_g = True
                self.letter_img_doubler = self.letter_list_image[7]
                self.count_letters[6] += 1
            elif letter == 'h':
                self.letter_h = True
                self.letter_img_doubler = self.letter_list_image[8]
                self.count_letters[7] += 1
            elif letter == 'i':
                self.letter_i = True
                self.letter_img_doubler = self.letter_list_image[9]
                self.count_letters[8] += 1
            elif letter == 'j':
                self.letter_j = True
                self.letter_img_doubler = self.letter_list_image[10]
                self.count_letters[9] += 1
            elif letter == 'k':
                self.letter_k = True
                self.letter_img_doubler = self.letter_list_image[11]
                self.count_letters[10] += 1
            elif letter == 'l':
                self.letter_l = True
                self.letter_img_doubler = self.letter_list_image[12]
                self.count_letters[11] += 1
            elif letter == 'm':
                self.letter_m = True
                self.letter_img_doubler = self.letter_list_image[13]
                self.count_letters[12] += 1
            elif letter == 'o':
                self.letter_o = True
                self.letter_img_doubler = self.letter_list_image[15]
                self.count_letters[13] += 1
            elif letter == 'n':
                self.letter_n = True
                self.letter_img_doubler = self.letter_list_image[14]
                self.count_letters[14] += 1
            elif letter == 'p':
                self.letter_p = True
                self.letter_img_doubler = self.letter_list_image[16]
                self.count_letters[15] += 1
            elif letter == 'q':
                self.letter_q = True
                self.letter_img_doubler = self.letter_list_image[17]
                self.count_letters[16] += 1
            elif letter == 'r':
                self.letter_r = True
                self.letter_img_doubler = self.letter_list_image[18]
                self.count_letters[17] += 1
            elif letter == 's':
                self.letter_s = True
                self.letter_img_doubler = self.letter_list_image[19]
                self.count_letters[18] += 1
            elif letter == 't':
                self.letter_t = True
                self.letter_img_doubler = self.letter_list_image[20]
                self.count_letters[19] += 1
            elif letter == 'u':
                self.letter_u = True
                self.letter_img_doubler = self.letter_list_image[21]
                self.count_letters[20] += 1
            elif letter == 'v':
                self.letter_v = True
                self.letter_img_doubler = self.letter_list_image[22]
                self.count_letters[21] += 1
            elif letter == 'w':
                self.letter_w = True
                self.letter_img_doubler = self.letter_list_image[23]
                self.count_letters[22] += 1
            elif letter == 'x':
                self.letter_x = True
                self.letter_img_doubler = self.letter_list_image[24]
                self.count_letters[23] += 1
            elif letter == 'y':
                self.letter_y = True
                self.letter_img_doubler = self.letter_list_image[25]
                self.count_letters[24] += 1
            elif letter == 'z':
                self.letter_z = True
                self.letter_img_doubler = self.letter_list_image[26]
                self.count_letters[25] += 1
            return letter

        #self.del_letter_from_lists()

    def movement_button(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.save_settings.save()
                self.running = False
                self.curr_menu.go_display = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAUSE:
                    self.pause_b = True
                if event.key == pygame.K_ESCAPE:
                    self.esc_b = True
                if event.key == pygame.K_DOWN:
                    self.arrow_down = True
                if event.key == pygame.K_UP:
                    self.arrow_up = True
                if event.key == pygame.K_RIGHT:
                    self.arrow_right = True
                if event.key == pygame.K_LEFT:
                    self.arrow_left = True
                if event.key == pygame.K_DELETE:
                    self.exit_b = True
                if event.key == pygame.K_RETURN:
                    self.start_b = True
                if event.key == pygame.K_SPACE:
                    self.space_b = True
                if event.key == pygame.K_END:
                    self.end_music_b = True
                if event.key == pygame.K_HOME:
                    self.end_effects_b = True
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_b = True

                if event.key == pygame.K_a:
                    self.a_b = True
                if event.key == pygame.K_q:
                    self.q_b = True
                if event.key == pygame.K_w:
                    self.w_b = True
                if event.key == pygame.K_e:
                    self.e_b = True
                if event.key == pygame.K_r:
                    self.r_b = True
                if event.key == pygame.K_t:
                    self.t_b = True
                if event.key == pygame.K_y:
                    self.y_b = True
                if event.key == pygame.K_u:
                    self.u_b = True
                if event.key == pygame.K_i:
                    self.i_b = True
                if event.key == pygame.K_o:
                    self.o_b = True
                if event.key == pygame.K_p:
                    self.p_b = True
                if event.key == pygame.K_s:
                    self.s_b = True
                if event.key == pygame.K_d:
                    self.d_b = True
                if event.key == pygame.K_f:
                    self.f_b = True
                if event.key == pygame.K_g:
                    self.g_b = True
                if event.key == pygame.K_h:
                    self.h_b = True
                if event.key == pygame.K_j:
                    self.j_b = True
                if event.key == pygame.K_k:
                    self.k_b = True
                if event.key == pygame.K_l:
                    self.l_b = True
                if event.key == pygame.K_z:
                    self.z_b = True
                if event.key == pygame.K_x:
                    self.x_b = True
                if event.key == pygame.K_c:
                    self.c_b = True
                if event.key == pygame.K_b:
                    self.b_b = True
                if event.key == pygame.K_v:
                    self.v_b = True
                if event.key == pygame.K_n:
                    self.n_b = True
                if event.key == pygame.K_m:
                    self.m_b = True

    def reset(self):
        self.pause_b, self.backspace_b, self.end_effects_b, self.end_music_b, self.space_b, self.arrow_left, self.arrow_right, self.arrow_up, self.arrow_down, self.start_b, self.esc_b, \
        self.exit_b = False, False, False, False, False, False, False, False, False, False, False, False

        self.q_b, self.w_b, self.e_b, self.r_b, self.t_b, self.y_b, self.u_b, self.i_b, self.o_b, self.p_b, self.a_b, \
        self.s_b, self.d_b, self.f_b, self.g_b, self.h_b, self.j_b, self.k_b, self.l_b, self.z_b, self.x_b, self.c_b, \
        self.v_b, self.b_b, self.n_b, self.m_b = False, False, False, False, False, False, False, False, False, False, \
                                                 False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False

    def drawing(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_sur = font.render(text, True, self.white)
        rect = text_sur.get_rect()
        rect.center = (x, y)
        self.display.blit(text_sur, rect)

    def del_letter_from_lists(self):
        if self.letter == 'k' or 'j' or 'q' or 'x' or 'z':
            self.contoids.remove(self.letter)
        elif self.letter == 'a' and self.count_letters_list[0] == 0:
            self.vowel.remove(self.letter)
        elif self.letter == 'b' and self.count_letters_list[1] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'c' and self.count_letters_list[2] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'd' and self.count_letters_list[3] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'e' and self.count_letters_list[4] == 0:
            self.vowel.remove(self.letter)
        elif self.letter == 'f' and self.count_letters_list[5] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'g' and self.count_letters_list[6] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'h' and self.count_letters_list[7] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'i' and self.count_letters_list[8] == 0:
            self.vowel.remove(self.letter)
        elif self.letter == 'l' and self.count_letters_list[10] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'm' and self.count_letters_list[11] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'n' and self.count_letters_list[12] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'o' and self.count_letters_list[13] == 0:
            self.vowel.remove(self.letter)
        elif self.letter == 'p' and self.count_letters_list[14] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'r' and self.count_letters_list[16] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 's' and self.count_letters_list[17] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 't' and self.count_letters_list[18] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'u' and self.count_letters_list[19] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'v' and self.count_letters_list[20] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'w' and self.count_letters_list[21] == 0:
            self.contoids.remove(self.letter)
        elif self.letter == 'z' and self.count_letters_list[23] == 0:
            self.contoids.remove(self.letter)

    def draw_board(self):
        pygame.draw.rect(self.display, (244, 164, 96), pygame.Rect(50, 50, 830,
830))
        pygame.draw.rect(self.display, (244, 164, 96), pygame.Rect(1300, 300,
200, 700))
        #pygame.draw.rect(self.display, (244, 164, 96), pygame.Rect(1500, 300, 400, 700))

        self.display.blit(self.tws_box, (self.pos_x, self.pos_y))  # red box
        self.display.blit(self.tws_box, (self.pos_x + 770, self.pos_y + 770))
        self.display.blit(self.tws_box, (self.pos_x + 385, self.pos_y))
        self.display.blit(self.tws_box, (self.pos_x + 385, self.pos_y + 770))
        self.display.blit(self.tws_box, (self.pos_x + 770, self.pos_y))
        self.display.blit(self.tws_box, (self.pos_x, self.pos_y + 770))
        self.display.blit(self.tws_box, (self.pos_x, self.pos_y + 385))
        self.display.blit(self.tws_box, (self.pos_x + 770, self.pos_y + 385))

        self.display.blit(self.dws_box, (self.pos_x + 55, self.pos_y + 55))  #pink box
        self.display.blit(self.dws_box, (self.pos_x + 110, self.pos_y + 110))
        self.display.blit(self.dws_box, (self.pos_x + 165, self.pos_y + 165))
        self.display.blit(self.dws_box, (self.pos_x + 220, self.pos_y + 220))
        self.display.blit(self.dws_box, (self.pos_x + 550, self.pos_y + 550))
        self.display.blit(self.dws_box, (self.pos_x + 605, self.pos_y + 605))
        self.display.blit(self.dws_box, (self.pos_x + 660, self.pos_y + 660))
        self.display.blit(self.dws_box, (self.pos_x + 715, self.pos_y + 715))
        self.display.blit(self.dws_box, (self.pos_x + 715, self.pos_y + 55))
        self.display.blit(self.dws_box, (self.pos_x + 715 - 55, self.pos_y + 110))
        self.display.blit(self.dws_box, (self.pos_x + 715 - 110, self.pos_y + 165))
        self.display.blit(self.dws_box, (self.pos_x + 715 - 165, self.pos_y + 220))
        self.display.blit(self.dws_box, (self.pos_x + 55, self.pos_y + 715))
        self.display.blit(self.dws_box, (self.pos_x + 110, self.pos_y + 660))
        self.display.blit(self.dws_box, (self.pos_x + 165, self.pos_y + 605))
        self.display.blit(self.dws_box, (self.pos_x + 220, self.pos_y + 550))

        self.display.blit(self.tls_box, (self.pos_x + 275, self.pos_y + 275))
# dark blue box
        self.display.blit(self.tls_box, (self.pos_x + 495, self.pos_y + 275))
        self.display.blit(self.tls_box, (self.pos_x + 275, self.pos_y + 495))
        self.display.blit(self.tls_box, (self.pos_x + 495, self.pos_y + 495))
        self.display.blit(self.tls_box, (self.pos_x + 55, self.pos_y + 495))
        self.display.blit(self.tls_box, (self.pos_x + 495, self.pos_y + 55))
        self.display.blit(self.tls_box, (self.pos_x + 275, self.pos_y + 55))
        self.display.blit(self.tls_box, (self.pos_x + 55, self.pos_y + 275))
        self.display.blit(self.tls_box, (self.pos_x + 715, self.pos_y + 275))
        self.display.blit(self.tls_box, (self.pos_x + 715, self.pos_y + 495))
        self.display.blit(self.tls_box, (self.pos_x + 275, self.pos_y + 715))
        self.display.blit(self.tls_box, (self.pos_x + 495, self.pos_y + 715))

        self.display.blit(self.dls_box, (self.pos_x + 330, self.pos_y + 330))
# light blue box
        self.display.blit(self.dls_box, (self.pos_x + 330, self.pos_y + 440))
        self.display.blit(self.dls_box, (self.pos_x + 440, self.pos_y + 330))
        self.display.blit(self.dls_box, (self.pos_x + 440, self.pos_y + 440))
        self.display.blit(self.dls_box, (self.pos_x + 330, self.pos_y + 110))
        self.display.blit(self.dls_box, (self.pos_x + 385, self.pos_y + 165))
        self.display.blit(self.dls_box, (self.pos_x + 440, self.pos_y + 110))
        self.display.blit(self.dls_box, (830 - 335, 830 - 115))
        self.display.blit(self.dls_box, (830 - 390, 830 - 170))
        self.display.blit(self.dls_box, (830 - 445, 830 - 115))
        self.display.blit(self.dls_box, (self.pos_x + 165, self.pos_y))
        self.display.blit(self.dls_box, (self.pos_x + 605, self.pos_y))
        self.display.blit(self.dls_box, (self.pos_x + 165, self.pos_y + 770))
        self.display.blit(self.dls_box, (self.pos_x + 605, self.pos_y + 770))
        self.display.blit(self.dls_box, (self.pos_x + 110, self.pos_y + 330))
        self.display.blit(self.dls_box, (self.pos_x + 110, self.pos_y + 440))
        self.display.blit(self.dls_box, (self.pos_x + 165, self.pos_y + 385))
        self.display.blit(self.dls_box, (830 - 115, self.pos_y + 330))
        self.display.blit(self.dls_box, (830 - 115, self.pos_y + 440))
        self.display.blit(self.dls_box, (830 - 170, self.pos_y + 385))
        self.display.blit(self.dls_box, (self.pos_x, self.pos_y + 165))
        self.display.blit(self.dls_box, (self.pos_x, self.pos_y + 605))
        self.display.blit(self.dls_box, (self.pos_x + 770, self.pos_y + 605))
        self.display.blit(self.dls_box, (self.pos_x + 770, self.pos_y + 165))

        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y))  #empty box
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 55))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 55))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 110))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 110))

        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 165))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 165))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 220))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 220))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 275))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 275))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 330))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 330))

        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 385))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 385))

        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 770))
        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 770))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 715))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 715))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 660))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 660))

        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 605))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 605))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 550))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 550))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 110, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 330, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 440, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 660, self.pos_y + 495))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 495))

        self.display.blit(self.empty_box, (self.pos_x, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 55, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 165, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 220, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 275, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 385, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 495, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 550, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 605, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 715, self.pos_y + 440))
        self.display.blit(self.empty_box, (self.pos_x + 770, self.pos_y + 440))

        self.display.blit(self.start_box, (self.pos_x + 385, self.pos_y + 385))
