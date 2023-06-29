# Pong Game

This project is a Pong game clone implemented in Python using the Pygame library. The gameplay involves controlling a paddle to prevent a ball from hitting the edge of the screen.

# Special Thanks

This project was inspired by the classic arcade game, Pong.

# Project Structure

The project has the following file and folder structure:

## src

### This folder contains the source code files for the game:

* `main.py`: The main entry point of the game. It controls the game loop, handles events, and manages the rendering and updating of game objects.
* `entities.py`: This file defines the Entity, Ball, Player, and Opponent classes, which are used to represent the different objects in the game.
* `game.py`: This file contains the Game class that represents the entire Pong game. It handles the game's logic, including ball and player movement, score tracking, and screen rendering.
* `settings.py`: This file defines the game's settings and constants.

# Classes

## src/main.py

This file is the main entry point of the game.

## src/entities.py

This file defines the Entity, Ball, Player, and Opponent classes.

* `Entity`: A base class for game objects, extending the Pygame Rect class.
* `Ball`: Represents the ball in the game.
* `Player`: Represents the player-controlled paddle.
* `Opponent`: Represents the AI-controlled paddle.

## src/game.py

This file contains the Game class.

* `Game`: This class represents the Pong game. It handles the game's logic, including ball and player movement, score tracking, and screen rendering. It also loads the game assets like images and sounds.

## src/settings.py

While this file does not contain any classes, it defines the game's settings and constants which are used by the Game class. For example, it includes settings like the screen resolution, frame rate, and various game parameters.

# Instructions

To run the project, follow these steps:

1. Install Python 3 if you haven't already.
2. Install the Pygame library by running the command: `pip install pygame`.
3. Navigate to the project's src directory.
4. Run the command: `python3 src/main.py`.

Feel free to modify and explore the game to suit your needs.

Enjoy playing!
