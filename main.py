import pygame
from pygame.locals import *

import sys

from plant import RedPlant
from settings import *
from scene import Scene


class Game:
    def __init__(self):
        pygame.display.set_caption("Farm")
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.scene = Scene()

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(FPS)
            frame_time_s = frame_time_ms / 1000.

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()

            self.scene.update(frame_time_ms)

            self.display_surface.fill((19, 111, 99))
            self.scene.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def stop(self):
        self.is_running = False


if __name__ == '__main__':
    Game().run()
