import random

import pygame

from settings import *
from plant import RedPlant, RedPlant2


class FarmCell:
    def __init__(self, pos):
        self.image = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        self.image.fill((255, 186, 8))
        self.rect = self.image.get_rect(topleft=pos)

        self.can_click = True
        self.last_clicked = 0
        self.click_cooldown = 50

        self.plant = None

    def process_click(self):
        self.last_clicked = pygame.time.get_ticks()
        if self.can_click:
            if not self.plant:
                plants = [RedPlant((self.rect.x, self.rect.y - CELL_HEIGHT // 2)),
                          RedPlant2((self.rect.x, self.rect.y - CELL_HEIGHT // 2))]
                new_plant = random.choice(plants)
                self.add_plant(new_plant)
            else:
                if self.plant.stage == PLANT_MAX_STAGE - 1:
                    self.plant = None
            self.can_click = False

    def update(self, frame_time_ms):
        if self.plant:
            self.plant.update(frame_time_ms)
        if pygame.time.get_ticks() - self.last_clicked >= self.click_cooldown:
            self.can_click = True

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.plant:
            self.plant.draw(surface)

    def add_plant(self, plant):
        self.plant = plant
