from collections import deque
from config import *


class Planet:
    #Constants
    AU = 149.6e6 * 1000 #* Distance from the sun = 149.6 million km
    G = 6.67428e-11 #* Gravitational constant
    SCALE = 200 / AU #* One AU = 100 pixels 
    TIMESTEP = 3600*24 #* One day

    def __init__(self, x: float, y: float, radius: int, color: str, mass: float, sun: bool = False) -> None:
        """
        Initialize a Planet object.

        Parameters:
        - x (float): The x-coordinate of the planet's position.
        - y (float): The y-coordinate of the planet's position.
        - radius (int): The radius of the planet.
        - color (tuple): The color of the planet.
        - mass (float): The mass of the planet.
        - sun (bool): Whether the planet is a sun or not. Defaults to False.

        Returns:
        None
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = sun
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

        self.orbit = deque(maxlen=MAX_ORBIT_LENGTH)

    def draw(self, win):
        """
        Draw the planet on the given window surface.

        Parameters:
            win (pygame.Surface): The window surface on which to draw the planet.

        Returns:
            None
        """
        x = self.x * self.SCALE + WIDTH / 2 #* To center the planet
        y = self.y * self.SCALE + HEIGHT / 2 #* To center the planet

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)
        if not self.sun:
            self.render_distance_text(win, x, y)

    def render_distance_text(self, win, x, y):
        distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, DARK_GREY)
        win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
    
    def calculate_force(self, planet) -> tuple[float, float]:
        """
        Calculate the force exerted on this planet by another planet.

        Parameters:
            planet (Planet): The other planet.

        Returns:
            Tuple[float, float]: The x and y components of the force.
        """
        distance_x = planet.x - self.x
        distance_y = planet.y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        force = self.G * self.mass * planet.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets) -> None:
        """
        Update the position of the planet based on the forces exerted by other planets.

        Parameters:
            - planets (list): A list of Planet objects representing all the planets in the system.

        Returns:
            None
        """
        px, py = 0, 0
        for planet in planets:
            if self is planet:
                continue
            force_x, force_y = self.calculate_force(planet)
            px += force_x 
            py += force_y

        self.x_vel += px / self.mass * self.TIMESTEP
        self.y_vel += py / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
