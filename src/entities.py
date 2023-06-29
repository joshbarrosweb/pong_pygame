# Import the Pygame library
import pygame

# Define an Entity class that extends the Pygame Rect class
class Entity(pygame.Rect):
    # Initialize the Entity class with x, y coordinates and width, height dimensions
    def __init__(self, x, y, width, height):
        # Call the super class's __init__ method with the passed parameters
        super().__init__(x, y, width, height)

# Define a Ball class that extends the Entity class
class Ball(Entity):
    # Initialize the Ball class with x, y coordinates and width, height dimensions
    def __init__(self, x, y, width, height):
        # Call the super class's __init__ method with the passed parameters
        super().__init__(x, y, width, height)

# Define a Player class that extends the Entity class
class Player(Entity):
    # Initialize the Player class with x, y coordinates and width, height dimensions
    def __init__(self, x, y, width, height):
        # Call the super class's __init__ method with the passed parameters
        super().__init__(x, y, width, height)

# Define an Opponent class that extends the Entity class
class Opponent(Entity):
    # Initialize the Opponent class with x, y coordinates and width, height dimensions
    def __init__(self, x, y, width, height):
        # Call the super class's __init__ method with the passed parameters
        super().__init__(x, y, width, height)
