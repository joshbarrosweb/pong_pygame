import pygame, sys, random
from settings import *
from entities import Ball, Player, Opponent

# Main Game class
class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512) # Initialize the mixer module with specific parameters
        pygame.init() # Initialize all imported pygame modules
        self.clock = pygame.time.Clock() # Create a pygame clock object to track time

        # Create the game display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pong Clone') # Set the caption for the game window

        # Create game entities (ball, player, opponent)
        self.ball = Ball(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30)
        self.player = Player(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10, 140)
        self.opponent = Opponent(10, SCREEN_HEIGHT / 2 - 70, 10, 140)

        # Set up colors
        self.bg_color = pygame.Color('grey12')
        self.light_grey = (200, 200, 200)

        # Set up initial speeds and scores
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.player_speed = 0
        self.opponent_speed = 7
        self.player_score = 0
        self.opponent_score = 0

        # Set up game font
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)

        # Score time for displaying countdown when scoring
        self.score_time = None

    def ball_movement(self):
        # Update ball position
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        # Check for collision with screen boundaries and update scores
        if self.ball.top <= 0 or self.ball.bottom >= SCREEN_HEIGHT:
          self.ball_speed_y *= -1

        # Player scores
        if self.ball.left <= 0:
          self.player_score += 1
          self.score_time = pygame.time.get_ticks()

        # Opponent scores
        if self.ball.right >= SCREEN_WIDTH:
          self.opponent_score += 1
          self.score_time = pygame.time.get_ticks()

        # Check for collision with player and opponent
        if self.ball.colliderect(self.player) and self.ball_speed_x > 0:
          if abs(self.ball.right - self.player.left) < 10:
            self.ball_speed_x *= -1
          elif abs(self.ball.bottom - self.player.top) < 10 and self.ball_speed_y > 0:
            self.ball_speed_y *= -1
          elif abs(self.ball.top - self.player.bottom) < 10 and self.ball_speed_y < 0:
            self.ball_speed_y *= -1

        if self.ball.colliderect(self.opponent) and self.ball_speed_x < 0:
          if abs(self.ball.left - self.opponent.right) < 10:
            self.ball_speed_x *= -1
          elif abs(self.ball.bottom - self.opponent.top) < 10 and self.ball_speed_y > 0:
            self.ball_speed_y *= -1
          elif abs(self.ball.top - self.opponent.bottom) < 10 and self.ball_speed_y < 0:
            self.ball_speed_y *= -1

    def ball_restart(self):
      # Reset the ball to the center after a player scores
      self.current_time = pygame.time.get_ticks()
      self.ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

      # Show countdown before starting the game after scoring
      if self.current_time - self.score_time < 700:
        self.number_three = self.game_font.render("3", False, self.light_grey)
        self.screen.blit(self.number_three, (SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 8 + 20))

      if 700 < self.current_time - self.score_time < 1400:
        self.number_two = self.game_font.render("2", False, self.light_grey)
        self.screen.blit(self.number_two, (SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 8 + 20))

      if 1400 < self.current_time - self.score_time < 2100:
        self.number_one = self.game_font.render("1", False, self.light_grey)
        self.screen.blit(self.number_one, (SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 8 + 20))

      if self.current_time - self.score_time < 2100:
        self.ball_speed_x, self.ball_speed_y = 0, 0
      else:
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.score_time = None

    def player_movement(self):
      # Prevent the player from moving out of screen
      if self.player.top <= 0:
        self.player.top = 0
      if self.player.bottom >= SCREEN_HEIGHT:
        self.player.bottom = SCREEN_HEIGHT

    def opponent_movement(self):
      # Make the opponent follow the ball
      if self.opponent.top < self.ball.y:
        self.opponent.top += self.opponent_speed
      if self.opponent.bottom > self.ball.y:
        self.opponent.bottom -= self.opponent_speed

      # Prevent the opponent from moving out of screen
      if self.opponent.top <= 0:
        self.opponent.top = 0
      if self.opponent.bottom >= SCREEN_HEIGHT:
        self.opponent.bottom = SCREEN_HEIGHT

    def run(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Player movement
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_DOWN:
                    self.player_speed += 7
                  if event.key == pygame.K_UP:
                    self.player_speed -= 7

                if event.type == pygame.KEYUP:
                  if event.key == pygame.K_DOWN:
                    self.player_speed -= 7
                  if event.key == pygame.K_UP:
                    self.player_speed += 7

            # Call game function each loop
            self.ball_movement()
            self.player_movement()
            self.opponent_movement()

            self.player.y += self.player_speed

            # Draw everything on the screen
            self.screen.fill(self.bg_color)
            pygame.draw.rect(self.screen, self.light_grey, self.player)
            pygame.draw.rect(self.screen, self.light_grey, self.opponent)
            pygame.draw.ellipse(self.screen, self.light_grey, self.ball)
            pygame.draw.aaline(self.screen, self.light_grey, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

            if self.score_time:
              self.ball_restart()

            # Render scores
            self.player_text = self.game_font.render(f"{self.player_score}", False, self.light_grey)
            self.screen.blit(self.player_text, (660, 470))

            self.opponent_text = self.game_font.render(f"{self.opponent_score}", False, self.light_grey)
            self.screen.blit(self.opponent_text, (600, 470))

            # Update the full display Surface to the screen
            pygame.display.flip()

            # Limit the game speed to 60 frames per second
            self.clock.tick(FPS)
