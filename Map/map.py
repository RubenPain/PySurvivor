import random

import Entities.wall, Entities.player, Entities.enemy
import constants


class Map:
    def __init__(self):
        self.file = open("/Users/rubenpain/Documents/Scolarité/IIM/Cours/Python/Rendu/PySurvivor/Map/map.txt", 'r')
        self.array = []
        self.wallArray = []
        # create an array from our txt file, to avoid open it every time we render the map
        for line in self.file:
            self.array.append([])
            for i in line:
                self.array[len(self.array) - 1].append(i)
        self.width = len(self.array[0]) * constants.WALL_SIZE[0]
        self.height = len(self.array) * constants.WALL_SIZE[1]
        self.enemies = []

    def render(self, surface, cam_x, cam_y, round):
        # browse array and in function of characters instantiate good element
        # set their position in function of camera position
        self.wallArray.clear()
        y = 0
        for line in self.array:
            x = 0
            for i in line:
                if i == '#':
                    wall = Entities.wall.Wall(x - cam_x, y - cam_y)
                    wall.render(surface)
                    self.wallArray.append(wall)
                if i == 'E':
                    self.array[self.array.index(line)][self.array[self.array.index(line)].index(i)] = '.'
                    enemy = Entities.enemy.Enemy(x - cam_x, y - cam_y, round)
                    self.enemies.append(enemy)
                x += constants.WALL_SIZE[0]
            y += constants.WALL_SIZE[1]

    def nextRound(self, cam_x, cam_y, rnd):
        # when all enemies are dead we instantiate a new wave
        # we need to render enemy on map and we set them a random position
        # try to let them in the map (not working every time) - Don't know if they are glitching the wall or they spawn outside map
        for wall in self.wallArray:
            if len(self.enemies) < 3 + rnd:
                x = random.randint(constants.WALL_SIZE[0], self.width - constants.WALL_SIZE[0])
                y = random.randint(constants.WALL_SIZE[1], self.height - constants.WALL_SIZE[1])
                while (wall.sprite.rect.x + cam_x) <= x <= (wall.sprite.rect.right + cam_x) or (wall.sprite.rect.y - cam_y) <= y <= (
                        wall.sprite.rect.bottom - cam_y) or x+cam_x >= self.width or y+cam_y >= self.height:
                    x = random.randint(constants.WALL_SIZE[0], self.width - constants.WALL_SIZE[0])
                    y = random.randint(constants.WALL_SIZE[1], self.height - constants.WALL_SIZE[1])
                enemy = Entities.enemy.Enemy(x, y, rnd)
                self.enemies.append(enemy)
            else:
                break
