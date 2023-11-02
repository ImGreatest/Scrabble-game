import pygame


class Sprite:
    def __init__(self):
        self.cursor_board = pygame.image.load('assets/jpg/cursor board.png').convert_alpha()
        self.score_panel = pygame.image.load('assets/jpg/Score panel.png').convert_alpha()
        self.empty_box = pygame.image.load('assets/jpg/boxs/empty - box.png').convert_alpha()
        self.tws_box = pygame.image.load('assets/jpg/boxs/tws - box.png').convert_alpha()
        self.dls_box = pygame.image.load('assets/jpg/boxs/bls - box.png').convert_alpha()
        self.dws_box = pygame.image.load('assets/jpg/boxs/bws - box.png').convert_alpha()
        self.tls_box = pygame.image.load('assets/jpg/boxs/tls - box.png').convert_alpha()
        self.start_box = pygame.image.load('assets/jpg/boxs/start box.png').convert_alpha()


class Animation:
    def __init__(self):
        pass
