import pygame
from Classes.Settings import *
from Classes.Tools import *


class EmptyBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, name="EmptyBlock"):
        super().__init__()
        self.image = pygame.image.load(EDITOR_SPRITES[name])
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.rectTwo = self.image.get_rect()
        self.rectTwo.y = y
        self.rectTwo.x = x

        self.name = name

        self.lastPointer = 0


    def Update(self):
        #  and self.lastPointer == 1)
        if (self.OnButton() and bool(pygame.mouse.get_pressed()[0] == 1)):
            if (Tools.selectedTool == "Paint"):
                self.image = pygame.image.load(LEVEL_GENERATOR_SPRITES[WORLD_TYPE][Tools.Paint.imageName])
                self.name = Tools.Paint.imageName
                self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
            elif (Tools.selectedTool == "Earse"):
                self.image = pygame.image.load(EDITOR_SPRITES[Tools.Earse.imageName])
                self.name = "EmptyBlock"
                self.image = pygame.transform.scale(self.image, BLOCK_SIZE)

        self.lastPointer = pygame.mouse.get_pressed()[0]


    def OnButton(self):
        pos = pygame.mouse.get_pos()
        return self.rectTwo.x <= pos[0] and self.rectTwo.x + self.rectTwo.width > pos[0] and self.rectTwo.y <= pos[1] and self.rectTwo.y + self.rectTwo.height > pos[1]



class TileBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, name="EmptyBlock"):
        super().__init__()
        self.name = name

        if (name in EDITOR_SPRITES.keys()):
            self.image = pygame.image.load(EDITOR_SPRITES[name])
        else:
            self.image = pygame.image.load(LEVEL_GENERATOR_SPRITES[WORLD_TYPE][name])
        self.image = pygame.transform.scale(self.image, TILE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.lastPointer = 0


    def Update(self):
        if (self.OnButton() and bool(pygame.mouse.get_pressed()[0] == 0 and self.lastPointer == 1)):
            if (self.name != "EmptyBlock"): Tools.Paint.imageName = self.name

        self.lastPointer = pygame.mouse.get_pressed()[0]


    def OnButton(self):
        pos = pygame.mouse.get_pos()
        return self.rect.x <= pos[0] and self.rect.x + self.rect.width > pos[0] and self.rect.y <= pos[1] and self.rect.y + self.rect.height > pos[1]