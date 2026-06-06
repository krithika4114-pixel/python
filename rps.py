import random
import pygame


class botton():

    def __init__(self, x, y, position, width, hight):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.position = position


        def clicked(self, pos):

            self.pos = pygame.mouse.get_pos()

            if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
                if self.pos[1] > self.y and self.pos[1] < self.y + self.hight:
                    return True
                
            return False


class RpsGame
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set.mode((960, 640))