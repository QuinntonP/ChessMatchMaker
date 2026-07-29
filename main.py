import pygame
import sys

from gui import Gui
from game_runner import Game_runner

WIDTH = 800
HEIGHT = 800
FPS = 60


def main():
    pygame.init()

    game_runner = Game_runner(result_output_path="results.txt", PLAY_SOUNDS=True)
    game_runner.start(2)

    gui = Gui(WIDTH, HEIGHT, FPS)
    running = True

    while running:
        game = game_runner.get_game()

        if game is not None:
            gui.loop(game.fen)

        running = gui.handle_events()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()