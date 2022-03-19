import pygame

from sound import Sound


class Enemy:
    def __init__(self, x, y, round):
        self.spritesheet = pygame.image.load('assets/squelette.png').convert_alpha()
        self.sprite = pygame.sprite.Sprite()
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
        self.speed = 3+(round*0.3)
        self.life = 10+(round*0.3)
        self.i = 0

    def move(self, player, cam_x, cam_y, wallArray):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player.sprite.rect.x - self.sprite.rect.x,
                                      player.sprite.rect.y - self.sprite.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)

        if self.i >= 30:
            self.i = 0

        collision = self.collide(wallArray, cam_x, cam_y)
        if not collision:
            self.sprite.rect.x += dirvect.x
            self.sprite.rect.y += dirvect.y
            if dirvect.x > dirvect.y:
                if dirvect.x > 0:
                    self.sprite.image = self.frames[3][int(self.i*0.3)]
                else:
                    self.sprite.image = self.frames[1][int(self.i*0.3)]
            else:
                if dirvect.y > 0:
                    self.sprite.image = self.frames[2][int(self.i*0.3)]
                else:
                    self.sprite.image = self.frames[0][int(self.i*0.3)]
            self.i += 1
        else:
            if dirvect.x > dirvect.y:
                self.sprite.rect.x -= dirvect.x
            else:
                self.sprite.rect.y -= dirvect.y
        if -40 < player.sprite.rect.y - self.sprite.rect.y < 40 or -40 < player.sprite.rect.x - self.sprite.rect.x < 40:
            Sound().sound('walk.mp3')

    def collide(self, wallArray, cam_x, cam_y):
        collision = False

        for wall in wallArray:
            wall.sprite.rect.x += cam_x
            wall.sprite.rect.y += cam_y
            if pygame.sprite.collide_mask(self.sprite, wall.sprite):
                collision = True
                wall.sprite.rect.x -= cam_x
                wall.sprite.rect.y -= cam_y
                break
            wall.sprite.rect.x -= cam_x
            wall.sprite.rect.y -= cam_y
        return collision
