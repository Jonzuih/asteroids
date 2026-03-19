import pygame
from circleshape import CircleShape
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)        
        self.radius = radius

    


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)


    def update(self, dt):
        self.position += (self.velocity * dt)

