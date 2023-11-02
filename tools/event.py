import sys
from tools.jsonManager import *
from gamefiles.game import *
import pygame


class Event:
    def __init__(self, game):
        self.game = game
        self.settings = JsonSettingsManager()
        self.gamepad_count = pygame.joystick.get_count()


class ControllerEvent(Event):
    def __init__(self, game):
        Event.__init__(self, game)

        self.mouse_visibility = self.settings.get_mouse_visible_application()

        self.right_click = False
        self.left_click = False

        self.pause_button = False
        self.space_button = False
        self.backspace_button = False
        self.home_button = False
        self.esc_button = False
        self.end_button = False
        self.return_button = False
        self.delete_button = False

        self.arrow_left = False
        self.arrow_up = False
        self.arrow_down = False
        self.arrow_right = False

        self.a_button = False
        self.b_button = False
        self.c_button = False
        self.d_button = False
        self.e_button = False
        self.f_button = False
        self.g_button = False
        self.h_button = False
        self.i_button = False
        self.j_button = False
        self.k_button = False
        self.l_button = False
        self.m_button = False
        self.n_button = False
        self.o_button = False
        self.p_button = False
        self.q_button = False
        self.r_button = False
        self.s_button = False
        self.t_button = False
        self.u_button = False
        self.v_button = False
        self.w_button = False
        self.x_button = False
        self.y_button = False
        self.z_button = False

    # detecting pressing default not letters button
    def movement(self, additional: bool):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                self.game.curr_menu.go_display = False

            # detect mouse pressing
            if pygame.mouse.get_visible():

                # left click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.left_click = True

                # right click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    self.right_click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAUSE:
                    self.pause_button = True
                if event.key == pygame.K_ESCAPE:
                    self.esc_button = True
                if event.key == pygame.K_DOWN:
                    self.arrow_down = True
                if event.key == pygame.K_UP:
                    self.arrow_up = True
                if event.key == pygame.K_RIGHT:
                    self.arrow_right = True
                if event.key == pygame.K_LEFT:
                    self.arrow_left = True
                if event.key == pygame.K_DELETE:
                    self.delete_button = True
                if event.key == pygame.K_RETURN:
                    self.return_button = True
                if event.key == pygame.K_SPACE:
                    self.space_button = True
                if event.key == pygame.K_END:
                    self.end_button = True
                if event.key == pygame.K_HOME:
                    self.home_button = True
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_button = True

            # if true -> adding detect press letter button
            if additional:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.q_button = True
                    if event.key == pygame.K_w:
                        self.w_button = True
                    if event.key == pygame.K_e:
                        self.e_button = True
                    if event.key == pygame.K_r:
                        self.r_button = True
                    if event.key == pygame.K_t:
                        self.t_button = True
                    if event.key == pygame.K_y:
                        self.y_button = True
                    if event.key == pygame.K_u:
                        self.u_button = True
                    if event.key == pygame.K_i:
                        self.i_button = True
                    if event.key == pygame.K_o:
                        self.o_button = True
                    if event.key == pygame.K_p:
                        self.p_button = True
                    if event.key == pygame.K_a:
                        self.a_button = True
                    if event.key == pygame.K_s:
                        self.s_button = True
                    if event.key == pygame.K_d:
                        self.d_button = True
                    if event.key == pygame.K_f:
                        self.f_button = True
                    if event.key == pygame.K_g:
                        self.g_button = True
                    if event.key == pygame.K_l:
                        self.l_button = True
                    if event.key == pygame.K_z:
                        self.z_button = True
                    if event.key == pygame.K_x:
                        self.x_button = True
                    if event.key == pygame.K_c:
                        self.c_button = True
                    if event.key == pygame.K_v:
                        self.v_button = True
                    if event.key == pygame.K_b:
                        self.b_button = True
                    if event.key == pygame.K_n:
                        self.n_button = True
                    if event.key == pygame.K_m:
                        self.m_button = True
