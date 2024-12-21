import pygame as pg


# Initializing the pygame screen
screen = None
clock = None
running = True
def initializePygame():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
initializePygame()


def main():
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


main()
pg.quit()