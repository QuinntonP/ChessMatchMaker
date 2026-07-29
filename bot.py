from rest_utils import Rest_utils

class Bot():
    def __init__(self, ip, port, depth, budget_millis, max_plies, is_white, log_moves, START_FEN):
        self.ip = ip
        self.port = port
        self.depth = depth
        self.budget_millis = budget_millis
        self.max_plies = max_plies
        self.is_white = is_white
        self.log_moves = log_moves
        self.START_FEN = START_FEN


    def run_setup(self):
        self.send_bot_data(f"new-game")
        self.send_bot_data(f"set-depth/{self.depth}")
        self.send_bot_data(f"set-budgetmillis/{self.budget_millis}")
        self.send_bot_data(f"set-maxPlies/{self.max_plies}")
        self.send_bot_data(f"set-color/{self.is_white}")
        self.send_bot_data(f"set-logMoves/{self.log_moves}")
        self.send_bot_data(f"set-FEN/?FEN={self.START_FEN}")


    def get_is_white_as_string(self):
        if self.is_white:
            return "White"
        else:
            return "Black"

    def get_is_white(self):
        return self.is_white


    def send_bot_data(self, url):
        return Rest_utils.send_data(self.ip, self.port, url)