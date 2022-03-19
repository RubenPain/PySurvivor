import pygame as pg

class Sound:
    def play(self):
        pg.mixer.music.load('assets/sounds/WorldCrisis.mp3')
        pg.mixer.music.play()


    def pause(self):
        pg.mixer.music.pause()


    def unpause(self):
        pg.mixer.music.unpause()


    def sound(self, sound_effect):
        pg.mixer.Sound.play(pg.mixer.Sound(f'assets/sounds/{sound_effect}'))