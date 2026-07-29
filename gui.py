import pygame

pygame.init()
pygame.mixer.init()


class Gui():
    def __init__(self, WIDTH, HEIGHT, FPS):
        self.clock = pygame.time.Clock()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = FPS
        self.SQUARE_SIZE = min(WIDTH, HEIGHT) // 8
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.piece_sprites = self.load_pieces()

    def loop(self, fen):
        self.delta_time = self.clock.tick(self.FPS) / 1000.0
        self.draw(fen)


    def draw(self, fen):
        self.screen.fill((0, 0, 0))
        self.draw_board()
        self.draw_pieces(fen)
        pygame.display.flip()


    def update(self, delta_time):
        pass


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        return True


    def draw_board(self):
        pass

    def load_pieces(self):
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


    def draw_pieces(self, fen):
        pieces = self.load_pieces()

        x = 0
        y = 0

        # draw based off of fen
        for char in fen.split()[0]:
            if char.isnumeric():
                x += (self.SQUARE_SIZE * int(char))
            elif char == "/":
                y += self.SQUARE_SIZE
                x = 0
            else:
                image = pygame.transform.scale(pieces[char], (self.SQUARE_SIZE, self.SQUARE_SIZE))
                self.screen.blit(image, (x, y))
                x += self.SQUARE_SIZE


    def draw_board(self):
        white = (234, 235, 218)
        black = (43, 71, 41)

        for y in range(8):
            for x in range(8):
                color = white if (x + y) % 2 == 0 else black

                rectangle = (
                    x * self.SQUARE_SIZE,
                    y * self.SQUARE_SIZE,
                    self.SQUARE_SIZE,
                    self.SQUARE_SIZE
                )

                pygame.draw.rect(self.screen, color, rectangle)
