import pygame as pg # type: ignore
import sys
import json
import importlib


if len(sys.argv) != 2:
    print("USAGE: python azores.py FOLDER")
    sys.exit()
game = "games/" + sys.argv[1]


funcs_name = "games." + sys.argv[1] + ".function.functionality_tags"
imp_funcs = importlib.import_module(funcs_name)


# Initializing the pygame screen
running = True
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()


## Start of reading game file
def read_core(path):
    path += "/core.json" # sets path of core
    f = open(path, "r")
    core = json.loads(f.read())
    pg.display.set_caption(core.get("title")) # sets title of page to game title.
    return core.get("first_world")
world = read_core(game)


entities = {}
def read_entities(path):
    path += "/entities.json"
    f = open(path, "r")
    return json.loads(f.read()) # Loads dictionary from entities so we can see details about tiles
entities = read_entities(game)


def read_world(path):
    path += "/worlds/" + world + ".json"
    f = open(path, "r")
    return json.loads(f.read())
world_load = read_world(game)
## End of reading game file


def display_world(world):
    for y, y_value in enumerate(world.get("world")):
        for x, x_value in enumerate(y_value):
            square = pg.Rect(x * 60, y * 60, 60, 60)
            display_details = imp_funcs.display_tags.get(entities.get(x_value)[4])(entities.get(x_value)[2], world.get("environment"), entities.get(x_value)[3], entities.get(x_value)[1])
            if display_details[0] == 1:
                pg.draw.rect(screen, display_details[1], square)
display_world(world_load)


while running:
    for event in pg.event.get(): # closes game when player clicks X button
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()

    clock.tick(10)


pg.quit()