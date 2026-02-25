import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            angle = random.uniform(20, 50)

            pos_vector = self.velocity.rotate(angle)
            neg_vector = self.velocity.rotate(-angle)

            NEW_RADIUS = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, NEW_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, NEW_RADIUS)

            asteroid1.velocity = self.velocity + pos_vector * 1.2
            asteroid2.velocity = self.velocity + neg_vector * 1.2