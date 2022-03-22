import pygame

import os
import random

from settings import *
from utility import *


class Plant:
    def __init__(self):

        # graphics
        self.image = None
        self.rect = None

        # main logic
        self.stage = 0
        self.plant_time = 0
        self.grow_time = 2000 + (random.random()-0.5) * 1000  # in ms

    def update(self, frame_time_ms):
        self.plant_time += frame_time_ms
        if self.plant_time >= self.grow_time and self.stage < PLANT_MAX_STAGE - 1:
            self.plant_time = 0
            self.stage += 1
            self.image = self.images[self.stage]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _import_graphics(self, plant_name, scale=8):
        self.images = []
        path, _, image_names = list(os.walk(f'graphics/{plant_name}/'))[0]
        for image_name in image_names[:-1]:
            image = pygame.image.load(path + image_name).convert_alpha()
            image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
            if random.random() > 0.5:
                image = pygame.transform.flip(image, True, False)

            shift = random.randint(0, 2)
            for i in range(image.get_width()):
                for j in range(image.get_height()):
                    image.set_at((i, j), change_color(image.get_at((i, j)), shift))

            image.set_colorkey('white')
            self.images.append(image)


class RedPlant(Plant):
    def __init__(self, pos):
        super().__init__()
        self._import_graphics('plant1')
        # self.images = [pygame.image.load('./graphics/plant1/1.png').convert_alpha(),
        #                pygame.image.load('./graphics/plant1/2.png').convert_alpha()]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)

        self.grow_time = 3000 + (random.random()-0.5) * 1000  # in ms
        self.price = 10


class RedPlant2(Plant):
    def __init__(self, pos):
        super().__init__()
        self._import_graphics('plant2')
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)

        self.grow_time = 5000 + (random.random()-0.5) * 1000  # in ms
        self.price = 50
