import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH


class Player(CircleShape):
    def _init_(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def triangle(self):
        self.rotation = 0
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

