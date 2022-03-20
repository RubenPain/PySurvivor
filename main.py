import pygame as pg
from Screen.game import Game
import constants

# inti pygame
pg.init()

# set title to windows
pg.display.set_caption("PySurvivor")

# create a game instance
game = Game(constants.SCREEN)

# launch run function from game
game.run()

pg.quit()
