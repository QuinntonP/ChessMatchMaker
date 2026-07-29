# game.py

class Game:
    def __init__(self, white_bot, black_bot, fen):
        self.white_bot = white_bot
        self.black_bot = black_bot
        self.fen = fen

    def start_game(self):
        print("Starting game...")

        while (
            self.white_bot.send_bot_data("get-checkmate") != "checkmate"
            and self.black_bot.send_bot_data("get-checkmate") != "checkmate"
        ):
            print(self.fen)
            print("=" * 40)
            print("White's Move")

            # This waits until the white bot responds
            self.fen = self.white_bot.send_bot_data(
                f"make-move/?FEN={self.fen}"
            )

            print("=" * 40)
            print("Black's Move")

            # This waits until the black bot responds
            self.fen = self.black_bot.send_bot_data(
                f"make-move/?FEN={self.fen}"
            )

        print("Game is over")