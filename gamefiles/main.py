from gamefiles.game import Game

game = Game()

while game.running:
    game.curr_menu.draw_menu()
