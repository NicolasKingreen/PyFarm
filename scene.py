import pygame

from settings import *
from farm_cell import FarmCell
from plant import RedPlant


class Scene:
    def __init__(self):
        self.farm_cells = []

        padding = 10
        margin = 50
        for i in range(4):
            for j in range(6):
                self.farm_cells.append(FarmCell(((CELL_WIDTH + padding) * i + margin, (CELL_HEIGHT + padding) * j + margin)))

    def process_clicks(self):
        mouse_pos = pygame.mouse.get_pos()
        mbuttons = pygame.mouse.get_pressed()

        if mbuttons[0]:
            for farm_cell in self.farm_cells:
                if farm_cell.rect.collidepoint(mouse_pos):
                    farm_cell.process_click()

    def update(self, frame_time_ms):
        self.process_clicks()

        for farm_cell in self.farm_cells:
            farm_cell.update(frame_time_ms)
            
    def draw(self, surface):
        for farm_cell in self.farm_cells:
            farm_cell.draw(surface)

