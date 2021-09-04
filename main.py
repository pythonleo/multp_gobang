import sys
import pygame as pg
from board import GameBoard
from piece import GamePiece, PieceColor
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE


class Game:
    """ Class for a game of Gobang. """
    def __init__(self, bg="res/img/bg.png", color: PieceColor = PieceColor.BLACK):
        """ Initializes the game. The player sending the request will have black pieces. """

        self._screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.bg = pg.image.load(bg)

        self._color = color
        self._game_board = GameBoard(self._screen)
        self._temporary_piece = GamePiece(color)

    def draw(self):
        self._screen.blit(self.bg, (0, 0))
        self._game_board.draw()

    def on_event(self, event):
        if event.type == pg.QUIT:
            sys.exit()

        self._game_board.on_event(event)

    def on_tick(self):
        for event in pg.event.get():
            self.on_event(event)

        self.draw()
        pg.display.update()


if __name__ == "__main__":
    game = Game()

    while True:
        game.on_tick()
