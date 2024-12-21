import pygame as pg
import sys


if len(sys.argv) != 2:
    print("USAGE: python azores.py games/FOLDER")
    sys.exit()


# Initializing the pygame screen
screen = None
clock = None
running = True

def initializePygame():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
initializePygame()

def read_core(path):
    path += "/core.txt" # makes sure we're reading core
    f = open(path, "r")
    title = f.readline()
    pg.display.set_caption(title) # sets title of page to game title.
read_core(sys.argv[1])


while running:
    for event in pg.event.get(): # closes game when player clicks X button
        if event.type == pg.QUIT:
            running = False


pg.quit()