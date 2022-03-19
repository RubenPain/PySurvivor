import pygame as pg

import constants
from Entities.player import Player
from Map.map import Map
from Camera.camera import Camera
from Screen.game_over import GameOver
from Screen.start_screen import StartScreen
from sound import Sound


class Game:
    def __init__(self, screen):
        Sound().play()
        self.screen = screen
        self.running = True
        self.clock = pg.time.Clock()
        self.map = Map()
        self.player = Player(280, 120)
        self.camera = Camera()
        self.rows, self.cols = 64, 64
        self.round = 0
        self.game_over = False
        self.play = False

    def reset(self):
        self.map = Map()
        self.player = Player(280, 120)
        self.camera = Camera()
        self.round = 0

    def handling_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        keys = pg.key.get_pressed()

        if True in keys and not self.play and not self.game_over:
            self.play = True

        if keys[pg.K_SPACE] and self.game_over:
            self.reset()
            self.play = True

        self.player.direction = [False, False, False, False]

        if keys[pg.K_SPACE]:
            if len(self.player.weapon.bullets)<1:
                self.player.weapon.shoot(self.map.enemies)

        if keys[pg.K_LEFT]:
            if not self.player.collide(self.map.wallArray, self.camera.x, self.camera.y, 'left'):
                self.player.direction[2] = True
        elif keys[pg.K_RIGHT]:
            if not self.player.collide(self.map.wallArray, self.camera.x, self.camera.y, 'right'):
                self.player.direction[3] = True

        if keys[pg.K_UP]:
            if not self.player.collide(self.map.wallArray, self.camera.x, self.camera.y, 'top'):
                self.player.direction[0] = True

        elif keys[pg.K_DOWN]:
            if not self.player.collide(self.map.wallArray, self.camera.x, self.camera.y, 'bottom'):
                self.player.direction[1] = True

    def update(self):
        self.player.update()
        not_all_dead = False
        for enemy in self.map.enemies:
            if enemy.life>0:
                not_all_dead = True
                enemy.move(self.player, self.camera.x, self.camera.y, self.map.wallArray)
        if not not_all_dead:
            self.map.enemies.clear()
        if self.player.injury(self.map.enemies):
            if self.player.life == 0:
                self.game_over = True
                self.play = False
        for bullet in self.player.weapon.bullets:
            if bullet.dead(self.map.enemies) or bullet.collide(self.map.wallArray, [self.camera.x, self.camera.y]) or bullet.living_time>50:
                self.player.weapon.bullets.pop(self.player.weapon.bullets.index(bullet))
            bullet.move()
        if not self.map.enemies:
            self.round += 1
            self.map.nextRound(self.camera.x, self.camera.y, self.round)

    def draw_grid(self):
        for r in range(self.rows+1):
            pg.draw.line(self.screen, constants.WHITE, (0-self.camera.x, r*constants.WALL_SIZE[0]-self.camera.y), (self.cols*constants.WALL_SIZE[1]-self.camera.x, r*constants.WALL_SIZE[0]-self.camera.y))
        for c in range(self.cols+1):
            pg.draw.line(self.screen, constants.WHITE, (c*constants.WALL_SIZE[1]-self.camera.x, 0-self.camera.y), (c*constants.WALL_SIZE[1]-self.camera.x, self.rows*constants.WALL_SIZE[0]-self.camera.y))

    def display(self):
        self.screen.fill(constants.GRAY)
        self.draw_grid()
        self.map.render(self.screen, self.camera.x, self.camera.y, self.round)
        for enemy in self.map.enemies:
            self.screen.blit(enemy.sprite.image, (enemy.sprite.rect.x-self.camera.x, enemy.sprite.rect.y-self.camera.y))
        self.player.render(self.screen, self.camera.x, self.camera.y, self.round)
        self.camera.update(self.player, self.map.width, self.map.height)
        pg.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            if self.play:
                self.update()
                self.display()
            elif self.game_over:
                GameOver().render(self.screen, self.round)
            else:
                StartScreen().render(self.screen)
                pg.display.flip()
            self.clock.tick(constants.FPS)
