import pygame as pg
from piece import PieceColor, GamePiece


class GameBoard:
    def __init__(self, screen: pg.Surface, color: PieceColor = PieceColor.BLACK):
        self._board = [[None for _ in range(19)] for _ in range(19)]
        self._screen = screen

        self._spawning = False
        self._mouse_on_board = False

        self._color = color
        self._temp_piece = GamePiece(color)
        self._temp_x, self._temp_y = 0, 0

    def add_piece(self, piece_color: PieceColor, x, y):
        self._board[x][y] = GamePiece(piece_color)

    def on_event(self, event):
        if event.type == pg.MOUSEMOTION:
            self._mouse_on_board = 12 <= event.pos[0] <= 888 and 12 <= event.pos[1] <= 888
            self._temp_x, self._temp_y = (event.pos[0] - 12) // 47, (event.pos[1] - 12) // 47
        if event.type == pg.MOUSEBUTTONDOWN and self._spawning and self._mouse_on_board:
            self.add_piece(self._color, self._temp_x, self._temp_y)

    def draw(self):
        for i, line in enumerate(self._board):
            for j, piece in enumerate(line):
                if isinstance(piece, GamePiece):
                    self._screen.blit(piece.image, (12 + i * 47, 12 + j * 47))

        if self._spawning and self._mouse_on_board:
            self._screen.blit(self._temp_piece.image, (12 + self._temp_x * 47, 12 + self._temp_y * 47))
