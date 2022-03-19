import pygame.display

import constants


class GameOver:
    def __init__(self):
        self.font_title = pygame.font.Font('freesansbold.ttf', 28)
        self.font_content = pygame.font.Font('freesansbold.ttf', 22)

        self.text_over = self.font_title.render('GAME OVER', True, constants.WHITE)
        self.textRect_GA = self.text_over.get_rect()
        self.textRect_GA.center = (constants.SCREEN_WIDTH/2, (constants.SCREEN_HEIGHT/2)-30)

        self.text_try_again = self.font_content.render('Appuyez sur ESPACE pour réessayer', True, constants.WHITE)
        self.textRect_TA = self.text_try_again.get_rect()
        self.textRect_TA.center = (constants.SCREEN_WIDTH/2, (constants.SCREEN_HEIGHT/2))

    def render(self, surface, score):
        surface.fill(constants.BLUE)
        nbr_round = self.font_content.render('Vous avez survécu à '+str(score)+ ' manche', True, constants.WHITE)
        if score >1:
            nbr_round = self.font_content.render('Vous avez survécu à '+str(score)+ ' manches', True, constants.WHITE)
        round_rect = nbr_round.get_rect()
        round_rect.center = (constants.SCREEN_WIDTH/2, (constants.SCREEN_HEIGHT/2)+30)
        surface.blit(nbr_round, round_rect)
        surface.blit(self.text_over, self.textRect_GA)
        surface.blit(self.text_try_again, self.textRect_TA)
        pygame.display.flip()