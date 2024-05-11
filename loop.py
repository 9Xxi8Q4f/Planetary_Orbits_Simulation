#Inspired from https://fiftyexamples.readthedocs.io/en/latest/gravity.html

import math
import pygame
from celestial_body import *
import time

def load_planets_from_config():
    # Load planets' properties from a configuration file or a database
    # Return a dictionary of Planet objects
    return {
        'sun': Planet(0, 0, 30, YELLOW, 1.98892 * 10**30, sun=True),
        'earth': Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24),
        'mars': Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23),
        'venus': Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24),
        'mercury': Planet(0.387 * Planet.AU, 0, 8, YELLOW, 3.30 * 10**23)
    }

def set_y_velocities(planets, y_vels):
    """
    Set the y velocities of the planets in the given dictionary of Planet objects.

    Parameters:
        - planets (dict): A dictionary of Planet objects representing the planets in the system.
        - y_vels (dict): A dictionary of y velocities to set for each planet. The keys should be the same as the planet names in the planets dictionary.

    Returns:
        None
    """
    for planet_name, y_vel in y_vels.items():
        planets[planet_name].y_vel = y_vel

def main():
    """
    The main function that runs the game loop.

    This function initializes the game loop and runs it until the user quits the game. It loads the planets from a configuration file, sets their initial y velocities, and then enters the game loop.

    The game loop updates the positions of the planets based on their velocities and gravitational forces, and then draws the planets on the screen. It also handles user input events, such as closing the game window.

    Parameters:
    None

    Returns:
    None
    """

    run = True
    clock = pygame.time.Clock() #FPS
    FPS = 60

    planets = load_planets_from_config()

    set_y_velocities(planets, y_vels)


    while run:
        clock.tick(FPS)

        #Draw here
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets.values():
            planet.update_position(list(planets.values()))
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    time.sleep(5)
    main()
