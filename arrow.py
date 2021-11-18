import pygame
from pygame.sprite import Sprite

from traffic_light_controller import State


class BaseArrow(Sprite):
    def __init__(self, x, y, frames, stateMap: dict[State, int], frame=0):
        super().__init__()
        self.frames = frames
        self.currentFrame = 0
        self.stateMap = stateMap

        self.currentFrame = frame
        self.image = self.frames[frame]
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.scale(0.5)

    def update(self):
        self.image = self.frames[self.currentFrame]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def changeState(self, state: State):
        self.currentFrame = self.stateMap[state]

    def rotate(self, angle: int):
        for i, image in enumerate(self.frames):
            loc = image.get_rect().center
            rotated_img = pygame.transform.rotate(image, angle)
            rotated_img.get_rect().center = loc
            self.frames[i] = rotated_img
        self.update()

    def scale(self, scale):
        for i, image in enumerate(self.frames):
            loc = image.get_rect().center
            scaled_img = pygame.transform.scale(
                image, (self.rect.w * scale,
                        self.rect.h * scale)
            )
            scaled_img.get_rect().center = loc
            self.frames[i] = scaled_img
        self.update()


class StraightArrow(BaseArrow):
    def __init__(self, x, y, stateMap: dict[State, int], frame=0):
        frames = [
            pygame.image.load("assets/red-straight.png").convert_alpha(),
            pygame.image.load("assets/yellow-straight.png").convert_alpha(),
            pygame.image.load("assets/green-straight.png").convert_alpha()
        ]

        super().__init__(x, y, frames, stateMap, frame)


class CurvedArrow(BaseArrow):
    def __init__(self, x, y, stateMap: dict[State, int], frame=0):
        frames = [
            pygame.image.load("assets/red-curve.png").convert_alpha(),
            pygame.image.load("assets/yellow-curve.png").convert_alpha(),
            pygame.image.load("assets/green-curve.png").convert_alpha()
        ]

        super().__init__(x, y, frames, stateMap, frame)
