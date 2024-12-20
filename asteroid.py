import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            pygame.Color("white"),
            self.position,
            self.radius,
            2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid1_velo = self.velocity.rotate(angle)
        asteroid2_velo = self.velocity.rotate(-angle)
        r = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, r)
        asteroid2 = Asteroid(self.position.x, self.position.y, r)
        asteroid1.velocity = asteroid1_velo * 1.2
        asteroid2.velocity = asteroid2_velo * 1.2
