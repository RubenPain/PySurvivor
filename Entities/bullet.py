import pygame
from sound import Sound


class Bullet:
    def __init__(self, x, y, direction):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(pygame.image.load('assets/bullet.png'), (30,30))
        self.sprite.rect = self.sprite.image.get_rect(x=x, y=y)
        self.speed = 8
        self.direction = direction
        self.living_time = 0

    def dead(self, enemies):
        # check if bullet collide with an enemy, then enemy loose life and can die
        enemies_group = pygame.sprite.Group()
        for enemy in enemies:
            enemies_group.add(enemy.sprite)
        if pygame.sprite.spritecollide(self.sprite, enemies_group, True):
            for enemy in enemies:
                if enemy.sprite not in enemies_group:
                    enemy.life -= 5
                    if enemy.life <= 0:
                        Sound().sound('skeleton_death.mp3')
                        enemy.sprite.image = pygame.transform.scale(pygame.image.load('assets/grave.png').convert_alpha(), (40, 40))
            return True
        return False

    def collide(self, walls, cam):
        # bullet also being deleted when enter in collision with a wall
        # walls are rendered in relation to camera position, so we need to add it when we check collision
        for wall in walls:
            wall.sprite.rect.x += cam[0]
            wall.sprite.rect.y += cam[1]
            if pygame.sprite.collide_mask(self.sprite, wall.sprite):
                wall.sprite.rect.x -= cam[0]
                wall.sprite.rect.y -= cam[1]
                return True
            wall.sprite.rect.x -= cam[0]
            wall.sprite.rect.y -= cam[1]
        return False

    def move(self):
        self.sprite.rect.x += self.direction.x*self.speed
        self.sprite.rect.y += self.direction.y*self.speed
        self.living_time += 1