from game import Game
from bot import Bot
import pygame
import threading


class Game_runner:
    def __init__(self, result_output_path, PLAY_SOUNDS):
        self.result_output_path = result_output_path
        self.PLAY_SOUNDS = PLAY_SOUNDS

        self.game = None
        self.runner_thread = None

    def load_sounds(self):
        return {
            "move-piece": pygame.mixer.Sound("sounds/move-self.wav")
        }

    def create_game(self):
        # start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        start_fen = "k7/8/8/8/8/3r4/KP6/4r3 b - - 0 1"

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

        return Game(
            self.load_sounds(),
            self.PLAY_SOUNDS,
            bot_1,
            bot_2,
            start_fen
        )

    def start(self, num_of_games):
        # Create the first game before the GUI tries to access it
        self.game = self.create_game()

        self.runner_thread = threading.Thread(
            target=self.run_games,
            args=(num_of_games,),
            daemon=True
        )
        self.runner_thread.start()

    def run_games(self, num_of_games):
        for game_number in range(num_of_games):
            # The first game was created in start()
            if game_number > 0:
                self.game = self.create_game()

            # No additional thread needed
            print(f"starting game #{game_number}")
            self.game.white_bot.run_setup()
            self.game.black_bot.run_setup()

            self.game.start_game()

    def get_game(self):
        return self.game