import pygame
from Classes.Settings import *



class Pointer(pygame.sprite.Sprite):
    def __init__(self, position=(DRAW_WIDTH // 2, DRAW_HEIGHT // 2)):
        super().__init__()
        self.image = pygame.image.load(EDITOR_SPRITES["Pointer"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, POINTER_SIZE)

        self.rect = self.image.get_rect()
        self.rect.topleft = position[0], position[1]
        self.speed = POINTER_SPEED

        self.xvel = 0
        self.yvel = 0


    def Move(self, keys):
        if not (keys[pygame.K_d] or keys[pygame.K_a]):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not (keys[pygame.K_w] or keys[pygame.K_s]):  # стоим, когда нет указаний идти
            self.yvel = 0

        if (keys[pygame.K_d]):
            self.xvel = self.speed
        elif (keys[pygame.K_a]):
            self.xvel = -self.speed
        elif (keys[pygame.K_s]):
            self.yvel = self.speed
        elif (keys[pygame.K_w]):
            self.yvel = -self.speed

        if (self.rect.x < 0):
            self.rect.x = 0
        elif (self.rect.x > TOTAL_WIDTH):
            self.rect.x = TOTAL_WIDTH

        if (self.rect.y < 0):
            self.rect.y = 0
        elif (self.rect.y > TOTAL_HEIGHT):
            self.rect.y = TOTAL_HEIGHT

        self.rect.x += self.xvel
        self.rect.y += self.yvel


    def Update(self, window):
        window.blit(self.image, self.rect.topleft)
