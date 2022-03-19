import pygame
import math

from Entities.bullet import Bullet
from sound import Sound


class Weapon:
    def __init__(self, player):
        self.player = player
        self.bullets = []

    def calculateDistance(self, x1, y1, x2, y2):
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return dist

    def shoot(self, enemies):
        dist = 99999
        enemy_coord = [0, 0]
        for enemy in enemies:
            if enemy.life > 0:
                if dist > self.calculateDistance(enemy.sprite.rect.x, enemy.sprite.rect.y, self.player.sprite.rect.x, self.player.sprite.rect.y):
                    dist = self.calculateDistance(enemy.sprite.rect.x, enemy.sprite.rect.y, self.player.sprite.rect.x, self.player.sprite.rect.y)
                    enemy_coord = [enemy.sprite.rect.x, enemy.sprite.rect.y]

        dirvect = pygame.math.Vector2(enemy_coord[0] - self.player.sprite.rect.x,
                                      enemy_coord[1]-self.player.sprite.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(1)
        bullet = Bullet(self.player.sprite.rect.x, self.player.sprite.rect.y, dirvect)
        self.bullets.append(bullet)
        Sound().sound('attack.mp3')