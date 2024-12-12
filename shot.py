import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color=(255,255,255), center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt