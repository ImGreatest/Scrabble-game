import sys
import math
from itertools import permutations
import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.middle_w, self.middle_h, self.full_w, self.full_h, self.go_display = self.game.d_wide / 2, self.game.d_high / 2, self.game.d_wide, self.game.d_high, True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.label_rules_x, self.label_rules_y = self.middle_w, self.middle_h - 400
        self.middle_b_x, self.middle_b_y = self.middle_w, self.middle_h + 350
        self.left_arrow_x, self.left_arrow_y = self.middle_w - 700, self.middle_h + 350
        self.right_arrow_x, self.right_arrow_y = self.middle_w + 700, self.middle_h + 350

        self.a1_x, self.a1_y, self.a2_x, self.a2_y, self.a3_x, self.a3_y, self.a4_x, self.a4_y, self.a5_x, self.a5_y, self.a6_x, self.a6_y, self.a7_x, self.a7_y, self.a8_x, self.a8_y, self.a9_x, self.a9_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200 - 200, -200
        self.l1_x, self.l1_y, self.l2_x, self.l2_y, self.l3_x, self.l3_y, self.l4_x, self.l4_y = -200, -200, -200, -200, -200, -200, -200, -200
        self.b1_x, self.b1_y, self.b2_x, self.b2_y = -200, -200, -200, -200
        self.c1_x, self.c1_y, self.c2_x, self.c2_y = -200, -200, -200, -200
        self.d1_x, self.d1_y, self.d2_x, self.d2_y, self.d3_x, self.d3_y, self.d4_x, self.d4_y, self.d5_x, self.d5_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.o1_x, self.o1_y, self.o2_x, self.o2_y, self.o3_x, self.o3_y, self.o4_x, self.o4_y, self.o5_x, self.o5_y, self.o6_x, self.o6_y, self.o7_x, self.o7_y, self.o8_x, self.o8_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.e1_x, self.e1_y, self.e2_x, self.e2_y, self.e3_x, self.e3_y, self.e4_x, self.e4_y, self.e5_x, self.e5_y, self.e6_x, self.e6_y, self.e7_x, self.e7_y, self.e8_x, self.e8_y, self.e9_x, self.e9_y, self.e10_x, self.e10_y, self.e11_x, self.e11_y, self.e12_x, self.e12_y, self.e13_x, self.e13_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.i1_x, self.i1_y, self.i2_x, self.i2_y, self.i3_x, self.i3_y, self.i4_x, self.i4_y, self.i5_x, self.i5_y, self.i6_x, self.i6_y, self.i7_x, self.i7_y, self.i8_x, self.i8_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.h1_x, self.h1_y, self.h2_x, self.h2_y, self.h3_x, self.h3_y, self.h4_x, self.h4_y = -200, -200, -200, -200, -200, -200, -200, -200
        self.m1_x, self.m1_y, self.m2_x, self.m2_y = -200, -200, -200, -200
        self.f1_x, self.f1_y, self.f2_x, self.f2_y = -200, -200, -200, -200
        self.g1_x, self.g1_y, self.g2_x, self.g2_y, self.g3_x, self.g3_y = -200, -200, -200, -200, -200, -200
        self.j1_x, self.j1_y = -200, -200
        self.k1_x, self.k1_y = -200, -200
        self.n1_x, self.n1_y, self.n2_x, self.n2_y, self.n3_x, self.n3_y, self.n4_x, self.n4_y, self.n5_x, self.n5_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.q1_x, self.q1_y = -200, -200
        self.x1_x, self.x1_y = -200, -200
        self.z1_x, self.z1_y = -200, -200
        self.r1_x, self.r1_y, self.r2_x, self.r2_y, self.r3_x, self.r3_y, self.r4_x, self.r4_y, self.r5_x, self.r5_y, self.r6_x, self.r6_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.v1_x, self.v1_y, self.v2_x, self.v2_y = -200, -200, -200, -200
        self.p1_x, self.p1_y, self.p2_x, self.p2_y = -200, -200, -200, -200
        self.s1_x, self.s1_y, self.s2_x, self.s2_y, self.s3_x, self.s3_y, self.s4_x, self.s4_y, self.s5_x, self.s5_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.t1_x, self.t1_y, self.t2_x, self.t2_y, self.t3_x, self.t3_y, self.t4_x, self.t4_y, self.t5_x, self.t5_y, self.t6_x, self.t6_y, self.t7_x, self.t7_y = -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200, -200
        self.u1_x, self.u1_y, self.u2_x, self.u2_y, self.u3_x, self.u3_y, self.u4_x, self.u4_y = -200, -200, -200, -200, -200, -200, -200, -200
        self.w1_x, self.w1_y, self.w2_x, self.w2_y = -200, -200, -200, -200
        self.y1_x, self.y1_y, self.y2_x, self.y2_y = -200, -200, -200, -200
        self.lay_out_letters, self.pos_cur_list, self.box_marker_list, self.pos_with_new_list, self.letter_status_list = [], [], [], [], [True, True, True, True, True, True, True]
        self.letter_status, self.movement_board, self.lay_out_control, self.index_letter, self.cur_x, self.cur_y = None, False, True, None, None, None
        self.pos_x, self.pos_y, self.board_cur_x, self.board_cur_y, self.last_word, self.lay_out_letters_doubler = 55, 55, 385 - 10, 385 - 3.2, None, None
        self.finding_word, self.finded_words, self.finded_words_scores = None, [], []

        pygame.mouse.set_visible(False)

        self.back = pygame.image.load('jpg/image/single back arrow.png').convert_alpha()
        self.back_active = pygame.image.load('jpg/active image/back arrow active.png').convert_alpha()
        self.next = pygame.image.load('jpg/image/single next arrow.png').convert_alpha()
        self.up_menu = pygame.image.load('jpg/image/single arrow.png').convert_alpha()
        self.next_active = pygame.image.load('jpg/active image/next arrow active.png').convert_alpha()
        self.up_menu_active = pygame.image.load('jpg/active image/arrow active.png').convert_alpha()
        self.back = pygame.transform.scale(self.back, (70, 70))
        self.next = pygame.transform.scale(self.next, (100, 100))
        self.back_active = pygame.transform.scale(self.back_active, (70, 70))
        self.up_menu = pygame.transform.scale(self.up_menu, (100, 100))
        self.up_menu_active = pygame.transform.scale(self.up_menu_active, (100, 100))
        self.next_active = pygame.transform.scale(self.next_active, (100, 100))

    def draw_box(self):
        self.game.display.blit(self.game.letter_list_image[1], (self.a1_x, self.a1_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a2_x, self.a2_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a3_x, self.a3_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a4_x, self.a4_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a5_x, self.a5_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a6_x, self.a6_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a7_x, self.a7_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a8_x, self.a8_y))
        self.game.display.blit(self.game.letter_list_image[1], (self.a9_x, self.a9_y))

        self.game.display.blit(self.game.letter_list_image[2], (self.b1_x, self.b1_y))
        self.game.display.blit(self.game.letter_list_image[2], (self.b2_x, self.b2_y))
        self.game.display.blit(self.game.letter_list_image[3], (self.c1_x, self.c1_y))
        self.game.display.blit(self.game.letter_list_image[3], (self.c2_x, self.c2_y))
        self.game.display.blit(self.game.letter_list_image[4], (self.d1_x, self.d1_y))
        self.game.display.blit(self.game.letter_list_image[4], (self.d2_x, self.d2_y))
        self.game.display.blit(self.game.letter_list_image[4], (self.d3_x, self.d3_y))
        self.game.display.blit(self.game.letter_list_image[4], (self.d4_x, self.d4_y))
        self.game.display.blit(self.game.letter_list_image[4], (self.d5_x, self.d5_y))

        self.game.display.blit(self.game.letter_list_image[5], (self.e1_x, self.e1_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e2_x, self.e2_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e3_x, self.e3_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e4_x, self.e4_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e5_x, self.e5_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e6_x, self.e6_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e7_x, self.e7_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e8_x, self.e8_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e9_x, self.e9_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e10_x, self.e10_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e11_x, self.e11_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e12_x, self.e12_y))
        self.game.display.blit(self.game.letter_list_image[5], (self.e13_x, self.e13_y))

        self.game.display.blit(self.game.letter_list_image[6], (self.f1_x, self.f1_y))
        self.game.display.blit(self.game.letter_list_image[6], (self.f2_x, self.f2_y))
        self.game.display.blit(self.game.letter_list_image[7], (self.g1_x, self.g1_y))
        self.game.display.blit(self.game.letter_list_image[7], (self.g2_x, self.g2_y))
        self.game.display.blit(self.game.letter_list_image[7], (self.g3_x, self.g3_y))
        self.game.display.blit(self.game.letter_list_image[8], (self.h1_x, self.h1_y))
        self.game.display.blit(self.game.letter_list_image[8], (self.h2_x, self.h2_y))
        self.game.display.blit(self.game.letter_list_image[8], (self.h3_x, self.h3_y))
        self.game.display.blit(self.game.letter_list_image[8], (self.h4_x, self.h4_y))

        self.game.display.blit(self.game.letter_list_image[9], (self.i1_x, self.i1_y))
        self.game.display.blit(self.game.letter_list_image[9], (self.i2_x, self.i2_y))
        self.game.display.blit(self.game.letter_list_image[9], (self.i3_x, self.i3_y))
        self.game.display.blit(self.game.letter_list_image[9], (self.i4_x, self.i4_y))
        self.game.display.blit(self.game.letter_list_image[9], (self.i5_x, self.i5_y))
        self.game.display.blit(self.game.letter_list_image[9], (self.i6_x, self.i6_y))
        self.game.display.blit(self.game.letter_list_image[9], (self.i7_x, self.i7_y))
        self.game.display.blit(self.game.letter_list_image[9], (self.i8_x, self.i8_y))

        self.game.display.blit(self.game.letter_list_image[10], (self.j1_x, self.j1_y))
        self.game.display.blit(self.game.letter_list_image[11], (self.k1_x, self.k1_y))
        self.game.display.blit(self.game.letter_list_image[12], (self.l1_x, self.l1_y))
        self.game.display.blit(self.game.letter_list_image[12], (self.l2_x, self.l2_y))
        self.game.display.blit(self.game.letter_list_image[12], (self.l3_x, self.l3_y))
        self.game.display.blit(self.game.letter_list_image[12], (self.l4_x, self.l4_y))
        self.game.display.blit(self.game.letter_list_image[13], (self.m1_x, self.m1_y))
        self.game.display.blit(self.game.letter_list_image[13], (self.m2_x, self.m2_y))

        self.game.display.blit(self.game.letter_list_image[14], (self.n1_x, self.n1_y))
        self.game.display.blit(self.game.letter_list_image[14], (self.n2_x, self.n2_y))
        self.game.display.blit(self.game.letter_list_image[14], (self.n3_x, self.n3_y))
        self.game.display.blit(self.game.letter_list_image[14], (self.n4_x, self.n4_y))
        self.game.display.blit(self.game.letter_list_image[14], (self.n5_x, self.n5_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o1_x, self.o1_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o2_x, self.o2_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o3_x, self.o3_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o4_x, self.o4_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o5_x, self.o5_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o6_x, self.o6_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o7_x, self.o7_y))
        self.game.display.blit(self.game.letter_list_image[15], (self.o8_x, self.o8_y))

        self.game.display.blit(self.game.letter_list_image[16], (self.p1_x, self.p1_y))
        self.game.display.blit(self.game.letter_list_image[16], (self.p2_x, self.p2_y))
        self.game.display.blit(self.game.letter_list_image[17], (self.q1_x, self.q1_y))
        self.game.display.blit(self.game.letter_list_image[18], (self.r1_x, self.r1_y))
        self.game.display.blit(self.game.letter_list_image[18], (self.r2_x, self.r2_y))
        self.game.display.blit(self.game.letter_list_image[18], (self.r3_x, self.r3_y))
        self.game.display.blit(self.game.letter_list_image[18], (self.r4_x, self.r4_y))
        self.game.display.blit(self.game.letter_list_image[18], (self.r5_x, self.r5_y))
        self.game.display.blit(self.game.letter_list_image[18], (self.r6_x, self.r6_y))

        self.game.display.blit(self.game.letter_list_image[19], (self.s1_x, self.s1_y))
        self.game.display.blit(self.game.letter_list_image[19], (self.s2_x, self.s2_y))
        self.game.display.blit(self.game.letter_list_image[19], (self.s3_x, self.s3_y))
        self.game.display.blit(self.game.letter_list_image[19], (self.s4_x, self.s4_y))
        self.game.display.blit(self.game.letter_list_image[19], (self.s5_x, self.s5_y))

        self.game.display.blit(self.game.letter_list_image[20], (self.t1_x, self.t1_y))
        self.game.display.blit(self.game.letter_list_image[20], (self.t2_x, self.t2_y))
        self.game.display.blit(self.game.letter_list_image[20], (self.t3_x, self.t3_y))
        self.game.display.blit(self.game.letter_list_image[20], (self.t4_x, self.t4_y))
        self.game.display.blit(self.game.letter_list_image[20], (self.t5_x, self.t5_y))
        self.game.display.blit(self.game.letter_list_image[20], (self.t6_x, self.t6_y))
        self.game.display.blit(self.game.letter_list_image[21], (self.u1_x, self.u1_y))
        self.game.display.blit(self.game.letter_list_image[21], (self.u2_x, self.u2_y))
        self.game.display.blit(self.game.letter_list_image[21], (self.u3_x, self.u3_y))
        self.game.display.blit(self.game.letter_list_image[21], (self.u4_x, self.u4_y))

        self.game.display.blit(self.game.letter_list_image[22], (self.v1_x, self.v1_y))
        self.game.display.blit(self.game.letter_list_image[22], (self.v2_x, self.v2_y))
        self.game.display.blit(self.game.letter_list_image[23], (self.w1_x, self.w1_y))
        self.game.display.blit(self.game.letter_list_image[23], (self.w2_x, self.w2_y))
        self.game.display.blit(self.game.letter_list_image[24], (self.x1_x, self.x1_y))
        self.game.display.blit(self.game.letter_list_image[25], (self.y1_x, self.y1_y))
        self.game.display.blit(self.game.letter_list_image[25], (self.y2_x, self.y2_y))
        self.game.display.blit(self.game.letter_list_image[26], (self.z1_x, self.z1_y))

    def go_cursor(self):
        self.game.drawing('*', 17, self.cursor_rect.x, self.cursor_rect.y)

    def b_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset()

    @staticmethod
    def exit_status():
        sys.exit()

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

    def add_pos_list(self, pos_x, pos_y, letter):
        self.game.pos_list.append(pos_x)
        self.game.pos_list.append(pos_y)
        self.game.help_pos.append(pos_x)
        self.game.help_pos.append(pos_y)
        self.game.help_pos.append(letter)
        self.game.all_pos.append(pos_x)
        self.game.all_pos.append(pos_y)
        self.game.all_pos.append(letter)

    def check_words(self):
        status, accept_words = False, []
        with open('scrabblewords.txt') as file:
            row = file.read().splitlines()
            if self.game.help_pos[0] == self.game.help_pos[3]:
                word = self.find_check_word_vert()
            else:
                word = self.find_check_word_gori()
            if word in row and word not in accept_words:
                status = True
                accept_words.append(word)
        if status:
            self.game.score += self.calculate_score()
            self.game.help_pos.clear()
        else:
            self.game.none_sound.play()

    def find_check_word_vert(self):
        list, new_list = [self.game.help_pos[d: d + 3] for d in range(0, len(self.game.help_pos), 3)], []
        all_list = [self.game.all_pos[d: d + 3] for d in range(0, len(self.game.all_pos), 3)]
        list0, list1, list2, word, word2 = [], [], [], '', ''
        if len(list) > 1:
            list = sorted(list, key=lambda x: x[1])
            var = [[new_list.append(i[1])] for i in list]
            var = [[list0.append(i[0])] for i in list]
            var = [[list1.append(i[0])] for i in all_list]
            var = [[list2.append(i[1])] for i in all_list]
            if new_list[0] - 55 in list2:
                n = - 55
                while new_list[0] + n in list2:
                    index = list2.index(new_list[0] + n)
                    if all_list[index][0] == list0[0] and all_list[index] not in list:
                        list.append(all_list[index])
                    else:
                        index += 1
                        if all_list[index][0] == list0[0] and all_list[index] not in list:
                            list.append(all_list[index])
                            break
                    n -= 55
                new_list.clear()
                var = [[new_list.append(i[1])] for i in list]
            if new_list[-1] + 55 in list2:
                n = 55
                while new_list[-1] + n in list2:
                    index = list2.index(new_list[-1] + n)
                    if all_list[index][0] == list0[0] and all_list[index] not in list:
                        list.append(all_list[index])
                    n += 55
                new_list.clear()
                var = [[new_list.append(i[1])] for i in list]
            for h in range(1, len(list)):
                list2.clear()
                list = sorted(list, key=lambda x: x[1])
                word = [''.join(i[2]) for i in list]
                for k in word:
                    word2 += ''.join(k)
                break
            return word2

    def find_check_word_gori(self):
        list, new_list = [self.game.help_pos[d: d + 3] for d in range(0, len(self.game.help_pos), 3)], []
        all_list = [self.game.all_pos[d: d + 3] for d in range(0, len(self.game.all_pos), 3)]
        list0, list1, list2, word, word2 = [], [], [], '', ''
        if len(list) > 1:
            list = sorted(list, key=lambda x: x[0])
            var = [[new_list.append(i[0])] for i in list]
            var = [[list0.append(i[1])] for i in list]
            var = [[list1.append(i[1])] for i in all_list]
            var = [[list2.append(i[0])] for i in all_list]
            if new_list[0] - 55 in list2:
                n = 55
                while new_list[0] - n in list2:
                    index = list2.index(new_list[0] - n)
                    if all_list[index][1] == list0[0] and all_list[index] not in list:
                        list.append(all_list[index])
                    else:
                        index += 1
                        if all_list[index][1] == list0[0] and len(list2) > index:
                            list.append(all_list[index])
                            break
                    n += 55
                new_list.clear()
                var = [[new_list.append(i[0])] for i in list]
            if new_list[-1] + 55 in list2:
                n = 55
                while new_list[-1] + n in list2:
                    index = list2.index(new_list[-1] + n)
                    if all_list[index][1] == list0[0] and all_list[index] not in list:
                        list.append(all_list[index])
                    n += 55
                new_list.clear()
                var = [[new_list.append(i[0])] for i in list]
            for h in range(1, len(list)):
                list2.clear()
                list = sorted(list, key=lambda x: x[0])
                word = [''.join(i[2]) for i in list]
                for k in word:
                    word2 += ''.join(k)
                break
            return word2

    def search_words(self):
        letters_list = [self.game.help_pos[d: d + 3] for d in range(0, len(self.game.help_pos), 3)]
        row_list, words, row_let = ''.join(self.game.letter_list), [], ''
        for i in letters_list:
            row_let = ''.join(i[2])
        true_row = list(row_list.replace(row_let, ''))
        with open('scrabblewords.txt') as file:
            row = file.read().splitlines()
            word = (''.join(true_row))
            if len(word) != 7:
                for j in range(2, len(word) + 1):
                    for c in permutations(word, j):
                        if ''.join(c) in row and not ''.join(c) in words:
                            words.append(self.score_search_word(c))
                            words.append(''.join(c))
            words = sorted([words[d: d + 2] for d in range(0, len(words), 2)])
        for i in words:
            self.finded_words_scores.append(i[0])
            self.finded_words.append(i[1])
        if len(words) == 0:
            self.game.none_sound.play()

    @staticmethod
    def score_search_word(word):
        score = 0
        letter_score = {"a": 1, "b": 3, "c": 3, "d": 2,
                        "e": 1, "f": 4, "g": 2, "h": 4,
                        "i": 1, "j": 8, "k": 5, "l": 1,
                        "m": 3, "n": 1, "o": 1, "p": 3,
                        "q": 10, "r": 1, "s": 1, "t": 1,
                        "u": 1, "v": 4, "w": 4, "x": 8,
                        "y": 4, "z": 10}
        for letter in word:
            score += letter_score[letter]
        return score

    def score_word(self):
        score = 0
        letter_score = {"a": 1, "b": 3, "c": 3, "d": 2,
                        "e": 1, "f": 4, "g": 2, "h": 4,
                        "i": 1, "j": 8, "k": 5, "l": 1,
                        "m": 3, "n": 1, "o": 1, "p": 3,
                        "q": 10, "r": 1, "s": 1, "t": 1,
                        "u": 1, "v": 4, "w": 4, "x": 8,
                        "y": 4, "z": 10}
        if not self.find_check_word_gori() is None:
            word = self.find_check_word_gori()
        else:
            word = self.find_check_word_vert()
        for letter in word:
            score += letter_score[letter]
        return score

    def score_word_double(self):
        score = 0
        letter_score = {"a": 2, "b": 6, "c": 6, "d": 4,
                        "e": 2, "f": 8, "g": 4, "h": 8,
                        "i": 2, "j": 16, "k": 10, "l": 2,
                        "m": 6, "n": 2, "o": 2, "p": 6,
                        "q": 20, "r": 2, "s": 2, "t": 2,
                        "u": 2, "v": 8, "w": 8, "x": 16,
                        "y": 8, "z": 20}
        if not self.find_check_word_gori() is None:
            word = self.find_check_word_gori()
        else:
            word = self.find_check_word_vert()
        for letter in word:
            score += letter_score[letter]
        return score

    def score_word_trible(self):
        score = 0
        letter_score = {"a": 3, "b": 9, "c": 9, "d": 6,
                        "e": 3, "f": 12, "g": 6, "h": 12,
                        "i": 3, "j": 24, "k": 15, "l": 3,
                        "m": 9, "n": 3, "o": 3, "p": 6,
                        "q": 30, "r": 3, "s": 3, "t": 3,
                        "u": 3, "v": 12, "w": 12, "x": 24,
                        "y": 12, "z": 30}
        if not self.find_check_word_gori() is None:
            word = self.find_check_word_gori()
        else:
            word = self.find_check_word_vert()
        for letter in word:
            score += letter_score[letter]
        return score

    def calculate_score(self):
        i, b = 0, math.trunc(len(self.game.pos_list) / 2)
        for i in range(len(self.game.pos_list)):
            self.game.pos_list[i] = math.floor(self.game.pos_list[i])
        pos_list = [self.game.pos_list[d: d + 2] for d in range(0, len(self.game.pos_list), 2)]
        i, j = 1, 0
        while i != b:
            if pos_list[j:i] == [[55, 55]]:
                self.game.score = self.score_word() * 3
            elif pos_list[j:i] == [[55 + 770, 55 + 770]]:
                self.game.score = self.score_word() * 3
            elif pos_list[j:i] == [[55 + 385, 55]]:
                self.game.score = self.score_word() * 3
            elif pos_list[j:i] == [[55 + 385, 55 + 770]]:
                self.game.score = self.score_word() * 3
            elif pos_list[j:i] == [[55 + 770, 55]]:
                self.game.score = self.score_word() * 3
            elif pos_list[j:i] == [[55, 55 + 770]]:
                self.game.score = self.score_word() * 3
            elif pos_list[j:i] == [[55, 55 + 385]]:
                self.game.score = self.score_word() * 3
            elif pos_list[j:i] == [[55 + 770, 55 + 385]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 55, 55 + 55]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 110, 55 + 110]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 165, 55 + 165]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 220, 55 + 220]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 550, 55 + 550]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 605, 55 + 605]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 660, 55 + 660]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 715, 55 + 715]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 715, 55 + 55]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 660, 55 + 110]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 605, 55 + 165]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 550, 55 + 220]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 55, 55 + 715]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 110, 55 + 660]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 165, 55 + 605]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 220, 55 + 550]]:
                self.game.score = self.score_word() * 2
            elif pos_list[j:i] == [[55 + 330, 55 + 330]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 330, 55 + 440]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 440, 55 + 330]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 440, 55 + 440]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 330, 55 + 110]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 385, 55 + 165]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 440, 55 + 110]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[830 - 335, 830 - 115]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[830 - 390, 830 - 170]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[830 - 445, 830 - 115]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 165, 55]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 605, 55]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 165, 55 + 770]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 605, 55 + 770]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 110, 55 + 330]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 110, 55 + 440]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 165, 55 + 385]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[830 - 115, 55 + 330]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[830 - 115, 55 + 440]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[830 - 170, 55 + 385]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55, 55 + 165]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55, 55 + 605]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 770, 55 + 605]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 770, 55 + 165]]:
                self.game.score = self.score_word_double()
            elif pos_list[j:i] == [[55 + 275, 55 + 275]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 495, 55 + 275]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 275, 55 + 495]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 495, 55 + 495]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 55, 55 + 495]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 495, 55 + 55]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 275, 55 + 55]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 55, 55 + 275]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 715, 55 + 275]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 715, 55 + 495]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 275, 55 + 715]]:
                self.game.score = self.score_word_trible()
            elif pos_list[j:i] == [[55 + 495, 55 + 715]]:
                self.game.score = self.score_word_trible()
            else:
                self.game.score = self.score_word()
            i += 1
            j += 1
        return self.game.score

    def save_achivement(self):
        self.game.record = self.game.score
        self.game.record_system()
        self.game.all_pos.clear()
        self.game.help_pos.clear()
        self.game.letter_list.clear()
        self.game.letter_list_img.clear()
        self.lay_out_letters.clear()
        self.lay_out_control = True
        count_letter_list = [9, 2, 2, 5, 13, 2, 3, 4, 8, 1, 1, 4, 2, 5, 8, 2, 1, 6, 5, 7, 4, 2, 2, 1, 2, 1]
        for i in range(len(self.game.count_letters_list)):
            self.game.count_letters_list[i] = count_letter_list[i]
        self.game.score = 0
        self.game.counts_letters_in_letter_list.clear()

    def count_letter_smooth(self):
        i = 0
        for i in range(25):
            if self.game.count_letters[i] == self.index_letter:
                self.game.count_letters[i] = 0
                break

    def use_bag(self):
        for c in range(len(self.game.letter_list)):
            self.game.pos_random_letter[c] = -200
        if len(self.lay_out_letters) == 0:
            self.game.contoids = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v',
                                  'w', 'x', 'y', 'z']
            self.game.vowel = ['a', 'e', 'i', 'o', 'u']
            self.game.count_letters_list = [9, 2, 2, 5, 13, 2, 3, 4, 8, 1, 1, 4, 2, 5, 8, 2, 1, 6, 5, 7, 4, 2, 2, 1, 2,
                                            1]
        self.game.letter_list.clear()
        self.game.help_pos.clear()
        self.letter_status_list = [True, True, True, True, True, True, True]
        i = 1
        for i in range(7):
            if self.game.pos_random_letter[i] < 0:
                self.letter_status = False
                self.letter_status_list[i] = self.letter_status
                if not self.letter_status_list[i]:
                    new_letter = self.game.bag_letter()
                    self.game.letter_list.append(new_letter)
                    if i == 0:
                        self.game.pos_random_letter[i] = 100
                    elif i == 1:
                        self.game.pos_random_letter[i] = 200
                    elif i == 2:
                        self.game.pos_random_letter[i] = 300
                    elif i == 3:
                        self.game.pos_random_letter[i] = 400
                    elif i == 4:
                        self.game.pos_random_letter[i] = 500
                    elif i == 5:
                        self.game.pos_random_letter[i] = 600
                    else:
                        self.game.pos_random_letter[i] = 700
                    self.game.letter_list_img[i] = self.game.letter_img_doubler


