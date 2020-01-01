import pygame, sys, os
from Classes.Settings import *
from Classes.Pointer import *
from Classes.Camera import *
from Classes.Block import *
from Classes.Tools import *
from Classes.UI.Button import *


pygame.init()

window = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT))
mapEditorSurface = pygame.Surface((DRAW_WIDTH, DRAW_HEIGHT))

POINTER = Pointer()

buttons = [
    Button(x=600, y=000, text="P", func=lambda :Tools.ChangeTool(Tools, "Paint")),
    Button(x=600, y=100, text="E", func=lambda :Tools.ChangeTool(Tools, "Earse"))
]


matrix = []
x, y, step = 0, 0, 32

for i in range(COUNT_HEIGHT):
    for j in range(COUNT_WIDTH):
        matrix.append(EmptyBlock(x, y))
        x += step
    y += step
    x = 0


pallete = []
x, y, step = 0, DRAW_HEIGHT, 50

pallete_names = [i.rsplit(".", 1)[0] for i in os.listdir(f"{os.getcwd()}\\Images\\Blocks\\World_1")]
count = 0

for i in range(2):
    for j in range(12):
        pallete.append(TileBlock(x, y, name=pallete_names[count] if count < len(pallete_names) else "EmptyBlock"))
        count += 1
        x += step
    y += step
    x = 0


def GenrateLevel(matrix):
    map = []

    line = ""
    count = 0
    for block in matrix:
        if (count < COUNT_WIDTH - 1):
            line += block.name if (block.name != "EmptyBlock") else " "
            count += 1
        else:
            line += "|"
            map.append(line)
            line = ""
            count = 0

    print(map)



CAMERA = Camera(camera_configure, TOTAL_WIDTH, TOTAL_HEIGHT)

pygame.display.set_caption("Platformer Editor")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_F5):
                GenrateLevel(matrix)

    mapEditorSurface.fill(BACKGROUND_COLOR)

    POINTER.Move(pygame.key.get_pressed())
    POINTER.Update(mapEditorSurface)
    CAMERA.update(POINTER)

    for block in matrix:
        block.Update()
        CAMERA.apply(block)
        mapEditorSurface.blit(block.image, block.rectTwo)

    for button in buttons:
        button.Update(window)

    for tile in pallete:
        tile.Update()
        window.blit(tile.image, tile.rect)

    window.blit(mapEditorSurface, (0, 0))

    clock.tick(60)
    pygame.display.flip()

pygame.quit()