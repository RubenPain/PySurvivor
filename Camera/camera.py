import constants


class Camera:
    def __init__(self):
        # create camera
        self.x = 0
        self.y = 0

    def update(self, target, width, height):
        # update camera position in relation to player position
        # camera is lock to the map limit (height and width), in relation to screen size
        if target.sprite.rect.x - self.x != constants.SCREEN_WIDTH / 2:
            if (self.x + constants.SCREEN_WIDTH <= width-constants.WALL_SIZE and 0 < target.sprite.rect.x - (self.x + constants.SCREEN_WIDTH / 2)) or (
                    self.x >= 0 and 0 > target.sprite.rect.x - (self.x + constants.SCREEN_WIDTH / 2)):
                self.x += target.sprite.rect.x - (self.x + constants.SCREEN_WIDTH / 2)
        if target.sprite.rect.y - self.y != constants.SCREEN_HEIGHT / 2:
            if (self.y + constants.SCREEN_HEIGHT <= height and 0 < target.sprite.rect.y - (self.y + constants.SCREEN_HEIGHT / 2)) or (
                    self.y >= 0 and 0 > target.sprite.rect.y - (self.y + constants.SCREEN_HEIGHT / 2)):
                self.y += target.sprite.rect.y - (self.y + constants.SCREEN_HEIGHT / 2)