# First Page
class AnyButtonPage(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.i = 1

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            self.game.drawing('SCRABBLE', 25, self.middle_w, self.middle_h)
            if self.game.language == 'en':
                self.game.drawing('press start', self.game.font_size, self.middle_b_x,
                                  self.middle_b_y)
            else:
                self.game.drawing('Продолжить', self.game.font_size, self.middle_b_x,
                                  self.middle_b_y)
            self.game.display.blit(self.game.animation1[self.i], (self.middle_w - 128, self.middle_h - 300))
            self.i += 1
            if self.i == 20:
                self.i = 6
            self.b_screen()
            pygame.time.wait(20)

    def check_movement(self):
        if self.game.start_b or self.game.space_b:
            self.game.start_effect.play()
            self.game.curr_menu = self.game.main_menu
            self.go_display = False
        if self.game.exit_b:
            self.exit_status()


# Page main menu
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = "Start"
        self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)
        self.arrow = pygame.image.load('jpg/image/single arrow.png').convert_alpha()
        self.gear = pygame.image.load('jpg/image/single gear.png').convert_alpha()
        self.info = pygame.image.load('jpg/image/single info.png').convert_alpha()
        self.cup = pygame.image.load('jpg/image/single cup.png').convert_alpha()
        self.arrow_active = pygame.image.load('jpg/active image/arrow active.png').convert_alpha()
        self.gear_active = pygame.image.load('jpg/active image/gear active.png').convert_alpha()
        self.info_active = pygame.image.load('jpg/active image/info active.png').convert_alpha()
        self.cup_active = pygame.image.load('jpg/active image/cup active.png').convert_alpha()
        self.arrow = pygame.transform.scale(self.arrow, (60, 60))
        self.gear = pygame.transform.scale(self.gear, (50, 50))
        self.info = pygame.transform.scale(self.info, (40, 40))
        self.cup = pygame.transform.scale(self.cup, (40, 40))
        self.arrow_active = pygame.transform.scale(self.arrow_active, (60, 60))
        self.gear_active = pygame.transform.scale(self.gear_active, (50, 50))
        self.info_active = pygame.transform.scale(self.info_active, (40, 40))
        self.cup_active = pygame.transform.scale(self.cup_active, (40, 40))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.drawing('Main Menu', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing("Start", self.game.font_size, self.middle_w + 20, self.middle_h)
                self.game.drawing("Settings", self.game.font_size, self.middle_w + 20, self.middle_h + 40)
                self.game.drawing("Rules", self.game.font_size, self.middle_w + 20, self.middle_h + 80)
                self.game.drawing("Records", self.game.font_size, self.middle_w + 20, self.middle_h + 120)
            else:
                self.game.drawing('Главное меню', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing("Старт", self.game.font_size, self.middle_w + 20, self.middle_h)
                self.game.drawing("Настройки", self.game.font_size, self.middle_w + 20, self.middle_h + 40)
                self.game.drawing("Правила", self.game.font_size, self.middle_w + 20, self.middle_h + 80)
                self.game.drawing("Рекорды", self.game.font_size, self.middle_w + 20, self.middle_h + 120)
            self.game.display.blit(self.arrow, (self.middle_w - 105, self.middle_h - 30))
            self.game.display.blit(self.gear, (self.middle_w - 100, self.middle_h + 15))
            self.game.display.blit(self.info, (self.middle_w - 95, self.middle_h + 60))
            self.game.display.blit(self.cup, (self.middle_w - 95, self.middle_h + 100))
            if self.title == 'Start':
                self.game.display.blit(self.arrow_active, (self.middle_w - 105, self.middle_h - 30))
            elif self.title == 'Settings':
                self.game.display.blit(self.gear_active, (self.middle_w - 100, self.middle_h + 15))
            elif self.title == 'Rules':
                self.game.display.blit(self.info_active, (self.middle_w - 95, self.middle_h + 60))
            else:
                self.game.display.blit(self.cup_active, (self.middle_w - 95, self.middle_h + 100))
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
                self.game.curr_menu = self.game.start
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


# Page the game
class Start(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'to board'
        self.cursor_rect.midtop = (1050 + (- 100), 100)
        self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.b1, self.b2, self.c1, self.c2, self.d1, self.d2, self.d3, self.d4, self.d5, self.e1, self.e2, self.e3, self.e4, \
        self.e5, self.e6, self.e7, self.e8, self.e9, self.e10, self.e11, self.e12, self.e13, self.f1, self.f2, self.g1, self.g2, self.g3, self.h1, self.h2, self.h3, self.h4, self.j1, self.k1, self.i1, self.i2, \
        self.i3, self.i4, self.i5, self.i6, self.i7, self.i8, self.l1, self.l2, self.l3, self.l4, self.m1, self.m2, self.n1, self.n2, self.n3, self.n4, self.n5, self.o1, self.o2, self.o3, self.o4, self.o5, \
        self.o6, self.o7, self.o8, self.p1, self.p2, self.q1, self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.s1, self.s2, self.s3, self.s4, self.s5, self.t1, self.t2, self.t3, self.t4, self.t5, \
        self.t6, self.t7, self.u1, self.u2, self.u3, self.u4, self.v1, self.v2, self.w1, self.w2, self.x1, self.y1, self.y2, self.z1 = True, True, True, True, True, True, True, True, True, True, True, True, True, \
                                                                                                                                       True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, \
                                                                                                                                       True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, \
                                                                                                                                       True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True
        self.i_board = pygame.image.load('jpg/image/single board.png').convert_alpha()
        self.i_bag = pygame.image.load('jpg/image/bag.png').convert_alpha()
        self.lens = pygame.image.load('jpg/image/single lens.png').convert_alpha()
        self.lamp = pygame.image.load('jpg/image/single lamp.png').convert_alpha()
        self.next_arrow = pygame.image.load('jpg/image/single next arrow.png').convert_alpha()
        self.i_board_active = pygame.image.load('jpg/active image/active board.png').convert_alpha()
        self.i_bag_active = pygame.image.load('jpg/active image/bag active.png').convert_alpha()
        self.lens_active = pygame.image.load('jpg/active image/active lens.png').convert_alpha()
        self.lamp_active = pygame.image.load('jpg/active image/lamp active.png').convert_alpha()
        self.next_arrow_active = pygame.image.load('jpg/active image/next arrow active.png').convert_alpha()
        self.i_board = pygame.transform.scale(self.i_board, (50, 50))
        self.i_bag = pygame.transform.scale(self.i_bag, (70, 70))
        self.lens = pygame.transform.scale(self.lens, (50, 50))
        self.lamp = pygame.transform.scale(self.lamp, (90, 90))
        self.next_arrow = pygame.transform.scale(self.next_arrow, (90, 90))
        self.i_board_active = pygame.transform.scale(self.i_board_active, (50, 50))
        self.i_bag_active = pygame.transform.scale(self.i_bag_active, (70, 70))
        self.lens_active = pygame.transform.scale(self.lens_active, (50, 50))
        self.lamp_active = pygame.transform.scale(self.lamp_active, (90, 90))
        self.next_arrow_active = pygame.transform.scale(self.next_arrow_active, (90, 90))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_game()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            self.game.display.blit(self.game.score_panel, (self.middle_w + 660, self.middle_h - 580))
            self.game.draw_board()
            self.game.display.blit(self.game.cursor_board, (self.board_cur_x, self.board_cur_y))  # 45 55
            self.draw_box()
            if self.game.language == 'en':
                self.game.drawing('to board', self.game.font_size, 1050, 100)
                self.game.drawing('bag', self.game.font_size, 1050, 200)
                self.game.drawing('check', self.game.font_size, 1050, 300)
                self.game.drawing('tips', self.game.font_size, 1050, 400)
                self.game.drawing('finish', self.game.font_size, 1050, 500)
                self.game.drawing('score', self.game.font_size, 1400, 335)
                self.game.drawing('words', self.game.font_size, 1600, 335)
            else:
                self.game.drawing('к доске', self.game.font_size, 1050, 100)
                self.game.drawing('мешок', self.game.font_size, 1050, 200)
                self.game.drawing('проверка', self.game.font_size, 1050, 300)
                self.game.drawing('помощь', self.game.font_size, 1050, 400)
                self.game.drawing('итог', self.game.font_size, 1050, 500)
                self.game.drawing('очки', self.game.font_size, 1400, 335)
                self.game.drawing('слова', self.game.font_size, 1600, 335)
            self.game.display.blit(self.i_board, (948, 75))
            self.game.display.blit(self.i_bag, (940, 160))
            self.game.display.blit(self.lens, (950, 270))
            self.game.display.blit(self.lamp, (933, 350))
            self.game.display.blit(self.next_arrow, (933, 450))
            if self.title == 'to board':
                self.game.display.blit(self.i_board_active, (948, 75))
            elif self.title == 'bag':
                self.game.display.blit(self.i_bag_active, (940, 160))
            elif self.title == 'check':
                self.game.display.blit(self.lens_active, (950, 270))
            elif self.title == 'tips':
                self.game.display.blit(self.lamp_active, (933, 350))
            else:
                self.game.display.blit(self.next_arrow_active, (933, 450))
            self.draw_finded_words()
            self.game.drawing(f'{self.game.score}', self.game.font_size, 1775, 90)
            self.cur_x, self.cur_y = math.trunc(self.board_cur_x + self.pos_x), math.trunc(
                self.board_cur_y + self.pos_y)
            for i in range(len(self.game.letter_list)):
                self.game.display.blit(self.game.letter_list_img[i], (self.game.pos_random_letter[i], 950))

            self.go_cursor()
            self.b_screen()

    def draw_finded_words(self):
        words = []
        high = 435
        for ii in reversed(self.finded_words[-5:]):
            if ii not in words:
                self.game.drawing(f'{ii}', self.game.font_size, 1600, high)
                words.append(ii)
                high += 100
        high = 435
        for iii in reversed(self.finded_words_scores[-5:]):
            self.game.drawing(f'{iii}', self.game.font_size, 1400, high)
            high += 100

    def movement_in_game(self):
        if not self.movement_board and self.game.arrow_down:
            if self.title == 'to board':
                self.title = 'bag'
                self.cursor_rect.midtop = (1050 + (- 100), 200)
            elif self.title == 'bag':
                self.title = 'check'
                self.cursor_rect.midtop = (1050 + (- 100), 300)
            elif self.title == 'check':
                self.title = 'tips'
                self.cursor_rect.midtop = (1050 + (- 100), 400)
            elif self.title == 'tips':
                self.title = 'finish'
                self.cursor_rect.midtop = (1050 + (- 100), 500)
            elif self.title == 'finish':
                self.title = 'to board'
                self.cursor_rect.midtop = (1050 + (- 100), 100)
            self.game.menu_effect.play()
        elif not self.movement_board and self.game.arrow_up:
            if self.title == 'to board':
                self.title = 'finish'
                self.cursor_rect.midtop = (1050 + (- 100), 500)
            elif self.title == 'finish':
                self.title = 'tips'
                self.cursor_rect.midtop = (1050 + (- 100), 400)
            elif self.title == 'tips':
                self.title = 'check'
                self.cursor_rect.midtop = (1050 + (- 100), 300)
            elif self.title == 'check':
                self.title = 'bag'
                self.cursor_rect.midtop = (1050 + (- 100), 200)
            elif self.title == 'bag':
                self.title = 'to board'
                self.cursor_rect.midtop = (1050 + (- 100), 100)
            self.game.menu_effect.play()

        elif self.movement_board and self.game.arrow_up and 767 >= self.board_cur_y > -2:
            self.board_cur_y -= 55
            self.game.move_cursor_effect.play()
        elif self.movement_board and self.game.arrow_down and 766 > self.board_cur_y > -3.3:
            self.board_cur_y += 55
            self.game.move_cursor_effect.play()
        elif self.movement_board and self.game.arrow_right and 760 > self.board_cur_x > -11:
            self.board_cur_x += 55
            self.game.move_cursor_effect.play()
        elif self.movement_board and self.game.arrow_left and 761 > self.board_cur_x > -10:
            self.board_cur_x -= 55
            self.game.move_cursor_effect.play()
        elif self.movement_board and self.game.pause_b:
            self.movement_board = False
            self.cursor_rect.midtop = (1050 + (- 100), 100)

        if self.movement_board and self.game.a_b and self.game.count_letters[0] > 0:
            if self.lay_out_control and self.a1:
                self.board_cur_x, self.board_cur_y, self.a1_x, self.a1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.lay_out_control, self.a1 = False, False
                self.lay_out_letters.append('a1')
                self.game.count_letters[0] -= 1
                self.game.hide_letter('a')
                self.add_pos_list(math.trunc(self.a1_x), math.trunc(self.a1_y), 'a')

            elif self.a1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.a1_x, self.a1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.a1 = False
                    self.lay_out_letters.append('a1')
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a1_x), math.trunc(self.a1_y), 'a')

            elif not self.a1 and self.a2:
                if not self.noheap():
                    self.a2_x, self.a2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('a2')
                    self.a2 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a2_x), math.trunc(self.a2_y), 'a')

            elif not self.a1 and not self.a2 and self.a3:
                if not self.noheap():
                    self.a3_x, self.a3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('a3')
                    self.a3 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a3_x), math.trunc(self.a3_y), 'a')

            elif not self.a1 and not self.a2 and not self.a3 and self.a4:
                if not self.noheap():
                    self.a4_x, self.a4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('a4')
                    self.a4 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a4_x), math.trunc(self.a4_y), 'a')

            elif not self.a1 and not self.a2 and not self.a3 and not self.a4 and self.a5:
                if not self.noheap():
                    self.a5_x, self.a5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('a5')
                    self.a5 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a5_x), math.trunc(self.a5_y), 'a')

            elif not self.a1 and not self.a2 and not self.a3 and not self.a4 and not self.a5 and self.a6:
                if not self.noheap():
                    self.a6_x, self.a6_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('a6')
                    self.a6 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a6_x), math.trunc(self.a6_y), 'a')

            elif not self.a1 and not self.a2 and not self.a3 and not self.a4 and not self.a5 and not self.a6 and self.a7:
                if not self.noheap():
                    self.a7_x, self.a7_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('a7')
                    self.a7 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a7_x), math.trunc(self.a7_y), 'a')

            elif not self.a1 and not self.a2 and not self.a3 and not self.a4 and not self.a5 and not self.a6 and not self.a7 and self.a8:
                if not self.noheap():
                    self.a8_x, self.a8_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('a8')
                    self.a8 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a8_x), math.trunc(self.a8_y), 'a')

            elif not self.a1 and not self.a2 and not self.a3 and not self.a4 and not self.a5 and not self.a6 and not self.a7 and not self.a8 and self.a9:
                if not self.noheap():
                    self.a9_x, self.a9_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('a9')
                    self.a9 = False
                    self.game.count_letters[0] -= 1
                    self.game.hide_letter('a')
                    self.add_pos_list(math.trunc(self.a9_x), math.trunc(self.a9_y), 'a')

        if self.movement_board and self.game.b_b and self.game.count_letters[1] > 0:
            if self.lay_out_control and self.b1:
                self.lay_out_control, self.b1 = False, False
                self.lay_out_letters.append('b1')
                self.board_cur_x, self.board_cur_y, self.b1_x, self.b1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[1] -= 1
                self.game.hide_letter('b')
                self.add_pos_list(math.trunc(self.b1_x), math.trunc(self.b1_y), 'b')

            elif not self.lay_out_control and self.b1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.b1_x, self.b1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('b1')
                    self.b1 = False
                    self.game.count_letters[1] -= 1
                    self.game.hide_letter('b')
                    self.add_pos_list(math.trunc(self.b1_x), math.trunc(self.b1_y), 'b')

            elif not self.b1 and self.b2:
                if not self.noheap():
                    self.b2_x, self.b2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('b2')
                    self.b2 = False
                    self.game.count_letters[1] -= 1
                    self.game.hide_letter('b')
                    self.add_pos_list(math.trunc(self.b2_x), math.trunc(self.b2_y), 'b')

        if self.movement_board and self.game.c_b and self.game.count_letters[2] > 0:
            if self.lay_out_control and self.c1:
                self.lay_out_control, self.c1 = False, False
                self.lay_out_letters.append('c1')
                self.board_cur_x, self.board_cur_y, self.c1_x, self.c1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[2] -= 1
                self.game.hide_letter('c')
                self.add_pos_list(math.trunc(self.c1_x), math.trunc(self.c1_y), 'c')

            elif not self.lay_out_control and self.c1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.c1_x, self.c1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('c1')
                    self.c1 = False
                    self.game.count_letters[2] -= 1
                    self.game.hide_letter('c')
                    self.add_pos_list(math.trunc(self.c1_x), math.trunc(self.c1_y), 'c')

            elif not self.c1 and self.c2:
                if not self.noheap():
                    self.c2_x, self.c2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('c2')
                    self.c2 = False
                    self.game.count_letters[2] -= 1
                    self.game.hide_letter('c')
                    self.add_pos_list(math.trunc(self.c2_x), math.trunc(self.c2_y), 'c')

        if self.movement_board and self.game.d_b and self.game.count_letters[3] > 0:
            if self.lay_out_control and self.d1:
                self.lay_out_control, self.d1 = False, False
                self.lay_out_letters.append('d1')
                self.board_cur_x, self.board_cur_y, self.d1_x, self.d1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[3] -= 1
                self.game.hide_letter('d')
                self.add_pos_list(math.trunc(self.d1_x), math.trunc(self.d1_y), 'd')

            elif not self.lay_out_control and self.d1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.d1_x, self.d1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('d1')
                    self.d1 = False
                    self.game.count_letters[3] -= 1
                    self.game.hide_letter('d')
                    self.add_pos_list(math.trunc(self.d1_x), math.trunc(self.d1_y), 'd')

            elif not self.d1 and self.d2:
                if not self.noheap():
                    self.d2_x, self.d2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('d2')
                    self.d2 = False
                    self.game.count_letters[3] -= 1
                    self.game.hide_letter('d')
                    self.add_pos_list(math.trunc(self.d2_x), math.trunc(self.d2_y), 'd')

            elif not self.d1 and not self.d2 and self.d3:
                if not self.noheap():
                    self.d3_x, self.d3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('d3')
                    self.d3 = False
                    self.game.count_letters[3] -= 1
                    self.game.hide_letter('d')
                    self.add_pos_list(math.trunc(self.d3_x), math.trunc(self.d3_y), 'd')

            elif not self.d1 and not self.d2 and not self.d3 and self.d4:
                if not self.noheap():
                    self.d4_x, self.d4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('d4')
                    self.d4 = False
                    self.game.count_letters[3] -= 1
                    self.game.hide_letter('d')
                    self.add_pos_list(math.trunc(self.d4_x), math.trunc(self.d4_y), 'd')

            elif not self.d1 and not self.d2 and not self.d3 and not self.d4 and self.d5:
                if not self.noheap():
                    self.d5_x, self.d5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('d5')
                    self.d5 = False
                    self.game.count_letters[3] -= 1
                    self.game.hide_letter('d')
                    self.add_pos_list(math.trunc(self.d5_x), math.trunc(self.d5_y), 'd')

        elif self.movement_board and self.game.e_b and self.game.count_letters[4] > 0:
            if self.lay_out_control and self.e1:
                self.lay_out_control, self.e1 = False, False
                self.lay_out_letters.append('e1')
                self.board_cur_x, self.board_cur_y, self.e1_x, self.e1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[4] -= 1
                self.game.hide_letter('e')
                self.add_pos_list(math.trunc(self.e1_x), math.trunc(self.e1_y), 'e')

            elif not self.lay_out_control and self.e1 and len(self.lay_out_letters) >= 1:

                if not self.noheap():
                    self.e1_x, self.e1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('e1')
                    self.e1 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e1_x), math.trunc(self.e1_y), 'e')

            elif not self.e1 and self.e2:
                if not self.noheap():
                    self.e2_x, self.e2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('e2')
                    self.e2 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e2_x), math.trunc(self.e2_y), 'e')

            elif not self.e1 and not self.e2 and self.e3:
                if not self.noheap():
                    self.e3_x, self.e3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e3')
                    self.e3 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e3_x), math.trunc(self.e3_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and self.e4:
                if not self.noheap():
                    self.e4_x, self.e4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e4')
                    self.e4 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e4_x), math.trunc(self.e4_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and self.e5:
                if not self.noheap():
                    self.e5_x, self.e5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e5')
                    self.e5 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e5_x), math.trunc(self.e5_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and self.e6:
                if not self.noheap():
                    self.e6_x, self.e6_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e6')
                    self.e6 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e6_x), math.trunc(self.e6_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and not self.e6 and self.e7:
                if not self.noheap():
                    self.e7_x, self.e7_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e7')
                    self.e7 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e7_x), math.trunc(self.e7_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and not self.e6 and not self.e7 and self.e8:
                if not self.noheap():
                    self.e8_x, self.e8_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e8')
                    self.e8 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e8_x), math.trunc(self.e8_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and not self.e6 and not self.e7 and not self.e8 and self.e9:
                if not self.noheap():
                    self.e9_x, self.e9_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e9')
                    self.e9 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e9_x), math.trunc(self.e9_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and not self.e6 and not self.e7 and not self.e8 and not self.e9 and self.e10:
                if not self.noheap():
                    self.e10_x, self.e10_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e10')
                    self.e10 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e10_x), math.trunc(self.e10_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and not self.e6 and not self.e7 and not self.e8 and not self.e9 and not self.e10 and self.e11:
                if not self.noheap():
                    self.e11_x, self.e11_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e11')
                    self.e11 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e11_x), math.trunc(self.e11_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and not self.e6 and not self.e7 and not self.e8 and not self.e9 and not self.e10 and not self.e11 and self.e12:
                if not self.noheap():
                    self.e12_x, self.e12_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e12')
                    self.e12 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e12_x), math.trunc(self.e12_y), 'e')

            elif not self.e1 and not self.e2 and not self.e3 and not self.e4 and not self.e5 and not self.e6 and not self.e7 and not self.e8 and not self.e9 and not self.e10 and not self.e11 and not self.e12 and self.e13:
                if not self.noheap():
                    self.e13_x, self.e13_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('e13')
                    self.e13 = False
                    self.game.count_letters[4] -= 1
                    self.game.hide_letter('e')
                    self.add_pos_list(math.trunc(self.e13_x), math.trunc(self.e13_y), 'e')

        elif self.movement_board and self.game.f_b and self.game.count_letters[5] > 0:
            if self.lay_out_control and self.f1:
                self.lay_out_control, self.f1 = False, False
                self.lay_out_letters.append('f1')
                self.board_cur_x, self.board_cur_y, self.f1_x, self.f1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[5] -= 1
                self.game.hide_letter('f')
                self.add_pos_list(math.trunc(self.f1_x), math.trunc(self.f1_y), 'f')

            elif not self.lay_out_control and self.f1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.f1_x, self.f1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('f1')
                    self.f1 = False
                    self.game.count_letters[5] -= 1
                    self.game.hide_letter('f')
                    self.add_pos_list(math.trunc(self.f1_x), math.trunc(self.f1_y), 'f')

            elif not self.f1 and self.f2:
                if not self.noheap():
                    self.f2_x, self.f2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('f2')
                    self.f2 = False
                    self.game.count_letters[5] -= 1
                    self.game.hide_letter('f')
                    self.add_pos_list(math.trunc(self.f2_x), math.trunc(self.f2_y), 'f')

        elif self.movement_board and self.game.g_b and self.game.count_letters[6] > 0:
            if self.lay_out_control and self.g1:
                self.lay_out_control, self.g1 = False, False
                self.lay_out_letters.append('g1')
                self.board_cur_x, self.board_cur_y, self.g1_x, self.g1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[6] -= 1
                self.game.hide_letter('g')
                self.add_pos_list(math.trunc(self.g1_x), math.trunc(self.g1_y), 'g')

            elif not self.lay_out_control and self.g1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.g1_x, self.g1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('g1')
                    self.g1 = False
                    self.game.count_letters[6] -= 1
                    self.game.hide_letter('g')
                    self.add_pos_list(math.trunc(self.g1_x), math.trunc(self.g1_y), 'g')

            elif not self.g1 and self.g2:
                if not self.noheap():
                    self.g2_x, self.g2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('g2')
                    self.g2 = False
                    self.game.count_letters[6] -= 1
                    self.game.hide_letter('g')
                    self.add_pos_list(math.trunc(self.g2_x), math.trunc(self.g2_y), 'g')

            elif not self.g1 and not self.g2 and self.g3:
                if not self.noheap():
                    self.g3_x, self.g3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('g3')
                    self.g3 = False
                    self.game.count_letters[6] -= 1
                    self.game.hide_letter('g')
                    self.add_pos_list(math.trunc(self.g3_x), math.trunc(self.g3_y), 'g')

        elif self.movement_board and self.game.h_b and self.game.count_letters[7] > 0:
            if self.lay_out_control and self.h1:
                self.lay_out_letters.append('h1')
                self.board_cur_x, self.board_cur_y, self.h1_x, self.h1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.h1 = False
                self.game.count_letters[7] -= 1
                self.game.hide_letter('h')
                self.add_pos_list(math.trunc(self.h1_x), math.trunc(self.h1_y), 'h')

            elif not self.lay_out_control and self.h1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.h1_x, self.h1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('h1')
                    self.h1 = False
                    self.game.count_letters[7] -= 1
                    self.game.hide_letter('h')
                    self.add_pos_list(math.trunc(self.h1_x), math.trunc(self.h1_y), 'h')

            elif not self.h1 and self.h2:
                if not self.noheap():
                    self.h2_x, self.h2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('h2')
                    self.h2 = False
                    self.game.count_letters[7] -= 1
                    self.game.hide_letter('h')
                    self.add_pos_list(math.trunc(self.h2_x), math.trunc(self.h2_y), 'h')

            elif not self.h1 and not self.h2 and self.h3:
                if not self.noheap():
                    self.h3_x, self.h3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('h3')
                    self.h3 = False
                    self.game.count_letters[7] -= 1
                    self.game.hide_letter('h')
                    self.add_pos_list(math.trunc(self.h3_x), math.trunc(self.h3_y), 'h')

            elif not self.h1 and not self.h2 and not self.h3 and self.h4:
                if not self.noheap():
                    self.h4_x, self.h4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('h4')
                    self.h4 = False
                    self.game.count_letters[7] -= 1
                    self.game.hide_letter('h')
                    self.add_pos_list(math.trunc(self.h4_x), math.trunc(self.h4_y), 'h')

        elif self.movement_board and self.game.i_b and self.game.count_letters[8] > 0:
            if self.lay_out_control and self.i1:
                self.lay_out_control, self.i1 = False, False
                self.lay_out_letters.append('i1')
                self.board_cur_x, self.board_cur_y, self.i1_x, self.i1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[8] -= 1
                self.game.hide_letter('i')
                self.add_pos_list(math.trunc(self.i1_x), math.trunc(self.i1_y), 'i')

            elif not self.lay_out_control and self.i1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.i1_x, self.i1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('i1')
                    self.i1 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i1_x), math.trunc(self.i1_y), 'i')

            elif not self.i1 and self.i2:
                if not self.noheap():
                    self.i2_x, self.i2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('i2')
                    self.i2 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i2_x), math.trunc(self.i2_y), 'i')

            elif not self.i1 and not self.i2 and self.i3:
                if not self.noheap():
                    self.i3_x, self.i3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('i3')
                    self.i3 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i3_x), math.trunc(self.i3_y), 'i')

            elif not self.i1 and not self.i2 and not self.i3 and self.i4:
                if not self.noheap():
                    self.i4_x, self.i4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('i4')
                    self.i4 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i4_x), math.trunc(self.i4_y), 'i')

            elif not self.i1 and not self.i2 and not self.i3 and not self.i4 and self.i5:
                if not self.noheap():
                    self.i5_x, self.i5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('i5')
                    self.i5 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i5_x), math.trunc(self.i5_y), 'i')

            elif not self.i1 and not self.i2 and not self.i3 and not self.i4 and not self.i5 and self.i6:
                if not self.noheap():
                    self.i6_x, self.i6_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('i6')
                    self.i6 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i6_x), math.trunc(self.i6_y), 'i')

            elif not self.i1 and not self.i2 and not self.i3 and not self.i4 and not self.i5 and not self.i6 and self.i7:
                if not self.noheap():
                    self.i7_x, self.i7_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('i7')
                    self.i7 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i7_x), math.trunc(self.i7_y), 'i')

            elif not self.i1 and not self.i2 and not self.i3 and not self.i4 and not self.i5 and not self.i6 and not self.i7 and self.i8:
                if not self.noheap():
                    self.i8_x, self.i8_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('i8')
                    self.i8 = False
                    self.game.count_letters[8] -= 1
                    self.game.hide_letter('i')
                    self.add_pos_list(math.trunc(self.i8_x), math.trunc(self.i8_y), 'i')

        elif self.movement_board and self.game.j_b and self.game.count_letters[9] > 0:
            if self.lay_out_control and self.j1:
                self.lay_out_control, self.j1 = False, False
                self.lay_out_letters.append('j1')
                self.board_cur_x, self.board_cur_y, self.j1_x, self.j1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[9] -= 1
                self.game.hide_letter('j')
                self.add_pos_list(math.trunc(self.j1_x), math.trunc(self.j1_y), 'j')

            elif not self.lay_out_control and self.j1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.j1_x, self.j1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('j1')
                    self.j1 = False
                    self.game.count_letters[9] -= 1
                    self.game.hide_letter('j')
                    self.add_pos_list(math.trunc(self.j1_x), math.trunc(self.j1_y), 'j')

        elif self.movement_board and self.game.k_b and self.game.count_letters[10] > 0:
            if self.lay_out_control and self.k1:
                self.lay_out_control, self.k1 = False, False
                self.lay_out_letters.append('k1')
                self.board_cur_x, self.board_cur_y, self.k1_x, self.k1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[10] -= 1
                self.game.hide_letter('k')
                self.add_pos_list(math.trunc(self.k1_x), math.trunc(self.k1_y), 'k')

            elif not self.lay_out_control and self.k1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.k1_x, self.k1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('k1')
                    self.k1 = False
                    self.game.count_letters[10] -= 1
                    self.game.hide_letter('k')
                    self.add_pos_list(math.trunc(self.k1_x), math.trunc(self.k1_y), 'k')

        elif self.movement_board and self.game.l_b and self.game.count_letters[11] > 0:
            if self.lay_out_control and self.l1:
                self.lay_out_control, self.l1 = False, False
                self.lay_out_letters.append('l1')
                self.board_cur_x, self.board_cur_y, self.l1_x, self.l1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[11] -= 1
                self.game.hide_letter('l')
                self.add_pos_list(math.trunc(self.l1_x), math.trunc(self.l1_y), 'k')

            elif not self.lay_out_control and self.l1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.l1_x, self.l1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('l1')
                    self.l1 = False
                    self.game.count_letters[11] -= 1
                    self.game.hide_letter('l')
                    self.add_pos_list(math.trunc(self.l1_x), math.trunc(self.l1_y), 'l')

            elif not self.l1 and self.l2:
                if not self.noheap():
                    self.l2_x, self.l2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('l2')
                    self.l2 = False
                    self.game.count_letters[11] -= 1
                    self.game.hide_letter('l')
                    self.add_pos_list(math.trunc(self.l2_x), math.trunc(self.l2_y), 'l')

            elif not self.l1 and not self.l2 and self.l3:
                if not self.noheap():
                    self.l3_x, self.l3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('l3')
                    self.l3 = False
                    self.game.count_letters[11] -= 1
                    self.game.hide_letter('l')
                    self.add_pos_list(math.trunc(self.l3_x), math.trunc(self.l3_y), 'l')

            elif not self.l1 and not self.l2 and not self.l3 and self.l4:
                if not self.noheap():
                    self.l4_x, self.l4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('l4')
                    self.l4 = False
                    self.game.count_letters[11] -= 1
                    self.game.hide_letter('l')
                    self.add_pos_list(math.trunc(self.l4_x), math.trunc(self.l4_y), 'l')

        elif self.movement_board and self.game.m_b and self.game.count_letters[12] > 0:
            if self.lay_out_control and self.m1:
                self.lay_out_control, self.m1 = False, False
                self.lay_out_letters.append('m1')
                self.board_cur_x, self.board_cur_y, self.m1_x, self.m1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[12] -= 1
                self.game.hide_letter('m')
                self.add_pos_list(math.trunc(self.m1_x), math.trunc(self.m1_y), 'm')

            elif not self.lay_out_control and self.m1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.m1_x, self.m1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('m1')
                    self.m1 = False
                    self.game.count_letters[12] -= 1
                    self.game.hide_letter('m')
                    self.add_pos_list(math.trunc(self.m1_x), math.trunc(self.m1_y), 'm')

            elif not self.m1 and self.m2:
                if not self.noheap():
                    self.m2_x, self.m2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('m2')
                    self.m2 = False
                    self.game.count_letters[12] -= 1
                    self.game.hide_letter('m')
                    self.add_pos_list(math.trunc(self.m2_x), math.trunc(self.m2_y), 'm')

        elif self.movement_board and self.game.n_b and self.game.count_letters[13] > 0:
            if self.lay_out_control and self.n1:
                self.lay_out_control, self.n1 = False, False
                self.lay_out_letters.append('n1')
                self.board_cur_x, self.board_cur_y, self.n1_x, self.n1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[13] -= 1
                self.game.hide_letter('n')
                self.add_pos_list(math.trunc(self.n1_x), math.trunc(self.n1_y), 'n')

            elif not self.lay_out_control and self.n1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.n1_x, self.n1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('n1')
                    self.n1 = False
                    self.game.count_letters[13] -= 1
                    self.game.hide_letter('n')
                    self.add_pos_list(math.trunc(self.n1_x), math.trunc(self.n1_y), 'n')

            elif not self.n1 and self.n2:
                if not self.noheap():
                    self.n2_x, self.n2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('n2')
                    self.n2 = False
                    self.game.count_letters[13] -= 1
                    self.game.hide_letter('n')
                    self.add_pos_list(math.trunc(self.n2_x), math.trunc(self.n2_y), 'n')

            elif not self.n1 and not self.n2 and self.n3:
                if not self.noheap():
                    self.n3_x, self.n3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('n3')
                    self.n3 = False
                    self.game.count_letters[13] -= 1
                    self.game.hide_letter('n')
                    self.add_pos_list(math.trunc(self.n3_x), math.trunc(self.n3_y), 'n')

            elif not self.n1 and not self.n2 and not self.n3 and self.n4:
                if not self.noheap():
                    self.n4_x, self.n4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('n4')
                    self.n4 = False
                    self.game.count_letters[13] -= 1
                    self.game.hide_letter('n')
                    self.add_pos_list(math.trunc(self.n4_x), math.trunc(self.n4_y), 'n')

            elif not self.n1 and not self.n2 and not self.n3 and not self.n4 and self.n5:
                if not self.noheap():
                    self.n5_x, self.n5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('n5')
                    self.n5 = False
                    self.game.count_letters[13] -= 1
                    self.game.hide_letter('n')
                    self.add_pos_list(math.trunc(self.n5_x), math.trunc(self.n5_y), 'n')

        elif self.movement_board and self.game.o_b and self.game.count_letters[14] > 0:
            if self.lay_out_control and self.o1:
                self.lay_out_control, self.o1 = False, False
                self.lay_out_letters.append('o1')
                self.board_cur_x, self.board_cur_y, self.o1_x, self.o1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[14] -= 1
                self.game.hide_letter('o')
                self.add_pos_list(math.trunc(self.o1_x), math.trunc(self.o1_y), 'o')

            elif not self.lay_out_control and self.o1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.o1_x, self.o1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('o1')
                    self.o1 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o1_x), math.trunc(self.o1_y), 'o')

            elif not self.o1 and self.o2:
                if not self.noheap():
                    self.o2_x, self.o2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('o2')
                    self.o2 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o2_x), math.trunc(self.o2_y), 'o')

            elif not self.o1 and not self.o2 and self.o3:
                if not self.noheap():
                    self.o3_x, self.o3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('o3')
                    self.o3 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o3_x), math.trunc(self.o3_y), 'o')

            elif not self.o1 and not self.o2 and not self.o3 and self.o4:
                if not self.noheap():
                    self.o4_x, self.o4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('o4')
                    self.o4 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o4_x), math.trunc(self.o4_y), 'o')

            elif not self.o1 and not self.o2 and not self.o3 and not self.o4 and self.o5:
                if not self.noheap():
                    self.o5_x, self.o5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('o5')
                    self.o5 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o5_x), math.trunc(self.o5_y), 'o')

            elif not self.o1 and not self.o2 and not self.o3 and not self.o4 and not self.o5 and self.o6:
                if not self.noheap():
                    self.o6_x, self.o6_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('o6')
                    self.o6 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o6_x), math.trunc(self.o6_y), 'o')

            elif not self.o1 and not self.o2 and not self.o3 and not self.o4 and not self.o5 and not self.o6 and self.o7:
                if not self.noheap():
                    self.o7_x, self.o7_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('o7')
                    self.o7 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o7_x), math.trunc(self.o7_y), 'o')

            elif not self.o1 and not self.o2 and not self.o3 and not self.o4 and not self.o5 and not self.o6 and not self.o7 and self.o8:
                if not self.noheap():
                    self.o8_x, self.o8_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('o8')
                    self.o8 = False
                    self.game.count_letters[14] -= 1
                    self.game.hide_letter('o')
                    self.add_pos_list(math.trunc(self.o8_x), math.trunc(self.o8_y), 'o')

        elif self.movement_board and self.game.p_b and self.game.count_letters[15] > 0:
            if self.lay_out_control and self.p1:
                self.lay_out_control, self.p1 = False, False
                self.lay_out_letters.append('p1')
                self.board_cur_x, self.board_cur_y, self.p1_x, self.p1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[15] -= 1
                self.game.hide_letter('p')
                self.add_pos_list(math.trunc(self.p1_x), math.trunc(self.p1_y), 'p')

            elif not self.lay_out_control and self.p1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('p1')
                    self.p1_x, self.p1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.p1 = False
                    self.game.count_letters[15] -= 1
                    self.game.hide_letter('p')
                    self.add_pos_list(math.trunc(self.p1_x), math.trunc(self.p1_y), 'p')

            elif not self.p1 and self.p2:
                if not self.noheap():
                    self.p2_x, self.p2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('p2')
                    self.p2 = False
                    self.game.count_letters[15] -= 1
                    self.game.hide_letter('p')
                    self.add_pos_list(math.trunc(self.p2_x), math.trunc(self.p2_y), 'p')

        elif self.movement_board and self.game.q_b and self.game.count_letters[16] > 0:
            if self.lay_out_control and self.q1:
                self.lay_out_control, self.q1 = False, False
                self.lay_out_letters.append('q1')
                self.board_cur_x, self.board_cur_y, self.q1_x, self.q1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[16] -= 1
                self.game.hide_letter('q')
                self.add_pos_list(math.trunc(self.q1_x), math.trunc(self.q1_y), 'q')

            elif not self.lay_out_control and self.q1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('q1')
                    self.q1_x, self.q1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.q1 = False
                    self.game.count_letters[16] -= 1
                    self.game.hide_letter('q')
                    self.add_pos_list(math.trunc(self.q1_x), math.trunc(self.q1_y), 'q')

        elif self.movement_board and self.game.r_b and self.game.count_letters[17] > 0:
            if self.lay_out_control and self.r1:
                self.lay_out_control, self.r1 = False, False
                self.lay_out_letters.append('r1')
                self.board_cur_x, self.board_cur_y, self.r1_x, self.r1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[17] -= 1
                self.game.hide_letter('r')
                self.add_pos_list(math.trunc(self.r1_x), math.trunc(self.r1_y), 'r')

            elif not self.lay_out_control and self.r1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('r1')
                    self.r1_x, self.r1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.r1 = False
                    self.game.count_letters[17] -= 1
                    self.game.hide_letter('r')
                    self.add_pos_list(math.trunc(self.r1_x), math.trunc(self.r1_y), 'r')

            elif not self.r1 and self.r2:
                if not self.noheap():
                    self.r2_x, self.r2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('r2')
                    self.r2 = False
                    self.game.count_letters[17] -= 1
                    self.game.hide_letter('r')
                    self.add_pos_list(math.trunc(self.r2_x), math.trunc(self.r2_y), 'r')

            elif not self.r1 and not self.r2 and self.r3:
                if not self.noheap():
                    self.r3_x, self.r3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('r3')
                    self.r3 = False
                    self.game.count_letters[17] -= 1
                    self.game.hide_letter('r')
                    self.add_pos_list(math.trunc(self.r3_x), math.trunc(self.r3_y), 'r')

            elif not self.r1 and not self.r2 and not self.r3 and self.r4:
                if not self.noheap():
                    self.r4_x, self.r4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('r4')
                    self.r4 = False
                    self.game.count_letters[17] -= 1
                    self.game.hide_letter('r')
                    self.add_pos_list(math.trunc(self.r4_x), math.trunc(self.r4_y), 'r')

            elif not self.r1 and not self.r2 and not self.r3 and not self.r4 and self.r5:
                if not self.noheap():
                    self.r5_x, self.r5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('r5')
                    self.r5 = False
                    self.game.count_letters[17] -= 1
                    self.game.hide_letter('r')
                    self.add_pos_list(math.trunc(self.r5_x), math.trunc(self.r5_y), 'r')

            elif not self.r1 and not self.r2 and not self.r3 and not self.r4 and not self.r5 and self.r6:
                if not self.noheap():
                    self.r6_x, self.r6_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('r6')
                    self.r6 = False
                    self.game.count_letters[17] -= 1
                    self.game.hide_letter('r')
                    self.add_pos_list(math.trunc(self.r6_x), math.trunc(self.r6_y), 'r')

        elif self.movement_board and self.game.s_b and self.game.count_letters[18] > 0:
            if self.lay_out_control and self.s1:
                self.lay_out_control, self.s1 = False, False
                self.lay_out_letters.append('s1')
                self.board_cur_x, self.board_cur_y, self.s1_x, self.s1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[18] -= 1
                self.game.hide_letter('s')
                self.add_pos_list(math.trunc(self.s1_x), math.trunc(self.s1_y), 's')

            elif not self.lay_out_control and self.s1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('s1')
                    self.s1_x, self.s1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.s1 = False
                    self.game.count_letters[18] -= 1
                    self.game.hide_letter('s')
                    self.add_pos_list(math.trunc(self.s1_x), math.trunc(self.s1_y), 's')

            elif not self.s1 and self.s2:
                if not self.noheap():
                    self.s2_x, self.s2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('s2')
                    self.s2 = False
                    self.game.count_letters[18] -= 1
                    self.game.hide_letter('s')
                    self.add_pos_list(math.trunc(self.s2_x), math.trunc(self.s2_y), 's')

            elif not self.s1 and not self.s2 and self.s3:
                if not self.noheap():
                    self.s3_x, self.s3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('s3')
                    self.s3 = False
                    self.game.count_letters[18] -= 1
                    self.game.hide_letter('s')
                    self.add_pos_list(math.trunc(self.s3_x), math.trunc(self.s3_y), 's')

            elif not self.s1 and not self.s2 and not self.s3 and self.s4:
                if not self.noheap():
                    self.s4_x, self.s4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('s4')
                    self.s4 = False
                    self.game.count_letters[18] -= 1
                    self.game.hide_letter('s')
                    self.add_pos_list(math.trunc(self.s4_x), math.trunc(self.s4_y), 's')

            elif not self.s1 and not self.s2 and not self.s3 and not self.s4 and self.s5:
                if not self.noheap():
                    self.s5_x, self.s5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('s5')
                    self.s5 = False
                    self.game.count_letters[18] -= 1
                    self.game.hide_letter('s')
                    self.add_pos_list(math.trunc(self.s5_x), math.trunc(self.s5_y), 's')

        elif self.movement_board and self.game.t_b and self.game.count_letters[19] > 0:
            if self.lay_out_control and self.t1:
                self.lay_out_control, self.t1 = False, False
                self.lay_out_letters.append('t1')
                self.board_cur_x, self.board_cur_y, self.t1_x, self.t1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[19] -= 1
                self.game.hide_letter('t')
                self.add_pos_list(math.trunc(self.t1_x), math.trunc(self.t1_y), 't')

            elif not self.lay_out_control and self.t1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('t1')
                    self.t1_x, self.t1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.t1 = False
                    self.game.count_letters[19] -= 1
                    self.game.hide_letter('t')
                    self.add_pos_list(math.trunc(self.t1_x), math.trunc(self.t1_y), 't')

            elif not self.t1 and self.t2:
                if not self.noheap():
                    self.t2_x, self.t2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('t2')
                    self.t2 = False
                    self.game.count_letters[19] -= 1
                    self.game.hide_letter('t')
                    self.add_pos_list(math.trunc(self.t2_x), math.trunc(self.t2_y), 't')

            elif not self.t1 and not self.t2 and self.t3:
                if not self.noheap():
                    self.t3_x, self.t3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('t3')
                    self.t3 = False
                    self.game.count_letters[19] -= 1
                    self.game.hide_letter('t')
                    self.add_pos_list(math.trunc(self.t3_x), math.trunc(self.t3_y), 't')

            elif not self.t1 and not self.t2 and not self.t3 and self.t4:
                if not self.noheap():
                    self.t4_x, self.t4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('t4')
                    self.t4 = False
                    self.game.count_letters[19] -= 1
                    self.game.hide_letter('t')
                    self.add_pos_list(math.trunc(self.t4_x), math.trunc(self.t4_y), 't')

            elif not self.t1 and not self.t2 and not self.t3 and not self.t4 and self.t5:
                if not self.noheap():
                    self.t5_x, self.t5_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('t5')
                    self.t5 = False
                    self.game.count_letters[19] -= 1
                    self.game.hide_letter('t')
                    self.add_pos_list(math.trunc(self.t5_x), math.trunc(self.t5_y), 't')

            elif not self.t1 and not self.t2 and not self.t3 and not self.t4 and not self.t5 and self.t6:
                if not self.noheap():
                    self.t6_x, self.t6_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('t6')
                    self.t6 = False
                    self.game.count_letters[19] -= 1
                    self.game.hide_letter('t')
                    self.add_pos_list(math.trunc(self.t6_x), math.trunc(self.t6_y), 't')

            elif not self.t1 and not self.t2 and not self.t3 and not self.t4 and not self.t5 and not self.t6 and self.t7:
                if not self.noheap():
                    self.t7_x, self.t7_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('t7')
                    self.t7 = False
                    self.game.count_letters[19] -= 1
                    self.game.hide_letter('t')
                    self.add_pos_list(math.trunc(self.t7_x), math.trunc(self.t7_y), 't')

        elif self.movement_board and self.game.u_b and self.game.count_letters[20] > 0:
            if self.lay_out_control and self.u1:
                self.lay_out_control, self.u1 = False, False
                self.lay_out_letters.append('u1')
                self.board_cur_x, self.board_cur_y, self.u1_x, self.u1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[20] -= 1
                self.game.hide_letter('u')
                self.add_pos_list(math.trunc(self.u1_x), math.trunc(self.u1_y), 'u')

            elif not self.lay_out_control and self.u1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('u1')
                    self.u1_x, self.u1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.u1 = False
                    self.game.count_letters[20] -= 1
                    self.game.hide_letter('u')
                    self.add_pos_list(math.trunc(self.u1_x), math.trunc(self.u1_y), 'u')

            elif not self.u1 and self.u2:
                if not self.noheap():
                    self.u2_x, self.u2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('u2')
                    self.u2 = False
                    self.game.count_letters[20] -= 1
                    self.game.hide_letter('u')
                    self.add_pos_list(math.trunc(self.u2_x), math.trunc(self.u2_y), 'u')

            elif not self.u1 and not self.u2 and self.u3:
                if not self.noheap():
                    self.u3_x, self.u3_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('u3')
                    self.u3 = False
                    self.game.count_letters[20] -= 1
                    self.game.hide_letter('u')
                    self.add_pos_list(math.trunc(self.u3_x), math.trunc(self.u3_y), 'u')

            elif not self.u1 and not self.u2 and not self.u3 and self.u4:
                if not self.noheap():
                    self.u4_x, self.u4_y = (self.board_cur_x + 65), (self.board_cur_y + 59)
                    self.lay_out_letters.append('u4')
                    self.u4 = False
                    self.game.count_letters[20] -= 1
                    self.game.hide_letter('u')
                    self.add_pos_list(math.trunc(self.u4_x), math.trunc(self.u4_y), 'u')

        elif self.movement_board and self.game.v_b and self.game.count_letters[21] > 0:
            if self.lay_out_control and self.v1:
                self.lay_out_control, self.v1 = False, False
                self.lay_out_letters.append('v1')
                self.board_cur_x, self.board_cur_y, self.v1_x, self.v1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[21] -= 1
                self.game.hide_letter('v')
                self.add_pos_list(math.trunc(self.v1_x), math.trunc(self.v1_y), 'v')

            elif not self.lay_out_control and self.v1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('v1')
                    self.v1_x, self.v1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.v1 = False
                    self.game.count_letters[21] -= 1
                    self.game.hide_letter('v')
                    self.add_pos_list(math.trunc(self.v1_x), math.trunc(self.v1_y), 'v')

            elif not self.v1 and self.v2:
                if not self.noheap():
                    self.v2_x, self.v2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('v2')
                    self.v2 = False
                    self.game.count_letters[21] -= 1
                    self.game.hide_letter('v')
                    self.add_pos_list(math.trunc(self.v2_x), math.trunc(self.v2_y), 'v')

        elif self.movement_board and self.game.w_b and self.game.count_letters[22] > 0:
            if self.lay_out_control and self.w1:
                self.lay_out_control, self.w1 = False, False
                self.lay_out_letters.append('w1')
                self.board_cur_x, self.board_cur_y, self.w1_x, self.w1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[22] -= 1
                self.game.hide_letter('w')
                self.add_pos_list(math.trunc(self.w1_x), math.trunc(self.w1_y), 'w')

            elif not self.lay_out_control and self.w1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('w1')
                    self.w1_x, self.w1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.w1 = False
                    self.game.count_letters[22] -= 1
                    self.game.hide_letter('w')
                    self.add_pos_list(math.trunc(self.w1_x), math.trunc(self.w1_y), 'w')

            elif not self.w1 and self.w2:
                if not self.noheap():
                    self.w2_x, self.w2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('w2')
                    self.w2 = False
                    self.game.count_letters[22] -= 1
                    self.game.hide_letter('w')
                    self.add_pos_list(math.trunc(self.w2_x), math.trunc(self.w2_y), 'w')

        elif self.movement_board and self.game.x_b and self.game.count_letters[23] > 0:
            if self.lay_out_control and self.x1:
                self.lay_out_control, self.x1 = False, False
                self.lay_out_letters.append('x1')
                self.board_cur_x, self.board_cur_y, self.x1_x, self.x1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[23] -= 1
                self.game.hide_letter('x')
                self.add_pos_list(math.trunc(self.x1_x), math.trunc(self.x1_y), 'x')

            elif not self.lay_out_control and self.x1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('x1')
                    self.x1_x, self.x1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.x1 = False
                    self.game.count_letters[23] -= 1
                    self.game.hide_letter('x')
                    self.add_pos_list(math.trunc(self.x1_x), math.trunc(self.x1_y), 'x')

        elif self.movement_board and self.game.y_b and self.game.count_letters[24] > 0:
            if self.lay_out_control and self.y1:
                self.lay_out_control, self.y1 = False, False
                self.lay_out_letters.append('y1')
                self.board_cur_x, self.board_cur_y, self.y1_x, self.y1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[24] -= 1
                self.game.hide_letter('y')
                self.add_pos_list(math.trunc(self.y1_x), math.trunc(self.y1_y), 'y')

            elif not self.lay_out_control and self.y1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('y1')
                    self.y1_x, self.y1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.y1 = False
                    self.game.count_letters[24] -= 1
                    self.game.hide_letter('y')
                    self.add_pos_list(math.trunc(self.y1_x), math.trunc(self.y1_y), 'y')

            elif not self.y1 and self.y2:
                if not self.noheap():
                    self.y2_x, self.y2_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.lay_out_letters.append('y2')
                    self.y2 = False
                    self.game.count_letters[24] -= 1
                    self.game.hide_letter('y')
                    self.add_pos_list(math.trunc(self.y2_x), math.trunc(self.y2_y), 'y')

        elif self.movement_board and self.game.z_b and self.game.count_letters[25] > 0:
            if self.lay_out_control and self.z1:
                self.lay_out_control, self.z1 = False, False
                self.lay_out_letters.append('z1')
                self.board_cur_x, self.board_cur_y, self.z1_x, self.z1_y = (
                385 - 10, 385 - 3.2, self.pos_x + 385, self.pos_y + 385)
                self.game.count_letters[25] -= 1
                self.game.hide_letter('z')
                self.add_pos_list(math.trunc(self.z1_x), math.trunc(self.z1_y), 'z')

            elif not self.lay_out_control and self.z1 and len(self.lay_out_letters) >= 1:
                if not self.noheap():
                    self.lay_out_letters.append('z1')
                    self.z1_x, self.z1_y = (self.board_cur_x + 65, self.board_cur_y + 59)
                    self.z1 = False
                    self.game.count_letters[25] -= 1
                    self.game.hide_letter('z')
                    self.add_pos_list(math.trunc(self.z1_x), math.trunc(self.z1_y), 'z')

        elif len(self.lay_out_letters) > 0:
            if self.movement_board and self.game.backspace_b:
                if self.lay_out_letters[-1] == 'a1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.a1 = True, True
                    self.game.count_letters[0] += 1
                    self.board_cur_x, self.board_cur_y, self.a1_x, self.a1_y = (
                    self.a1_x - 65, self.a1_y - 59, -200, -200)
                    self.lay_out_letters.remove('a1')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a1' and len(self.lay_out_letters) > 1:
                    self.a1 = True
                    self.board_cur_x, self.board_cur_y, self.a1_x, self.a1_y = (
                    self.a1_x - 65, self.a1_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a1')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a2':
                    self.a2 = True
                    self.board_cur_x, self.board_cur_y, self.a2_x, self.a2_y = (
                    self.a2_x - 65, self.a2_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a2')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a3':
                    self.a3 = True
                    self.board_cur_x, self.board_cur_y, self.a3_x, self.a3_y = (
                    self.a3_x - 65, self.a3_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a3')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a4':
                    self.a4 = True
                    self.board_cur_x, self.board_cur_y, self.a4_x, self.a4_y = (
                    self.a4_x - 65, self.a4_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a4')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a5':
                    self.a5 = True
                    self.board_cur_x, self.board_cur_y, self.a5_x, self.a5_y = (
                    self.a5_x - 65, self.a5_y - 59, -200, -200)
                    self.a5_x, self.a5_y = -200, -200
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a5')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a6':
                    self.a6 = True
                    self.board_cur_x, self.board_cur_y, self.a6_x, self.a6_y = (
                    self.a6_x - 65, self.a6_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a6')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a7':
                    self.a7 = True
                    self.board_cur_x, self.board_cur_y, self.a7_x, self.a7_y = (
                    self.a7_x - 65, self.a7_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a7')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a8':
                    self.a8 = True
                    self.board_cur_x, self.board_cur_y, self.a8_x, self.a8_y = (
                    self.a8_x - 65, self.a8_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a8')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'a9':
                    self.a9 = True
                    self.board_cur_x, self.board_cur_y, self.a9_x, self.a9_y = (
                    self.a9_x - 65, self.a9_y - 59, -200, -200)
                    self.game.count_letters[0] += 1
                    self.lay_out_letters.remove('a9')
                    self.game.return_letter('a')

                elif self.lay_out_letters[-1] == 'b1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.b1 = True, True
                    self.board_cur_x, self.board_cur_y, self.b1_x, self.b1_y = (
                    self.b1_x - 65, self.b1_y - 59, -200, -200)
                    self.game.count_letters[1] += 1
                    self.lay_out_letters.remove('b1')
                    self.game.return_letter('b')

                elif self.lay_out_letters[-1] == 'b1' and len(self.lay_out_letters) > 1:
                    self.b1 = True
                    self.board_cur_x, self.board_cur_y, self.b1_x, self.b1_y = (
                    self.b1_x - 65, self.b1_y - 59, -200, -200)
                    self.game.count_letters[1] += 1
                    self.lay_out_letters.remove('b1')
                    self.game.return_letter('b')

                elif self.lay_out_letters[-1] == 'b2':
                    self.b2 = True
                    self.board_cur_x, self.board_cur_y, self.b2_x, self.b2_y = (
                    self.b2_x - 65, self.b2_y - 59, -200, -200)
                    self.game.count_letters[1] += 1
                    self.lay_out_letters.remove('b2')
                    self.game.return_letter('b')

                elif self.lay_out_letters[-1] == 'c1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.c1 = True, True
                    self.game.count_letters[2] += 1
                    self.board_cur_x, self.board_cur_y, self.c1_x, self.c1_y = (
                    self.c1_x - 65, self.c1_y - 59, -200, -200)
                    self.lay_out_letters.remove('c1')
                    self.game.return_letter('c')

                elif self.lay_out_letters[-1] == 'c1' and len(self.lay_out_letters) > 1:
                    self.c1 = True
                    self.board_cur_x, self.board_cur_y, self.c1_x, self.c1_y = (
                    self.c1_x - 65, self.c1_y - 59, -200, -200)
                    self.game.count_letters[2] += 1
                    self.lay_out_letters.remove('c1')
                    self.game.return_letter('c')

                elif self.lay_out_letters[-1] == 'c2':
                    self.c2 = True
                    self.board_cur_x, self.board_cur_y, self.c2_x, self.c2_y = (
                    self.c2_x - 65, self.c2_y - 59, -200, -200)
                    self.game.count_letters[2] += 1
                    self.lay_out_letters.remove('c2')
                    self.game.return_letter('c')

                elif self.lay_out_letters[-1] == 'd1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.d1 = True, True
                    self.game.count_letters[3] += 1
                    self.board_cur_x, self.board_cur_y, self.d1_x, self.d1_y = (
                    self.d1_x - 65, self.d1_y - 59, -200, -200)
                    self.lay_out_letters.remove('d1')
                    self.game.return_letter('d')

                elif self.lay_out_letters[-1] == 'd1' and len(self.lay_out_letters) > 1:
                    self.d1 = True
                    self.board_cur_x, self.board_cur_y, self.d1_x, self.d1_y = (
                    self.d1_x - 65, self.d1_y - 59, -200, -200)
                    self.game.count_letters[3] += 1
                    self.lay_out_letters.remove('d1')
                    self.game.return_letter('d')

                elif self.lay_out_letters[-1] == 'd2':
                    self.d2 = True
                    self.board_cur_x, self.board_cur_y, self.d2_x, self.d2_y = (
                    self.d2_x - 65, self.d2_y - 59, -200, -200)
                    self.game.count_letters[3] += 1
                    self.lay_out_letters.remove('d2')
                    self.game.return_letter('d')

                elif self.lay_out_letters[-1] == 'd3':
                    self.d3 = True
                    self.board_cur_x, self.board_cur_y, self.d3_x, self.d3_y = (
                    self.d3_x - 65, self.d3_y - 59, -200, -200)
                    self.game.count_letters[3] += 1
                    self.lay_out_letters.remove('d3')
                    self.game.return_letter('d')

                elif self.lay_out_letters[-1] == 'd4':
                    self.d4 = True
                    self.board_cur_x, self.board_cur_y, self.d4_x, self.d4_y = (
                    self.d4_x - 65, self.d4_y - 59, -200, -200)
                    self.game.count_letters[3] += 1
                    self.lay_out_letters.remove('d4')
                    self.game.return_letter('d')

                elif self.lay_out_letters[-1] == 'd5':
                    self.d5 = True
                    self.board_cur_x, self.board_cur_y, self.d5_x, self.d5_y = (
                    self.d5_x - 65, self.d5_y - 59, -200, -200)
                    self.game.count_letters[3] += 1
                    self.lay_out_letters.remove('d5')
                    self.game.return_letter('d')

                elif self.lay_out_letters[-1] == 'e1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.e1 = True, True
                    self.game.count_letters[4] += 1
                    self.board_cur_x, self.board_cur_y, self.e1_x, self.e1_y = (
                    self.e1_x - 65, self.e1_y - 59, -200, -200)
                    self.lay_out_letters.remove('e1')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e1' and len(self.lay_out_letters) > 1:
                    self.e1 = True
                    self.board_cur_x, self.board_cur_y, self.e1_x, self.e1_y = (
                    self.e1_x - 65, self.e1_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e1')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e2':
                    self.e2 = True
                    self.board_cur_x, self.board_cur_y, self.e2_x, self.e2_y = (
                    self.e2_x - 65, self.e2_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e2')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e3':
                    self.e3 = True
                    self.board_cur_x, self.board_cur_y, self.e3_x, self.e3_y = (
                    self.e3_x - 65, self.e3_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e3')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e4':
                    self.e4 = True
                    self.board_cur_x, self.board_cur_y, self.e4_x, self.e4_y = (
                    self.e4_x - 65, self.e4_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e4')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e5':
                    self.e5 = True
                    self.board_cur_x, self.board_cur_y, self.e5_x, self.e5_y = (
                    self.e5_x - 65, self.e5_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e5')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e6':
                    self.e6 = True
                    self.board_cur_x, self.board_cur_y, self.e6_x, self.e6_y = (
                    self.e6_x - 65, self.e6_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e6')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e7':
                    self.e7 = True
                    self.board_cur_x, self.board_cur_y, self.e7_x, self.e7_y = (
                    self.e7_x - 65, self.e7_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e7')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e8':
                    self.e8 = True
                    self.board_cur_x, self.board_cur_y, self.e8_x, self.e8_y = (
                    self.e8_x - 65, self.e8_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e8')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e9':
                    self.e9 = True
                    self.board_cur_x, self.board_cur_y, self.e9_x, self.e9_y = (
                    self.e9_x - 65, self.e9_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e9')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e10':
                    self.e10 = True
                    self.board_cur_x, self.board_cur_y, self.e10_x, self.e10_y = (
                    self.e10_x - 65, self.e10_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e10')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e11':
                    self.e11 = True
                    self.board_cur_x, self.board_cur_y, self.e11_x, self.e11_y = (
                    self.e11_x - 65, self.e11_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e11')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e12':
                    self.e12 = True
                    self.board_cur_x, self.board_cur_y, self.e12_x, self.e12_y = (
                    self.e12_x - 65, self.e12_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e12')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'e13':
                    self.e13 = True
                    self.board_cur_x, self.board_cur_y, self.e13_x, self.e13_y = (
                    self.e13_x - 65, self.e13_y - 59, -200, -200)
                    self.game.count_letters[4] += 1
                    self.lay_out_letters.remove('e13')
                    self.game.return_letter('e')

                elif self.lay_out_letters[-1] == 'f1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.f1 = True, True
                    self.board_cur_x, self.board_cur_y, self.f1_x, self.f1_y = (
                    self.f1_x - 65, self.f1_y - 59, -200, -200)
                    self.game.count_letters[5] += 1
                    self.lay_out_letters.remove('f1')
                    self.game.return_letter('f')

                elif self.lay_out_letters[-1] == 'f1' and len(self.lay_out_letters) > 1:
                    self.f1 = True
                    self.board_cur_x, self.board_cur_y, self.f1_x, self.f1_y = (
                    self.f1_x - 65, self.f1_y - 59, -200, -200)
                    self.game.count_letters[5] += 1
                    self.lay_out_letters.remove('f1')
                    self.game.return_letter('f')

                elif self.lay_out_letters[-1] == 'f2':
                    self.f2 = True
                    self.board_cur_x, self.board_cur_y, self.f2_x, self.f2_y = (
                    self.f2_x - 65, self.f2_y - 59, -200, -200)
                    self.game.count_letters[5] += 1
                    self.lay_out_letters.remove('f2')
                    self.game.return_letter('f')

                elif self.lay_out_letters[-1] == 'g1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.g1 = True, True
                    self.board_cur_x, self.board_cur_y, self.g1_x, self.g1_y = (
                    self.g1_x - 65, self.g1_y - 59, -200, -200)
                    self.game.count_letters[6] += 1
                    self.lay_out_letters.remove('g1')
                    self.game.return_letter('g')

                elif self.lay_out_letters[-1] == 'g1' and len(self.lay_out_letters) > 1:
                    self.g1 = True
                    self.board_cur_x, self.board_cur_y, self.g1_x, self.g1_y = (
                    self.g1_x - 65, self.g1_y - 59, -200, -200)
                    self.game.count_letters[6] += 1
                    self.lay_out_letters.remove('g1')
                    self.game.return_letter('g')

                elif self.lay_out_letters[-1] == 'g2':
                    self.g2 = True
                    self.board_cur_x, self.board_cur_y, self.g2_x, self.g2_y = (
                    self.g2_x - 65, self.g2_y - 59, -200, -200)
                    self.game.count_letters[6] += 1
                    self.lay_out_letters.remove('g2')
                    self.game.return_letter('g')

                elif self.lay_out_letters[-1] == 'g3':
                    self.g3 = True
                    self.board_cur_x, self.board_cur_y, self.g3_x, self.g3_y = (
                    self.g3_x - 65, self.g3_y - 59, -200, -200)
                    self.game.count_letters[6] += 1
                    self.lay_out_letters.remove('g3')
                    self.game.return_letter('g')

                elif self.lay_out_letters[-1] == 'h1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.h1 = True, True
                    self.game.count_letters[7] += 1
                    self.board_cur_x, self.board_cur_y, self.h1_x, self.h1_y = (
                    self.h1_x - 65, self.h1_y - 59, -200, -200)
                    self.lay_out_letters.remove('h1')
                    self.game.return_letter('h')

                elif self.lay_out_letters[-1] == 'h1' and len(self.lay_out_letters) > 1:
                    self.h1 = True
                    self.board_cur_x, self.board_cur_y, self.h1_x, self.h1_y = (
                    self.h1_x - 65, self.h1_y - 59, -200, -200)
                    self.game.count_letters[7] += 1
                    self.lay_out_letters.remove('h1')
                    self.game.return_letter('h')

                elif self.lay_out_letters[-1] == 'h2':
                    self.h2 = True
                    self.board_cur_x, self.board_cur_y, self.h2_x, self.h2_y = (
                    self.h2_x - 65, self.h2_y - 59, -200, -200)
                    self.game.count_letters[7] += 1
                    self.lay_out_letters.remove('h2')
                    self.game.return_letter('h')

                elif self.lay_out_letters[-1] == 'h3':
                    self.h3 = True
                    self.board_cur_x, self.board_cur_y, self.h3_x, self.h3_y = (
                    self.h3_x - 65, self.h3_y - 59, -200, -200)
                    self.game.count_letters[7] += 1
                    self.lay_out_letters.remove('h3')
                    self.game.return_letter('h')

                elif self.lay_out_letters[-1] == 'h4':
                    self.h4 = True
                    self.board_cur_x, self.board_cur_y, self.h4_x, self.h4_y = (
                    self.h4_x - 65, self.h4_y - 59, -200, -200)
                    self.game.count_letters[7] += 1
                    self.lay_out_letters.remove('h4')
                    self.game.return_letter('h')

                elif self.lay_out_letters[-1] == 'i1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.i1 = True, True
                    self.game.count_letters[8] += 1
                    self.board_cur_x, self.board_cur_y, self.i1_x, self.i1_y = (
                    self.i1_x - 65, self.i1_y - 59, -200, -200)
                    self.lay_out_letters.remove('i1')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i1' and len(self.lay_out_letters) > 1:
                    self.i1 = True
                    self.board_cur_x, self.board_cur_y, self.i1_x, self.i1_y = (
                    self.i1_x - 65, self.i1_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i1')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i2':
                    self.i2 = True
                    self.board_cur_x, self.board_cur_y, self.i2_x, self.i2_y = (
                    self.i2_x - 65, self.i2_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i2')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i3':
                    self.i3 = True
                    self.board_cur_x, self.board_cur_y, self.i3_x, self.i3_y = (
                    self.i3_x - 65, self.i3_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i3')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i4':
                    self.i4 = True
                    self.board_cur_x, self.board_cur_y, self.i4_x, self.i4_y = (
                    self.i4_x - 65, self.i4_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i4')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i5':
                    self.i5 = True
                    self.board_cur_x, self.board_cur_y, self.i5_x, self.i5_y = (
                    self.i5_x - 65, self.i5_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i5')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i6':
                    self.i6 = True
                    self.board_cur_x, self.board_cur_y, self.i6_x, self.i6_y = (
                    self.i6_x - 65, self.i6_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i6')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i7':
                    self.i7 = True
                    self.board_cur_x, self.board_cur_y, self.i7_x, self.i7_y = (
                    self.i7_x - 65, self.i7_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i7')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'i8':
                    self.board_cur_x, self.board_cur_y, self.i8_x, self.i8_y = (
                    self.i8_x - 65, self.i8_y - 59, -200, -200)
                    self.game.count_letters[8] += 1
                    self.lay_out_letters.remove('i8')
                    self.game.return_letter('i')

                elif self.lay_out_letters[-1] == 'j1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.j1 = True, True
                    self.game.count_letters[9] += 1
                    self.board_cur_x, self.board_cur_y, self.j1_x, self.j1_y = self.j1_x - 65, self.j1_y - 59, -200, -200
                    self.lay_out_letters.remove('j1')
                    self.game.return_letter('j')

                elif self.lay_out_letters[-1] == 'j1' and len(self.lay_out_letters) > 1:
                    self.j1 = True
                    self.board_cur_x, self.board_cur_y, self.j1_x, self.j1_y = (
                    self.j1_x - 65, self.j1_y - 59, -200, -200)
                    self.game.count_letters[9] += 1
                    self.lay_out_letters.remove('j1')
                    self.game.return_letter('j')

                elif self.lay_out_letters[-1] == 'k1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.k1 = True, True
                    self.game.count_letters[10] += 1
                    self.board_cur_x, self.board_cur_y, self.k1_x, self.k1_y = (
                    self.k1_x - 65, self.k1_y - 59, -200, -200)
                    self.lay_out_letters.remove('k1')
                    self.game.return_letter('k')

                elif self.lay_out_letters[-1] == 'k1' and len(self.lay_out_letters) > 1:
                    self.k1 = True
                    self.board_cur_x, self.board_cur_y, self.k1_x, self.k1_y = (
                    self.k1_x - 65, self.k1_y - 59, -200, -200)
                    self.game.count_letters[10] += 1
                    self.lay_out_letters.remove('k1')
                    self.game.return_letter('k')

                elif self.lay_out_letters[-1] == 'l1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.l1 = True, True
                    self.game.count_letters[11] += 1
                    self.board_cur_x, self.board_cur_y, self.l1_x, self.l1_y = (
                    self.l1_x - 65, self.l1_y - 59, -200, -200)
                    self.lay_out_letters.remove('l1')
                    self.game.return_letter('l')

                elif self.lay_out_letters[-1] == 'l1' and len(self.lay_out_letters) > 1:
                    self.l1 = True
                    self.board_cur_x, self.board_cur_y, self.l1_x, self.l1_y = (
                    self.l1_x - 65, self.l1_y - 59, -200, -200)
                    self.game.count_letters[11] += 1
                    self.lay_out_letters.remove('l1')
                    self.game.return_letter('l')

                elif self.lay_out_letters[-1] == 'l2':
                    self.l2 = True
                    self.board_cur_x, self.board_cur_y, self.l2_x, self.l2_y = (
                    self.l2_x - 65, self.l2_y - 59, -200, -200)
                    self.game.count_letters[11] += 1
                    self.lay_out_letters.remove('l2')
                    self.game.return_letter('l')

                elif self.lay_out_letters[-1] == 'l3':
                    self.l3 = True
                    self.board_cur_x, self.board_cur_y, self.l3_x, self.l3_y = (
                    self.l3_x - 65, self.l3_y - 59, -200, -200)
                    self.game.count_letters[11] += 1
                    self.lay_out_letters.remove('l3')
                    self.game.return_letter('l')

                elif self.lay_out_letters[-1] == 'l4':
                    self.l4 = True
                    self.board_cur_x, self.board_cur_y, self.l4_x, self.l4_y = (
                    self.l4_x - 65, self.l4_y - 59, -200, -200)
                    self.game.count_letters[11] += 1
                    self.lay_out_letters.remove('l4')
                    self.game.return_letter('l')

                elif self.lay_out_letters[-1] == 'm1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.m1 = True, True
                    self.game.count_letters[12] += 1
                    self.board_cur_x, self.board_cur_y, self.m1_x, self.m1_y = (
                    self.m1_x - 65, self.m1_y - 59, -200, -200)
                    self.lay_out_letters.remove('m1')
                    self.game.return_letter('m')

                elif self.lay_out_letters[-1] == 'm1' and len(self.lay_out_letters) > 1:
                    self.m1 = True
                    self.board_cur_x, self.board_cur_y, self.m1_x, self.m1_y = (
                    self.m1_x - 65, self.m1_y - 59, -200, -200)
                    self.game.count_letters[12] += 1
                    self.lay_out_letters.remove('m1')
                    self.game.return_letter('m')

                elif self.lay_out_letters[-1] == 'm2':
                    self.m2 = True
                    self.board_cur_x, self.board_cur_y, self.m2_x, self.m2_y = (
                    self.m2_x - 65, self.m2_y - 59, -200, -200)
                    self.game.count_letters[12] += 1
                    self.lay_out_letters.remove('m2')
                    self.game.return_letter('m')

                elif self.lay_out_letters[-1] == 'n1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.n1 = True, True
                    self.game.count_letters[13] += 1
                    self.board_cur_x, self.board_cur_y, self.n1_x, self.n1_y = (
                    self.n1_x - 65, self.n1_y - 59, -200, -200)
                    self.lay_out_letters.remove('n1')
                    self.game.return_letter('n')

                elif self.lay_out_letters[-1] == 'n1' and len(self.lay_out_letters) > 1:
                    self.n1 = True
                    self.board_cur_x, self.board_cur_y, self.n1_x, self.n1_y = (
                    self.n1_x - 65, self.n1_y - 59, -200, -200)
                    self.game.count_letters[13] += 1
                    self.lay_out_letters.remove('n1')
                    self.game.return_letter('n')

                elif self.lay_out_letters[-1] == 'n2':
                    self.n2 = True
                    self.board_cur_x, self.board_cur_y, self.n2_x, self.n2_y = (
                    self.n2_x - 65, self.n2_y - 59, -200, -200)
                    self.game.count_letters[13] += 1
                    self.lay_out_letters.remove('n2')
                    self.game.return_letter('n')

                elif self.lay_out_letters[-1] == 'n3':
                    self.n3 = True
                    self.board_cur_x, self.board_cur_y, self.n3_x, self.n3_y = (
                    self.n3_x - 65, self.n3_y - 59, -200, -200)
                    self.game.count_letters[13] += 1
                    self.lay_out_letters.remove('n3')
                    self.game.return_letter('n')

                elif self.lay_out_letters[-1] == 'n4':
                    self.n4 = True
                    self.board_cur_x, self.board_cur_y, self.n4_x, self.n4_y = (
                    self.n4_x - 65, self.n4_y - 59, -200, -200)
                    self.game.count_letters[13] += 1
                    self.lay_out_letters.remove('n4')
                    self.game.return_letter('n')

                elif self.lay_out_letters[-1] == 'n5':
                    self.n5 = True
                    self.board_cur_x, self.board_cur_y, self.n5_x, self.n5_y = (
                    self.n5_x - 65, self.n5_y - 59, -200, -200)
                    self.game.count_letters[13] += 1
                    self.lay_out_letters.remove('n5')
                    self.game.return_letter('n')

                elif self.lay_out_letters[-1] == 'o1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.o1 = True, True
                    self.game.count_letters[14] += 1
                    self.board_cur_x, self.board_cur_y, self.o1_x, self.o1_y = (
                    self.o1_x - 65, self.o1_y - 59, -200, -200)
                    self.lay_out_letters.remove('o1')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o1' and len(self.lay_out_letters) > 1:
                    self.o1 = True
                    self.board_cur_x, self.board_cur_y, self.o1_x, self.o1_y = (
                    self.o1_x - 65, self.o1_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o1')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o2':
                    self.o2 = True
                    self.board_cur_x, self.board_cur_y, self.o2_x, self.o2_y = (
                    self.o2_x - 65, self.o2_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o2')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o3':
                    self.o3 = True
                    self.board_cur_x, self.board_cur_y, self.o3_x, self.o3_y = (
                    self.o3_x - 65, self.o3_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o3')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o4':
                    self.o4 = True
                    self.board_cur_x, self.board_cur_y, self.o4_x, self.o4_y = (
                    self.o4_x - 65, self.o4_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o4')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o5':
                    self.o5 = True
                    self.board_cur_x, self.board_cur_y, self.o5_x, self.o5_y = (
                    self.o5_x - 65, self.o5_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o5')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o6':
                    self.o6 = True
                    self.board_cur_x, self.board_cur_y, self.o6_x, self.o6_y = (
                    self.o6_x - 65, self.o6_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o6')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o7':
                    self.o7 = True
                    self.board_cur_x, self.board_cur_y, self.o7_x, self.o7_y = (
                    self.o7_x - 65, self.o7_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o7')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'o8':
                    self.o8 = True
                    self.board_cur_x, self.board_cur_y, self.o8_x, self.o8_y = (
                    self.o8_x - 65, self.o8_y - 59, -200, -200)
                    self.game.count_letters[14] += 1
                    self.lay_out_letters.remove('o8')
                    self.game.return_letter('o')

                elif self.lay_out_letters[-1] == 'p1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.p1 = True, True
                    self.game.count_letters[15] += 1
                    self.board_cur_x, self.board_cur_y, self.p1_x, self.p1_y = (
                    self.p1_x - 65, self.p1_y - 59, -200, -200)
                    self.lay_out_letters.remove('p1')
                    self.game.return_letter('p')

                elif self.lay_out_letters[-1] == 'p1' and len(self.lay_out_letters) > 1:
                    self.p1 = True
                    self.board_cur_x, self.board_cur_y, self.p1_x, self.p1_y = (
                    self.p1_x - 65, self.p1_y - 59, -200, -200)
                    self.p1_x, self.p1_y = -200, -200
                    self.game.count_letters[15] += 1
                    self.lay_out_letters.remove('p1')
                    self.game.return_letter('p')

                elif self.lay_out_letters[-1] == 'p2':
                    self.p2 = True
                    self.board_cur_x, self.board_cur_y, self.p2_x, self.p2_y = (
                    self.p2_x - 65, self.p2_y - 59, -200, -200)
                    self.game.count_letters[15] += 1
                    self.lay_out_letters.remove('p2')
                    self.game.return_letter('p')

                elif self.lay_out_letters[-1] == 'q1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.q1 = True, True
                    self.game.count_letters[16] += 1
                    self.board_cur_x, self.board_cur_y, self.q1_x, self.q1_y = (
                    self.q1_x - 65, self.q1_y - 59, -200, -200)
                    self.lay_out_letters.remove('q1')
                    self.game.return_letter('q')

                elif self.lay_out_letters[-1] == 'q1' and len(self.lay_out_letters) > 1:
                    self.q1 = True
                    self.board_cur_x, self.board_cur_y, self.q1_x, self.q1_y = (
                    self.q1_x - 65, self.q1_y - 59, -200, -200)
                    self.game.count_letters[16] += 1
                    self.lay_out_letters.remove('q1')
                    self.game.return_letter('q')

                elif self.lay_out_letters[-1] == 'r1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.r1 = True, True
                    self.game.count_letters[17] += 1
                    self.board_cur_x, self.board_cur_y, self.r1_x, self.r1_y = (
                    self.r1_x - 65, self.r1_y - 59, -200, -200)
                    self.lay_out_letters.remove('r1')
                    self.game.return_letter('r')

                elif self.lay_out_letters[-1] == 'r1' and len(self.lay_out_letters) > 1:
                    self.r1 = True
                    self.board_cur_x, self.board_cur_y, self.r1_x, self.r1_y = (
                    self.r1_x - 65, self.r1_y - 59, -200, -200)
                    self.game.count_letters[17] += 1
                    self.lay_out_letters.remove('r1')
                    self.game.return_letter('r')

                elif self.lay_out_letters[-1] == 'r2':
                    self.r2 = True
                    self.board_cur_x, self.board_cur_y, self.r2_x, self.r2_y = (
                    self.r2_x - 65, self.r2_y - 59, -200, -200)
                    self.game.count_letters[17] += 1
                    self.lay_out_letters.remove('r2')
                    self.game.return_letter('r')

                elif self.lay_out_letters[-1] == 'r3':
                    self.r3 = True
                    self.board_cur_x, self.board_cur_y, self.r3_x, self.r3_y = (
                    self.r3_x - 65, self.r3_y - 59, -200, -200)
                    self.game.count_letters[17] += 1
                    self.lay_out_letters.remove('r3')
                    self.game.return_letter('r')

                elif self.lay_out_letters[-1] == 'r4':
                    self.r4 = True
                    self.board_cur_x, self.board_cur_y, self.r4_x, self.r4_y = (
                    self.r4_x - 65, self.r4_y - 59, -200, -200)
                    self.game.count_letters[17] += 1
                    self.lay_out_letters.remove('r4')
                    self.game.return_letter('r')

                elif self.lay_out_letters[-1] == 'r5':
                    self.r5 = True
                    self.board_cur_x, self.board_cur_y, self.r5_x, self.r5_y = (
                    self.r5_x - 65, self.r5_y - 59, -200, -200)
                    self.game.count_letters[17] += 1
                    self.lay_out_letters.remove('r5')
                    self.game.return_letter('r')

                elif self.lay_out_letters[-1] == 'r6':
                    self.r6 = True
                    self.board_cur_x, self.board_cur_y, self.r6_x, self.r6_y = (
                    self.r6_x - 65, self.r6_y - 59, -200, -200)
                    self.game.count_letters[17] += 1
                    self.lay_out_letters.remove('r6')
                    self.game.return_letter('r')

                elif self.lay_out_letters[-1] == 's1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.s1 = True, True
                    self.game.count_letters[18] += 1
                    self.board_cur_x, self.board_cur_y, self.s1_x, self.s1_y = (
                    self.s1_x - 65, self.s1_y - 59, -200, -200)
                    self.lay_out_letters.remove('s1')
                    self.game.return_letter('s')

                elif self.lay_out_letters[-1] == 's1' and len(self.lay_out_letters) > 1:
                    self.s1 = True
                    self.board_cur_x, self.board_cur_y, self.s1_x, self.s1_y = (
                    self.s1_x - 65, self.s1_y - 59, -200, -200)
                    self.game.count_letters[18] += 1
                    self.lay_out_letters.remove('s1')
                    self.game.return_letter('s')

                elif self.lay_out_letters[-1] == 's2':
                    self.s2 = True
                    self.board_cur_x, self.board_cur_y, self.s2_x, self.s2_y = (
                    self.s2_x - 65, self.s2_y - 59, -200, -200)
                    self.game.count_letters[18] += 1
                    self.lay_out_letters.remove('s2')
                    self.game.return_letter('s')

                elif self.lay_out_letters[-1] == 's3':
                    self.s3 = True
                    self.board_cur_x, self.board_cur_y, self.s3_x, self.s3_y = (
                    self.s3_x - 65, self.s3_y - 59, -200, -200)
                    self.game.count_letters[18] += 1
                    self.lay_out_letters.remove('s3')
                    self.game.return_letter('s')

                elif self.lay_out_letters[-1] == 's4':
                    self.s4 = True
                    self.board_cur_x, self.board_cur_y, self.s4_x, self.s4_y = (
                    self.s4_x - 65, self.s4_y - 59, -200, -200)
                    self.game.count_letters[18] += 1
                    self.lay_out_letters.remove('s4')
                    self.game.return_letter('s')

                elif self.lay_out_letters[-1] == 's5':
                    self.s5 = True
                    self.board_cur_x, self.board_cur_y, self.s5_x, self.s5_y = (
                    self.s5_x - 65, self.s5_y - 59, -200, -200)
                    self.game.count_letters[18] += 1
                    self.lay_out_letters.remove('s5')
                    self.game.return_letter('s')

                elif self.lay_out_letters[-1] == 't1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.t1 = True, True
                    self.game.count_letters[19] += 1
                    self.board_cur_x, self.board_cur_y, self.t1_x, self.t1_y = (
                    self.t1_x - 65, self.t1_y - 59, -200, -200)
                    self.lay_out_letters.remove('t1')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 't1' and len(self.lay_out_letters) > 1:
                    self.t1 = True
                    self.board_cur_x, self.board_cur_y, self.t1_x, self.t1_y = (
                    self.t1_x - 65, self.t1_y - 59, -200, -200)
                    self.game.count_letters[19] += 1
                    self.lay_out_letters.remove('t1')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 't2':
                    self.t2 = True
                    self.board_cur_x, self.board_cur_y, self.t2_x, self.t2_y = (
                    self.t2_x - 65, self.t2_y - 59, -200, -200)
                    self.game.count_letters[19] += 1
                    self.lay_out_letters.remove('t2')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 't3':
                    self.t3 = True
                    self.board_cur_x, self.board_cur_y, self.t3_x, self.t3_y = (
                    self.t3_x - 65, self.t3_y - 59, -200, -200)
                    self.game.count_letters[19] += 1
                    self.lay_out_letters.remove('t3')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 't4':
                    self.t4 = True
                    self.board_cur_x, self.board_cur_y, self.t4_x, self.t4_y = (
                    self.t4_x - 65, self.t4_y - 59, -200, -200)
                    self.game.count_letters[19] += 1
                    self.lay_out_letters.remove('t4')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 't5':
                    self.t5 = True
                    self.board_cur_x, self.board_cur_y, self.t5_x, self.t5_y = (
                    self.t5_x - 65, self.t5_y - 59, -200, -200)
                    self.game.count_letters[19] += 1
                    self.lay_out_letters.remove('t5')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 't6':
                    self.t6 = True
                    self.board_cur_x, self.board_cur_y, self.t6_x, self.t6_y = (
                    self.t6_x - 65, self.t6_y - 59, -200, -200)
                    self.game.count_letters[19] += 1
                    self.lay_out_letters.remove('t6')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 't7':
                    self.t7 = True
                    self.board_cur_x, self.board_cur_y, self.t7_x, self.t7_y = (
                    self.t7_x - 65, self.t7_y - 59, -200, -200)
                    self.game.count_letters[19] += 1
                    self.lay_out_letters.remove('t7')
                    self.game.return_letter('t')

                elif self.lay_out_letters[-1] == 'u1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control = True
                    self.u1 = True
                    self.game.count_letters[20] += 1
                    self.board_cur_x, self.board_cur_y, self.u1_x, self.u1_y = (
                    self.u1_x - 65, self.u1_y - 59, -200, -200)
                    self.lay_out_letters.remove('u1')
                    self.game.return_letter('u')

                elif self.lay_out_letters[-1] == 'u1' and len(self.lay_out_letters) > 1:
                    self.u1 = True
                    self.board_cur_x, self.board_cur_y, self.u1_x, self.u1_y = (
                    self.u1_x - 65, self.u1_y - 59, -200, -200)
                    self.game.count_letters[20] += 1
                    self.lay_out_letters.remove('u1')
                    self.game.return_letter('u')

                elif self.lay_out_letters[-1] == 'u2':
                    self.u2 = True
                    self.board_cur_x, self.board_cur_y, self.u2_x, self.u2_y = (
                    self.u2_x - 65, self.u2_y - 59, -200, -200)
                    self.game.count_letters[20] += 1
                    self.lay_out_letters.remove('u2')
                    self.game.return_letter('u')

                elif self.lay_out_letters[-1] == 'u3':
                    self.u3 = True
                    self.board_cur_x, self.board_cur_y, self.u3_x, self.u3_y = (
                    self.u3_x - 65, self.u3_y - 59, -200, -200)
                    self.game.count_letters[20] += 1
                    self.lay_out_letters.remove('u3')
                    self.game.return_letter('u')

                elif self.lay_out_letters[-1] == 'u4':
                    self.u4 = True
                    self.board_cur_x, self.board_cur_y, self.u4_x, self.u4_y = (
                    self.u4_x - 65, self.u4_y - 59, -200, -200)
                    self.game.count_letters[20] += 1
                    self.lay_out_letters.remove('u4')
                    self.game.return_letter('u')

                elif self.lay_out_letters[-1] == 'v1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control = True
                    self.v1 = True
                    self.game.count_letters[21] += 1
                    self.board_cur_x, self.board_cur_y, self.v1_x, self.v1_y = (
                    self.v1_x - 65, self.v1_y - 59, -200, -200)
                    self.lay_out_letters.remove('v1')
                    self.game.return_letter('v')

                elif self.lay_out_letters[-1] == 'v1' and len(self.lay_out_letters) > 1:
                    self.v1 = True
                    self.board_cur_x, self.board_cur_y, self.v1_x, self.v1_y = (
                    self.v1_x - 65, self.v1_y - 59, -200, -200)
                    self.game.count_letters[21] += 1
                    self.lay_out_letters.remove('v1')
                    self.game.return_letter('v')

                elif self.lay_out_letters[-1] == 'v2':
                    self.v2 = True
                    self.board_cur_x, self.board_cur_y, self.v2_x, self.v2_y = (
                    self.v2_x - 65, self.v2_y - 59, -200, -200)
                    self.game.count_letters[21] += 1
                    self.lay_out_letters.remove('v2')
                    self.game.return_letter('v')

                elif self.lay_out_letters[-1] == 'w1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.w1 = True, True
                    self.game.count_letters[22] += 1
                    self.board_cur_x, self.board_cur_y, self.w1_x, self.w1_y = (
                    self.w1_x - 65, self.w1_y - 59, -200, -200)
                    self.lay_out_letters.remove('w1')
                    self.game.return_letter('w')

                elif self.lay_out_letters[-1] == 'w1' and len(self.lay_out_letters) > 1:
                    self.w1 = True
                    self.board_cur_x, self.board_cur_y, self.w1_x, self.w1_y = (
                    self.w1_x - 65, self.w1_y - 59, -200, -200)
                    self.game.count_letters[22] += 1
                    self.lay_out_letters.remove('w1')
                    self.game.return_letter('w')

                elif self.lay_out_letters[-1] == 'w2':
                    self.w2 = True
                    self.board_cur_x, self.board_cur_y, self.w2_x, self.w2_y = (
                    self.w2_x - 65, self.w2_y - 59, -200, -200)
                    self.game.count_letters[22] += 1
                    self.lay_out_letters.remove('w2')
                    self.game.return_letter('w')

                elif self.lay_out_letters[-1] == 'x1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.x1 = True, True
                    self.game.count_letters[23] += 1
                    self.board_cur_x, self.board_cur_y, self.x1_x, self.x1_y = (
                    self.x1_x - 65, self.x1_y - 59, -200, -200)
                    self.lay_out_letters.remove('x1')
                    self.game.return_letter('x')

                elif self.lay_out_letters[-1] == 'x1' and len(self.lay_out_letters) > 1:
                    self.x1 = True
                    self.board_cur_x, self.board_cur_y, self.x1_x, self.x1_y = (
                    self.x1_x - 65, self.x1_y - 59, -200, -200)
                    self.game.count_letters[23] += 1
                    self.lay_out_letters.remove('x1')
                    self.game.return_letter('x')

                elif self.lay_out_letters[-1] == 'y1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control, self.y1 = True, True
                    self.game.count_letters[24] += 1
                    self.board_cur_x, self.board_cur_y, self.y1_x, self.y1_y = (
                    self.y1_x - 65, self.y1_y - 59, -200, -200)
                    self.lay_out_letters.remove('y1')
                    self.game.return_letter('y')

                elif self.lay_out_letters[-1] == 'y1' and len(self.lay_out_letters) > 1:
                    self.y1 = True
                    self.board_cur_x, self.board_cur_y, self.y1_x, self.y1_y = (
                    self.y1_x - 65, self.y1_y - 59, -200, -200)
                    self.game.count_letters[24] += 1
                    self.lay_out_letters.remove('y1')
                    self.game.return_letter('y')

                elif self.lay_out_letters[-1] == 'y2':
                    self.y2 = True
                    self.board_cur_x, self.board_cur_y, self.y2_x, self.y2_y = (
                    self.y2_x - 65, self.y2_y - 59, -200, -200)
                    self.game.count_letters[24] += 1
                    self.lay_out_letters.remove('y2')
                    self.game.return_letter('y')

                elif self.lay_out_letters[-1] == 'z1' and len(self.lay_out_letters) == 1:
                    self.lay_out_control = True
                    self.z1 = True
                    self.game.count_letters[25] += 1
                    self.board_cur_x, self.board_cur_y, self.z1_x, self.z1_y = (
                    self.z1_x - 65, self.z1_y - 59, -200, -200)
                    self.lay_out_letters.remove('z1')
                    self.game.return_letter('z')

                elif self.lay_out_letters[-1] == 'z1' and len(self.lay_out_letters) > 1:
                    self.z1 = True
                    self.board_cur_x, self.board_cur_y, self.z1_x, self.z1_y = (
                    self.z1_x - 65, self.z1_y - 59, -200, -200)
                    self.game.count_letters[25] += 1
                    self.lay_out_letters.remove('z1')
                    self.game.return_letter('z')

    def check_movement(self):
        self.movement_in_game()
        if self.game.start_b or self.game.space_b:
            if self.title == 'go menu':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
                self.go_display = False
            elif self.title == 'to board':
                self.movement_board = True
                self.cursor_rect.midtop = (0 + (- 100), 0)
            elif self.title == 'bag':
                self.game.count_letters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.use_bag()
            elif self.title == 'check':
                self.check_words()
                self.lay_out_letters_doubler = self.lay_out_letters
            elif self.title == 'finish':
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.finish_page
                self.go_display = False
            elif self.title == 'tips':
                self.search_words()
        if self.game.exit_b:
            self.exit_status()


class FinishPage(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'go menu'
        self.cursor_rect.midtop = (self.middle_b_x + (- 125), self.middle_b_y)
        self.back_arrow = pygame.image.load('jpg/active image/back arrow active.png').convert_alpha()
        self.back_arrow = pygame.transform.scale(self.back_arrow, (60, 60))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.drawing('go menu', self.game.font_size, self.middle_b_x, self.middle_b_y)
                self.game.drawing('points earned ' + f'{self.game.score}', self.game.font_size, self.middle_w, self.middle_h)
            else:
                self.game.drawing('в главное меню', self.game.font_size, self.middle_b_x, self.middle_b_y)
                self.game.drawing('заработано очков ' + f'{self.game.score}', self.game.font_size, self.middle_w, self.middle_h)
            self.game.display.blit(self.back_arrow, (self.middle_b_x - 115, self.middle_b_y - 30))
            self.go_cursor()
            self.b_screen()

    def check_movement(self):
        if self.game.esc_b:
            self.game.back_menu_effect.play()
            self.game.curr_menu = self.game.main_menu
            self.game.save_settings.save()
            self.go_display = False

        if self.game.start_b or self.game.space_b:
            if self.title == 'go menu':
                self.save_achivement()
                #self.game.save_settings.save()
                self.game.back_menu_effect.play()
                self.game.curr_menu = self.game.main_menu
            self.go_display = False


# Page settings
class SettingsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.title = 'music'
        self.cursor_rect.midtop = (self.middle_w + (- 100), self.middle_h)
        self.i_music = pygame.image.load('jpg/image/single music.png').convert_alpha()
        self.i_o_s = pygame.image.load('jpg/image/single o_s.png').convert_alpha()
        self.i_back = pygame.image.load('jpg/image/single back arrow.png').convert_alpha()
        self.i_exit = pygame.image.load('jpg/image/single next arrow.png').convert_alpha()
        self.i_music_active = pygame.image.load('jpg/active image/music active.png').convert_alpha()
        self.i_o_s_active = pygame.image.load('jpg/active image/o_s active.png').convert_alpha()
        self.i_back_active = pygame.image.load('jpg/active image/back arrow active.png').convert_alpha()
        self.i_next_active = pygame.image.load('jpg/active image/next arrow active.png').convert_alpha()
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
                self.game.drawing("Settings menu", self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing("music", self.game.font_size, self.middle_w, self.middle_h)
                self.game.drawing("other", self.game.font_size, self.middle_w, self.middle_h + 40)
                self.game.drawing('back', self.game.font_size, self.middle_w, self.middle_h + 80)
                self.game.drawing("exit", self.game.font_size, self.middle_w, self.middle_h + 120)
            else:
                self.game.drawing("Меню настроек", self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing("музыка", self.game.font_size, self.middle_w, self.middle_h)
                self.game.drawing("другие", self.game.font_size, self.middle_w, self.middle_h + 40)
                self.game.drawing("назад", self.game.font_size, self.middle_w, self.middle_h + 80)
                self.game.drawing("выход", self.game.font_size, self.middle_w, self.middle_h + 120)
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
        self.volume_line = pygame.image.load('jpg/Sound.png').convert_alpha()
        self.volume_pin = pygame.image.load('jpg/Pin_sound.png').convert_alpha()
        self.volume_pin = pygame.transform.scale(self.volume_pin, (125, 125))
        self.full_volume = pygame.image.load('jpg/image/single full volume.png').convert_alpha()
        self.empty_volume = pygame.image.load('jpg/image/single empty volume.png').convert_alpha()
        self.third_volume = pygame.image.load('jpg/image/single third volume.png').convert_alpha()
        self.half_volume = pygame.image.load('jpg/image/single half volume.png').convert_alpha()
        self.i_back = pygame.image.load('jpg/image/single back arrow.png').convert_alpha()
        self.i_language = pygame.image.load('jpg/image/single language.png').convert_alpha()
        self.full_volume_active = pygame.image.load('jpg/active image/full volume active.png').convert_alpha()
        self.trird_volume_active = pygame.image.load('jpg/active image/third volume active.png').convert_alpha()
        self.half_volume_active = pygame.image.load('jpg/active image/half volume active.png').convert_alpha()
        self.empty_volume_active = pygame.image.load('jpg/active image/empty volume active.png').convert_alpha()
        self.i_back_active = pygame.image.load('jpg/active image/back arrow active.png').convert_alpha()
        self.i_language_active = pygame.image.load('jpg/active image/language active.png').convert_alpha()
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
                self.game.drawing('Other settings', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing('volume music', self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.drawing('volume effects', self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.drawing('language en', self.game.font_size, self.middle_w, self.middle_h + 50)
                self.game.drawing('back', self.game.font_size, self.middle_w, self.middle_h + 100)
            else:
                self.game.drawing('Другие настройки', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing('музыка', self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.drawing('эффекты', self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.drawing('язык ру', self.game.font_size, self.middle_w, self.middle_h + 50)
                self.game.drawing('назад', self.game.font_size, self.middle_w, self.middle_h + 100)
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
                    #self.game.save_settings.save()
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
                    #self.game.save_settings.save()
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
                    #self.game.save_settings.save()
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
        self.i_back_active = pygame.image.load('jpg/active image/back arrow active.png').convert_alpha()
        self.i_back_active = pygame.transform.scale(self.i_back_active, (60, 60))

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            if self.game.language == 'en':
                self.game.drawing('records', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing(('1 ' + f'{self.game.record}'), self.game.font_size, self.middle_w,
                                  self.middle_h - 150)
                self.game.drawing(('2 ' + f'{self.game.record2}'), self.game.font_size, self.middle_w,
                                  self.middle_h - 100)
                self.game.drawing(('3 ' + f'{self.game.record3}'), self.game.font_size, self.middle_w,
                                  self.middle_h - 50)
                self.game.drawing(('4 ' + f'{self.game.record4}'), self.game.font_size, self.middle_w, self.middle_h)
                self.game.drawing(('5 ' + f'{self.game.record5}'), self.game.font_size, self.middle_w,
                                  self.middle_h + 50)
                self.game.drawing('back', self.game.font_size, self.middle_w, self.middle_h + 100)
            else:
                self.game.drawing('рекорды', self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing(('1 ' + f'{self.game.record}'), self.game.font_size, self.middle_w,
                                  self.middle_h - 150)
                self.game.drawing(('2 ' + f'{self.game.record2}'), self.game.font_size, self.middle_w,
                                  self.middle_h - 100)
                self.game.drawing(('3 ' + f'{self.game.record3}'), self.game.font_size, self.middle_w,
                                  self.middle_h - 50)
                self.game.drawing(('4 ' + f'{self.game.record4}'), self.game.font_size, self.middle_w, self.middle_h)
                self.game.drawing(('5 ' + f'{self.game.record5}'), self.game.font_size, self.middle_w,
                                  self.middle_h + 50)
                self.game.drawing('назад', self.game.font_size, self.middle_w, self.middle_h + 100)
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
        self.music_i = pygame.image.load('jpg/image/single sound.png').convert_alpha()
        self.music_i_active = pygame.image.load('jpg/active image/sound active.png').convert_alpha()
        self.back_i = pygame.image.load('jpg/image/single back arrow.png').convert_alpha()
        self.back_active = pygame.image.load('jpg/active image/back arrow active.png').convert_alpha()
        self.full_music = pygame.image.load('jpg/image/single full volume.png').convert_alpha()
        self.full_music_active = pygame.image.load('jpg/active image/full volume active.png').convert_alpha()
        self.off_music = pygame.image.load('jpg/image/single empty volume.png').convert_alpha()
        self.off_music_active = pygame.image.load('jpg/active image/empty volume active.png').convert_alpha()
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
                self.game.drawing("Music", self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing("Starter", self.game.font_size, self.middle_w, self.middle_h - 100)
                self.game.drawing("theme 1", self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.drawing("theme 2", self.game.font_size, self.middle_w, self.middle_h)
                self.game.drawing("theme 3", self.game.font_size, self.middle_w, self.middle_h + 50)
                self.game.drawing("off * on music", self.game.font_size, self.middle_w, self.middle_h + 100)
                self.game.drawing("back", self.game.font_size, self.middle_w, self.middle_h + 150)
            else:
                self.game.drawing("Музыка", self.game.font_size_Upper, self.label_rules_x, self.label_rules_y)
                self.game.drawing("Основная", self.game.font_size, self.middle_w, self.middle_h - 100)
                self.game.drawing("тема 1", self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.drawing("тема 2", self.game.font_size, self.middle_w, self.middle_h)
                self.game.drawing("тема 3", self.game.font_size, self.middle_w, self.middle_h + 50)
                self.game.drawing("вкл * выкл", self.game.font_size, self.middle_w, self.middle_h + 100)
                self.game.drawing("назад", self.game.font_size, self.middle_w, self.middle_h + 150)
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
                pygame.mixer.music.load('music/Start music.mp3')
                pygame.mixer.music.play()
                self.game.music = True
            elif self.title == 'theme 1':
                self.game.accept_setting.play()
                self.game.p_music = 'music/Theme 1.mp3'
                pygame.mixer.music.load('music/Theme 1.mp3')
                pygame.mixer.music.play()
                self.game.music = True
            elif self.title == 'theme 2':
                self.game.accept_setting.play()
                self.game.p_music = 'music/Theme 2.mp3'
                pygame.mixer.music.load('music/Theme 2.mp3')
                pygame.mixer.music.play()
                self.game.music = True
            elif self.title == 'theme 3':
                self.game.accept_setting.play()
                self.game.p_music = 'music/Theme 3.mp3'
                pygame.mixer.music.load('music/Theme 3.mp3')
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


# Page of rules 1 - rules the game
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
                self.game.drawing("Rules", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.drawing(
                    "The playing field consists of 15 x 15 that is 225 squares on which the participants "
                    "of the game lay out letters",
                    self.game.font_size, self.middle_w, self.middle_h - 350)
                self.game.drawing(
                    "thereby making words At the beginning of the game each player receives 7 random letters",
                    self.game.font_size, self.middle_w, self.middle_h - 300)
                self.game.drawing("( there are 104 in total in the game 131 in Scrabble )",
                                  self.game.font_size, self.middle_w, self.middle_h - 250)
                self.game.drawing("Through the central cell of the playing field the first word is laid out"
                                  " horizontally or vertically", self.game.font_size, self.middle_w,
                                  self.middle_h - 200)
                self.game.drawing("then the next player can add the word ( to the intersection ) from their letters",
                                  self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.drawing("Words are laid out either from left to right or from top to bottom",
                                  self.game.font_size, self.middle_w, self.middle_h - 100)
                self.game.drawing(
                    "Each player aims to win the game by creating more words based on the available letter "
                    "tiles to score more points",
                    self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.drawing("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
                self.game.drawing("go menu", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
            else:
                self.game.drawing("Правила", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.drawing(
                    "Игровое поле состоит из 15 х 15, то есть 225 квадратов, на которые участники игры "
                    "выкладывают буквы ",
                    self.game.font_size, self.middle_w, self.middle_h - 350)
                self.game.drawing(
                    "составляя слова В начале игры каждый игрок получает по 7 случайных букв",
                    self.game.font_size, self.middle_w, self.middle_h - 300)
                self.game.drawing("( всего в игре 100 букв )",
                                  self.game.font_size, self.middle_w, self.middle_h - 250)
                self.game.drawing("Через центральную ячейку игрового поля выкладывается первое слово"
                                  " горизонтально или вертикально", self.game.font_size, self.middle_w,
                                  self.middle_h - 200)
                self.game.drawing("Следующий игрок может добавить слово (к пересечению) из своих букв",
                                  self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.drawing("Words are laid out either from left to right or from top to bottom",
                                  self.game.font_size, self.middle_w, self.middle_h - 100)
                self.game.drawing(
                    "Каждый игрок стремится выиграть игру, создавая больше слов на основе доступной буквы. "
                    "чтобы набрать больше очков",
                    self.game.font_size, self.middle_w, self.middle_h - 50)
                self.game.drawing("далее", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
                self.game.drawing("в меню", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
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
                self.game.drawing("Glossary", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.drawing("It is allowed to use all the words given in the standard dictionary of the language "
                                  "with the exception of *", self.game.font_size, self.middle_w, self.middle_h - 400)
                self.game.drawing("words that are written with capital letters",
                                  self.game.font_size, self.middle_w - 335, self.middle_h - 350)
                self.game.drawing("abbreviation", self.game.font_size, self.middle_w - 595, self.middle_h - 300)
                self.game.drawing("words that are written with an apostrophe",
                                  self.game.font_size, self.middle_w - 350, self.middle_h - 250)
                self.game.drawing("words that are written with a hyphen",
                                  self.game.font_size, self.middle_w - 394, self.middle_h - 200)
                self.game.drawing("If a word does not have a nominative case or a singular number it is allowed to "
                                  "use this word in any case or number",
                                  self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.drawing("Do not use a dictionary to look up words",
                                  self.game.font_size, self.middle_w - 530, self.middle_h - 50)
                self.game.drawing("Dictionary is allowed only in the case of checking the existence of an "
                                  "already composed word", self.game.font_size, self.middle_w - 100, self.middle_h)
                self.game.drawing("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.drawing("go menu", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.drawing("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
            else:
                self.game.drawing("Глоссарий", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.drawing("Разрешается использовать все слова, приведенные в словаре "
                                  "за исключением *", self.game.font_size, self.middle_w, self.middle_h - 400)
                self.game.drawing("слова которые пишутся с большой буквы",
                                  self.game.font_size, self.middle_w - 335, self.middle_h - 350)
                self.game.drawing("аббревиатуры", self.game.font_size, self.middle_w - 595, self.middle_h - 300)
                self.game.drawing("слова, которые пишутся с апострофом",
                                  self.game.font_size, self.middle_w - 350, self.middle_h - 250)
                self.game.drawing("слова которые пишутся через дефис",
                                  self.game.font_size, self.middle_w - 394, self.middle_h - 200)
                self.game.drawing("Если слово не имеет именительного падежа или единственного числа, то допускается "
                                  "используйте это слово в любом падеже или числе",
                                  self.game.font_size, self.middle_w, self.middle_h - 150)
                self.game.drawing("Не используйте словарь для поиска слов",
                                  self.game.font_size, self.middle_w - 530, self.middle_h - 50)
                self.game.drawing("Словарь допускается только в случае проверки существования "
                                  "уже составленное слово", self.game.font_size, self.middle_w - 100, self.middle_h)
                self.game.drawing("назад", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.drawing("в меню", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.drawing("далее", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
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
                self.game.drawing("Game process", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.drawing("* At the beginning of the game everyone is given 7 tiles "
                                  "Only one word is allowed per turn",
                                  self.game.font_size, self.middle_w - 100, self.middle_h - 400)
                self.game.drawing("Each new word must touch or have a common letter ( or letters ) "
                                  "with previously composed words", self.game.font_size, self.middle_w - 80,
                                  self.middle_h - 350)
                self.game.drawing("Words should be read from left to right ( horizontally ) and from "
                                  "top to bottom ( vertically )",
                                  self.game.font_size, self.middle_w - 117, self.middle_h - 300)
                self.game.drawing("* The first composed word must go through the central cell",
                                  self.game.font_size, self.middle_w - 410, self.middle_h - 200)
                self.game.drawing("* If the player does not want or cannot make a single word he has the right "
                                  "to change any number of his letters", self.game.font_size, self.middle_w,
                                  self.middle_h - 100)
                self.game.drawing("* Any sequence of letters horizontally and vertically must be a word",
                                  self.game.font_size, self.middle_w - 335, self.middle_h)
                self.game.drawing("* After each move you need to get new letters up to seven",
                                  self.game.font_size, self.middle_w - 430, self.middle_h + 100)
                self.game.drawing("* If a player has used all seven tiles during a turn then an "
                                  "additional 50 points are awarded to him",
                                  self.game.font_size, self.middle_w - 105, self.middle_h + 200)
                self.game.drawing("* The game ends if you run out of chips in your hand and there are no "
                                  "more chips to draw",
                                  self.game.font_size, self.middle_w - 200, self.middle_h + 270)
                self.game.drawing("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.drawing("go menu", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.drawing("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
            else:
                self.game.drawing("Игровой процесс", self.game.font_size_Upper, self.middle_w, self.middle_h - 450)
                self.game.drawing("* В начале игры каждому дается по 7 букв "
                                  "допускается составить только одно слово за ход",
                                  self.game.font_size, self.middle_w - 100, self.middle_h - 400)
                self.game.drawing("Каждое новое слово должно касаться или иметь общую букву (или буквы) "
                                  "с ранее составленными словами", self.game.font_size, self.middle_w - 80,
                                  self.middle_h - 350)
                self.game.drawing("Слова следует читать слева направо (по горизонтали) и с "
                                  "сверху вниз (по вертикали)",
                                  self.game.font_size, self.middle_w - 117, self.middle_h - 300)
                self.game.drawing("* Первое составленное слово должно пройти через центральную ячейку",
                                  self.game.font_size, self.middle_w - 410, self.middle_h - 200)
                self.game.drawing("* Если игрок не может составить ни одного слова, он имеет право "
                                  "добавить себе буквы", self.game.font_size, self.middle_w,
                                  self.middle_h - 100)
                self.game.drawing("* Любая последовательность букв по горизонтали и вертикали должна быть словом",
                                  self.game.font_size, self.middle_w - 335, self.middle_h)
                self.game.drawing("* После каждого хода нужно пополнять запас новыми буквами ( до 7 )",
                                  self.game.font_size, self.middle_w - 430, self.middle_h + 100)
                self.game.drawing("* * Если игрок использовал все 7 букв за ход то "
                                  "ему начисляются дополнительные 50 баллов",
                                  self.game.font_size, self.middle_w - 105, self.middle_h + 200)
                self.game.drawing("* Игра заканчивается, если у вас в руке закончились буквы и нет  "
                                  "больше дополнительных для розыгрыша",
                                  self.game.font_size, self.middle_w - 200, self.middle_h + 270)
                self.game.drawing("назад", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.drawing("в меню", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.drawing("далее", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
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
        self.letters = pygame.image.load('jpg/count letters.png').convert_alpha()

    def draw_menu(self):
        self.go_display = True
        while self.go_display:
            self.movement_in_menu()
            self.game.movement_button()
            self.check_movement()
            self.game.display.fill(self.game.black)
            self.game.display.blit(self.letters, (self.middle_w - 300, self.middle_h - 400))
            if self.game.language == 'en':
                self.game.drawing("Chip distribution and letter values", self.game.font_size_Upper, self.middle_w, self.middle_h - 400)
                self.game.drawing("go menu", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.drawing("next", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
                self.game.drawing("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
            else:
                self.game.drawing("Количество и цена букв", self.game.font_size_Upper, self.middle_w, self.middle_h - 400)
                self.game.drawing("в меню", self.game.font_size, self.middle_w, self.middle_h + 350)
                self.game.drawing("далее", self.game.font_size, self.middle_w + 700, self.middle_h + 350)
                self.game.drawing("назад", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
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
                self.game.drawing("Scoring and bonuses", self.game.font_size_Upper, self.label_rules_x,
                                  self.label_rules_y)
                self.game.drawing("Each letter is assigned a number of points from 1 to 10 Some squares on the "
                                  "board are painted in different colors ", self.game.font_size, self.middle_w,
                                  self.middle_h - 350)
                self.game.drawing("The number of points a player receives for a laid out word is calculated as "
                                  "follows", self.game.font_size, self.middle_w - 225, self.middle_h - 300)
                self.game.drawing("* if the box under the letter is empty the number of points written on the letter "
                                  "is added", self.game.font_size, self.middle_w - 173, self.middle_h - 200)
                self.game.drawing('* if the square is blue the number of points of the letter is multiplied by 2',
                                  self.game.font_size,
                                  self.middle_w - 290, self.middle_h - 150)
                self.game.drawing('* if the square is pink the score of the whole word is multiplied by 2',
                                  self.game.font_size,
                                  self.middle_w - 343, self.middle_h - 100)
                self.game.drawing('* if the square is blue the score of the letter is multiplied by 3',
                                  self.game.font_size,
                                  self.middle_w - 380, self.middle_h - 50)
                self.game.drawing('* if the square is red the score of the whole word is multiplied by 3',
                                  self.game.font_size,
                                  self.middle_w - 350, self.middle_h)
                self.game.drawing("back", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.drawing("go menu", self.game.font_size, self.middle_b_x, self.middle_b_y)
            else:
                self.game.drawing("Подсчет очков и бонусов", self.game.font_size_Upper, self.label_rules_x,
                                  self.label_rules_y)
                self.game.drawing("Каждой букве присваивается количество баллов от 1 до 10. Некоторые ячейки на "
                                  "доске окрашены в разные цвета ", self.game.font_size, self.middle_w,
                                  self.middle_h - 350)
                self.game.drawing("Количество очков, получаемых игроком за выложенное слово, рассчитывается так *",
                                  self.game.font_size, self.middle_w - 225, self.middle_h - 300)
                self.game.drawing(
                    "* Если поле под буквой пустое то количество начисляемых очков считается за сумму букв",
                    self.game.font_size, self.middle_w - 173, self.middle_h - 200)
                self.game.drawing('* Eсли ячейка голубая то количество баллов за буквы умножается на 2',
                                  self.game.font_size,
                                  self.middle_w - 290, self.middle_h - 150)
                self.game.drawing('* Если ячейка красная то количество баллов за всё слово умножается на 2',
                                  self.game.font_size,
                                  self.middle_w - 343, self.middle_h - 100)
                self.game.drawing('* Eсли ячейка синяя то количество баллов за букву умножается на 3',
                                  self.game.font_size,
                                  self.middle_w - 380, self.middle_h - 50)
                self.game.drawing('* Если ячейка красная то количество баллов за слово умножается на 3',
                                  self.game.font_size,
                                  self.middle_w - 350, self.middle_h)
                self.game.drawing("назад", self.game.font_size, self.middle_w - 700, self.middle_h + 350)
                self.game.drawing("в меню", self.game.font_size, self.middle_b_x, self.middle_b_y)
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