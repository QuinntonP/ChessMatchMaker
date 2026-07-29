from bot import Bot
from game import Game

import pygame
import sys
import threading


pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Project")

SQUARE_SIZE = min(WIDTH, HEIGHT) // 8

clock = pygame.time.Clock()


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

    return Game(bot_1, bot_2, start_fen)


def load_pieces():
    lookup = dict()

    # White
    lookup["P"] = pygame.image.load("sprites/white-pawn.png")
    lookup["R"] = pygame.image.load("sprites/white-rook.png")
    lookup["N"] = pygame.image.load("sprites/white-knight.png")
    lookup["B"] = pygame.image.load("sprites/white-bishop.png")
    lookup["K"] = pygame.image.load("sprites/white-king.png")
    lookup["Q"] = pygame.image.load("sprites/white-queen.png")

    # Black
    lookup["p"] = pygame.image.load("sprites/black-pawn.png")
    lookup["r"] = pygame.image.load("sprites/black-rook.png")
    lookup["n"] = pygame.image.load("sprites/black-knight.png")
    lookup["b"] = pygame.image.load("sprites/black-bishop.png")
    lookup["k"] = pygame.image.load("sprites/black-king.png")
    lookup["q"] = pygame.image.load("sprites/black-queen.png")

    return lookup


def draw_pieces(fen):
    pieces = load_pieces()

    x = 0
    y = 0

    # draw based off of fen
    for char in fen.split()[0]:
        if char.isnumeric():
            x += (SQUARE_SIZE * int(char))
        elif char == "/":
            y += SQUARE_SIZE
            x = 0
        else:
            image = pygame.transform.scale(pieces[char], (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(image, (x, y))
            x += SQUARE_SIZE
        



def draw_board():
    white = (255, 247, 212)
    black = (43, 71, 41)

    for y in range(8):
        for x in range(8):
            color = white if (x + y) % 2 == 0 else black

            rectangle = (
                x * SQUARE_SIZE,
                y * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            )

            pygame.draw.rect(screen, color, rectangle)


def draw(fen):
    screen.fill((0, 0, 0))
    draw_board()
    draw_pieces(fen)
    pygame.display.flip()


def update(delta_time):
    pass


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

    return True


def main():
    game = create_game()

    game_thread = threading.Thread(
        target=game.start_game,
        daemon=True
    )

    game_thread.start()

    running = True

    while running:
        delta_time = clock.tick(FPS) / 1000.0

        running = handle_events()
        update(delta_time)
        draw(game.fen)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()