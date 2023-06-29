# Import the Game class from the game module
from game import Game

# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    # Create an instance of the Game class
    game = Game()
    # Run the game
    game.run()
