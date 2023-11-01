from game import Game

game = Game()


def load_settings():
    game.music = game.save_settings.get('music status')
    game.p_music = game.save_settings.get('music')
    game.language = game.save_settings.get('language')
    game.record = game.save_settings.get('record')


while game.running:
    #load_settings()
    game.curr_menu.draw_menu()
