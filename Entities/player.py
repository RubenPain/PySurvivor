import pygame

from Entities.weapon import Weapon
import constants


class Player:
    def __init__(self, x ,y):
        self.font = pygame.font.Font('freesansbold.ttf', 26)
        self.spritesheet = pygame.image.load('assets/spritesheet.png').convert_alpha()
        self.sprite = pygame.sprite.Sprite()
        # split the spritesheet to use every sprite on it
        self.frames = []
        cols = 9
        rows = 4
        for row in range(rows):
            self.frames.append([])
            for col in range(cols):
                rect = pygame.Rect(col*64, row*64, 64, 64)
                self.frames[len(self.frames) - 1].append(self.spritesheet.subsurface(rect))
        self.sprite.image = self.frames[0][0]
        self.sprite.rect = self.sprite.image.get_rect(x=x, y=y)
        self.sprite.mask = pygame.mask.from_surface(self.sprite.image)
        self.speed = 3
        self.direction = [False, False, False, False]
        self.weapon = Weapon(self)
        self.life = 3
        self.text = self.font.render(str(self.life), True, constants.WHITE)
        self.textRect = self.text.get_rect()
        self.textRect.center = (constants.SCREEN_WIDTH - 20, 20)
        self.i = 0

    def update(self):
        # increment in x direction
        self.sprite.rect.x += (-self.speed if self.direction[2] else 0) + (self.speed if self.direction[3] else 0)
        # increment in y direction
        self.sprite.rect.y += (-self.speed if self.direction[0] else 0) + (self.speed if self.direction[1] else 0)
        # update sprite
        if self.i >= 30:
            self.i = 0
        if self.direction[2]:
            self.sprite.image = self.frames[1][int(self.i*0.3)]
        if self.direction[3]:
            self.sprite.image = self.frames[3][int(self.i*0.3)]
        if self.direction[0]:
            self.sprite.image = self.frames[0][int(self.i*0.3)]
        if self.direction[1]:
            self.sprite.image = self.frames[2][int(self.i*0.3)]
        self.i += 1

    def injury(self, enemies):
        # check for each enemy collide, if he is alive, then adjust player life and text
        for enemy in enemies:
            if pygame.sprite.collide_mask(enemy.sprite, self.sprite) and enemy.life>0:
                enemy.life = 0
                enemy.sprite.image = pygame.transform.scale(pygame.image.load('assets/grave.png').convert_alpha(), (40, 40))
                self.life -= 1
                self.text = self.font.render(str(self.life), True, constants.WHITE)
                return True
        return False

    def collide(self, wallArray, cam_x, cam_y, direction):
        # walls are rendered in relation to camera position, so we need to add it when we check collision
        # to avoid player block, if we collide we move back a little
        collision = False
        for wall in wallArray:
            wall.sprite.rect.x += cam_x
            wall.sprite.rect.y += cam_y
            if pygame.sprite.collide_mask(self.sprite, wall.sprite):
                collision = True
                if direction == 'left':
                    self.sprite.rect.x += self.speed*2
                elif direction == 'right':
                    self.sprite.rect.x -= self.speed*2
                elif direction == 'top':
                    self.sprite.rect.y += self.speed*2
                elif direction == 'bottom':
                    self.sprite.rect.y -= self.speed*2
                wall.sprite.rect.x -= cam_x
                wall.sprite.rect.y -= cam_y
                break
            wall.sprite.rect.x -= cam_x
            wall.sprite.rect.y -= cam_y
        return collision

    def render(self, surface, cam_x, cam_y, rnd):
        # render all the element in relation to the player + text
        for bullet in self.weapon.bullets:
            surface.blit(bullet.sprite.image, (bullet.sprite.rect.x+30-cam_x, bullet.sprite.rect.y+30-cam_y))
        surface.blit(self.sprite.image, (self.sprite.rect.x-cam_x, self.sprite.rect.y-cam_y))
        surface.blit(self.text, self.textRect)
        nbr_round = self.font.render('Round '+str(rnd), True, constants.WHITE)
        round_rect = nbr_round.get_rect()
        round_rect.topleft = (20, 20)
        surface.blit(nbr_round, round_rect)
