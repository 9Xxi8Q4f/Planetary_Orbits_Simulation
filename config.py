import pygame
import math
pygame.init()

MAX_ORBIT_LENGTH = 1000
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 150)

FONT = pygame.font.SysFont("comicsans", 30)


y_vels = {
    'earth': 29.783 * 1000,
    'mars': -24.077 * 1000,
    'venus': -35.02 * 1000,
    'mercury': -47.4 * 1000
}

