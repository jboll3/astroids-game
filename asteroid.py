import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            random_angle = pygame.math.Vector2.rotate(self.velocity, angle)
            neg_random_angle = pygame.math.Vector2.rotate(self.velocity, angle*-1)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
            asteroid_1.velocity=random_angle*1.2
            asteroid_2.velocity=neg_random_angle*1.2
