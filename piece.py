import pygame as pg
from enum import Enum


class PieceColor(Enum):
    BLACK = -1
    WHITE = 1


class GamePiece(pg.sprite.Sprite):
    def __init__(self, color: PieceColor):
        super().__init__()
        self.image = pg.image.load("res/img/%s_piece.png" % ("black" if color == PieceColor.BLACK else "white")) \
                     .convert_alpha()
