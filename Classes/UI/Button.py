import pygame, os
from Classes.Settings import *


class Button(object):
    def __init__(self, x=0, y=0, w=100, h=100, musicSound="B_Click", spriteName=None, name=None, text="Text", fontSize=20, color=(255, 0, 0), onColor=(200, 0, 0), pressColor=(150, 0, 0), func=None):
        self.normalColor = color
        self.onColor = onColor
        self.pressColor = pressColor

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name

        self.font = pygame.font.Font(None, fontSize)
        self.lastPointer = 0


        self.image = None
        if (spriteName):
            if (spriteName in EDITOR_SPRITES.keys()):
                self.image = pygame.image.load(EDITOR_SPRITES[spriteName])
                self.image = pygame.transform.scale(self.image, (w, h))
                self.image = self.image.convert_alpha()

                self.normalImage = self.image.copy()
                self.onImage = self.image.copy()
                self.pressImage = self.image.copy()

                self.normalImage.fill(self.normalColor, None, pygame.BLEND_RGBA_MULT)
                self.onImage.fill(self.onColor, None, pygame.BLEND_RGBA_MULT)
                self.pressImage.fill(self.pressColor, None, pygame.BLEND_RGBA_MULT)

        self.text = text
        self.event = func

    def Update(self, screen):
        bg = (255, 255, 255)

        if (self.image):
            if (not self.OnButton()):
                screen.blit(self.normalImage, (self.x, self.y))
            elif (self.OnButton() and bool(pygame.mouse.get_pressed()[0] == 0 and self.lastPointer == 1)):
                screen.blit(self.pressImage, (self.x, self.y))
                if (self.event): self.event()
            else:
                screen.blit(self.onImage, (self.x, self.y))
        else:
            if (not self.OnButton()):
                bg = self.normalColor
            elif (self.OnButton() and bool(pygame.mouse.get_pressed()[0] == 0 and self.lastPointer == 1)):
                bg = self.pressColor
                if (self.event): self.event()
            else:
                bg = self.onColor

        surf = self.font.render(self.text, True, (0, 0, 0), bg if not self.image else self.image)
        rect = (self.x, self.y, self.w, self.h)
        xo = self.x + (self.w - surf.get_width()) // 2
        yo = self.y + (self.h - surf.get_height()) // 2
        if (not self.image): screen.fill(bg, rect)
        screen.blit(surf, (xo, yo))

        self.lastPointer = pygame.mouse.get_pressed()[0]

    def OnButton(self):
        pos = pygame.mouse.get_pos()
        return self.x <= pos[0] and self.x + self.w > pos[0] and self.y <= pos[1] and self.y + self.h > pos[1]

