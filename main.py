import pygame as pg

if __name__ == "__main__":
    import sys

    screen = pg.display.set_mode((1200, 900))
    pg.display.set_caption("Gobang but Multiplayer")
    bg = pg.image.load("res/img/bg.png")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            screen.blit(bg, (0, 0))
            pg.display.update()
