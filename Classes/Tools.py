import pygame


class Tools:
    selectedTool = "Paint"
    tools = ["Paint", "Earse"]

    class Paint:
        imageName = "1"

    class Earse:
        imageName = "EmptyBlock"

    def ChangeTool(self, tool):
        if (tool in self.tools):
            self.selectedTool = tool
