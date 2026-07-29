class Game:
    def __init__(self, sounds, play_sounds, white_bot, black_bot, fen):
        self.sounds = sounds
        self.play_sounds = play_sounds
        self.white_bot = white_bot
        self.black_bot = black_bot
        self.fen = fen


    def start_game(self):
        print("Starting game...")

        count = 0
        bot = self.white_bot

        while (self.white_bot.send_bot_data("get-checkmate") != "checkmate" and self.black_bot.send_bot_data("get-checkmate") != "checkmate"):
            if count % 2 == 0:
                bot = self.white_bot
            else:
                bot = self.black_bot

            self.make_move(bot)

        print("Game is over")


    def make_move(self, bot):
        print(self.fen)
        print("=" * 40)
        # print(f"{bot.get_is_white_as_string()}'s Move")

        # This waits until the white bot responds
        self.fen = bot.send_bot_data(
            f"make-move/?FEN={self.fen}"
        )

        if self.play_sounds:
            self.sounds["move-piece"].play()
