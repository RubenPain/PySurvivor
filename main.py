import pygame as pg
from Screen.game import Game
import constants


pg.init()

pg.display.set_caption("PySurvivor")
game = Game(constants.SCREEN)
game.run()

pg.quit()
