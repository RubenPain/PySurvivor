import pygame.transform

import constants


class StartScreen:
    def __init__(self):
        self.font_title = pygame.font.Font('freesansbold.ttf', 30)
        self.font_content = pygame.font.Font('freesansbold.ttf', 22)
        self.text_play = self.font_content.render("Appuyez sur n'importe quelle touche pour commencer", True, constants.WHITE)
        self.textRect_play = self.text_play.get_rect()
        self.textRect_play.center = (constants.SCREEN_WIDTH/2, (constants.SCREEN_HEIGHT/2)-30)

        self.text_title = self.font_title.render('PySurvivor', True, constants.WHITE)
        self.textRect_title = self.text_title.get_rect()
        self.textRect_title.center = (constants.SCREEN_WIDTH/2, (constants.SCREEN_HEIGHT/2)-60)

        self.arrow = pygame.transform.scale(pygame.image.load('assets/arrow.png'), (60, 60))
        self.arrow_rect = self.arrow.get_rect()
        self.arrow_rect.center = (constants.SCREEN_WIDTH/2-((constants.SCREEN_WIDTH/2)/2), (constants.SCREEN_HEIGHT/2)+60)

        self.text_arrow = self.font_content.render('Déplacez vous avec les flèches', True, constants.WHITE)
        self.textRect_arrow = self.text_arrow.get_rect()
        self.textRect_arrow.center = (constants.SCREEN_WIDTH/2-((constants.SCREEN_WIDTH/2)/2), (constants.SCREEN_HEIGHT/2)+110)

        self.space = pygame.transform.scale(pygame.image.load('assets/space.png'), (90, 40))
        self.space_rect = self.space.get_rect()
        self.space_rect.center = (constants.SCREEN_WIDTH/2+((constants.SCREEN_WIDTH/2)/2), (constants.SCREEN_HEIGHT/2)+60)

        self.text_space = self.font_content.render('Tirez avec la barre espace', True, constants.WHITE)
        self.textRect_space = self.text_space.get_rect()
        self.textRect_space.center = (constants.SCREEN_WIDTH/2+((constants.SCREEN_WIDTH/2)/2), (constants.SCREEN_HEIGHT/2)+100)

    def render(self, surface):
        surface.fill(constants.BLUE)
        surface.blit(self.text_title, self.textRect_title)
        surface.blit(self.text_play, self.textRect_play)
        surface.blit(self.arrow, self.arrow_rect)
        surface.blit(self.space, self.space_rect)
        surface.blit(self.text_space, self.textRect_space)
        surface.blit(self.text_arrow, self.textRect_arrow)
        pygame.display.flip()