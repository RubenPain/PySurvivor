import pygame

import constants


class Wall:
    def __init__(self, x, y):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface(constants.WALL_SIZE)
        self.sprite.image.fill(constants.BURLYWOOD)
        self.sprite.rect = self.sprite.image.get_rect(x=x, y=y)

    def render(self, surface):
        surface.blit(self.sprite.image, self.sprite.rect)
