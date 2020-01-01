import pygame, math
from Classes.Settings import *


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        target.rectTwo = target.rect.move(self.state.topleft)
        # return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)



def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + DRAW_WIDTH / 2, -t + DRAW_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - DRAW_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - DRAW_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)