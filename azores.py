import pygame as pg
import sys
import json


if len(sys.argv) != 2:
    print("USAGE: python azores.py games/FOLDER")
    sys.exit()
game = sys.argv[1]


# Initializing the pygame screen
running = True
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()


## Start of reading game file
def read_core(path):
    path += "/core.txt" # makes sure we're reading core
    f = open(path, "r")
    title = f.readline()
    pg.display.set_caption(title) # sets title of page to game title.
    return f.readline()
world = read_core(game)


entities = {}
def read_entities(path):
    path += "/entities.json"
    f = open(path, "r")
    return json.loads(f.read())
entities = read_entities(game)
## End of reading game file


def display_world(path):
    path += "/worlds/" + world + ".json"
    f = open(path, "r")
    temp = json.loads(f.read())
    world_load = temp.get("world")
    for y, y_value in enumerate(world_load):
        for x, x_value in enumerate(y_value):
            square = pg.Rect(x * 60, y * 60, 60, 60)
            color = (255,0,0)
            if entities.get(x_value)[1]:
                brightness = entities.get(x_value)[2]
                environment = temp.get("environment")
                color = (int(environment[0] * brightness), int(environment[1] * brightness), int(environment[2] * brightness))
            else:
                color = (entities.get(x_value)[3][0], entities.get(x_value)[3][1], entities.get(x_value)[3][2])
            pg.draw.rect(screen, color, square)
display_world(game)


while running:
    for event in pg.event.get(): # closes game when player clicks X button
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()

    clock.tick(10)


pg.quit()