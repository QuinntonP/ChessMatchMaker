from bot import Bot
from game import Game
from gui import Gui

import pygame
import sys
import threading

PLAY_SOUNDS = True

WIDTH = 800
HEIGHT = 800
FPS = 60


def load_sounds():
    lookup = dict()

    lookup["move-piece"] = pygame.mixer.Sound("sounds/move-self.wav")
    
    return lookup


def create_game():
    start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    bot_1 = Bot(
        ip="localhost",
        port="8080",
        depth=5,
        budget_millis=5000,
        max_plies=600,
        is_white=True,
        log_moves=True,
        START_FEN=start_fen
    )

    bot_2 = Bot(
        ip="localhost",
        port="8081",
        depth=5,
        budget_millis=5000,
        max_plies=600,
        is_white=False,
        log_moves=True,
        START_FEN=start_fen
    )

    bot_1.run_setup()
    bot_2.run_setup()

    return Game(load_sounds(), PLAY_SOUNDS, bot_1, bot_2, start_fen)


def main():
    game = create_game()

    game_thread = threading.Thread(
        target=game.start_game,
        daemon=True
    )

    game_thread.start()

    running = True
    gui = Gui(WIDTH, HEIGHT, FPS)

    while running:
        gui.loop(game.fen)

        running = gui.handle_events()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()