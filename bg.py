import pygame
import random
pygame.init()

def ra():
        return random.randint(0, 600)

class Background:
    def __init__(self, window, img):
        self.window = window
        self.img = img
        self.lemon = pygame.transform.scale(pygame.image.load(self.img).convert_alpha(), (25, 20))
        self.slow_lemons = [[ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0]]
        self.medium_lemons = [[ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0]]
        self.fast_lemons = [[ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0], [ra(), 0]]
    def slow(self):
        for lemon in self.slow_lemons:
            self.window.blit(pygame.transform.scale(self.lemon, (25, 20)), tuple(lemon))
            lemon[1] += 2
            lemon[0] += 1
            if lemon[1] > 450:
                lemon[1] = 0
            if lemon[0] > 600:
                lemon[0] = 0
    def medium(self):
        for lemon in self.medium_lemons:
            self.window.blit(pygame.transform.scale(self.lemon, (25, 20)), tuple(lemon))
            lemon[1] += 4
            lemon[0] += 1
            if lemon[1] > 450:
                lemon[1] = 0
            if lemon[0] > 600:
                lemon[0] = 0
    def fast(self):
        for lemon in self.fast_lemons:
            self.window.blit(pygame.transform.scale(self.lemon, (25, 20)), tuple(lemon))
            lemon[1] += 6
            lemon[0] += 1
            if lemon[1] > 450:
                lemon[1] = 0
            if lemon[0] > 600:
                lemon[0] = 0
    def update(self):
        self.slow()
        self.medium()
        self.fast()