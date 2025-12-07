"""
__author__ = "Donal Melicio Moloney"
__copyright__ = "2018 2007, Simple Game"
__version__ = "1.0.0"
__maintainer__ = "Donal Melicio Moloney"
__email__ = "Moloneyda@msoe.edu"
__status__ = "Production"
__date__ = "12/7/18"
"""
import random
import sys
from enum import Enum
import arcade
from PyQt5.QtWidgets import QMessageBox, QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap

# Setting game screen size as constant
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SPRITE_SCALING = 0.3
NUMBER_ROBBERS = 3  # Todo: it's three for now but maybe allow user to change it once GUI is made better


# Enums that define the two directions the robbers can go in
class Direction(Enum):
    LEFT = 0
    RIGHT = 1


# Class that represents a robber and his abilities
class Robber(arcade.Sprite):
    """
    Represents a robber sprite that moves back and forth.
    """
    ROBBER_SPEED = 3
    CURRENT_DIRECTION = Direction.LEFT

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = self.ROBBER_SPEED * -1

    # Method allowing the robber to move left
    def move_right(self):
        self.center_x += self.change_x
        if (
                self.center_x + self.ROBBER_SPEED) >= SCREEN_WIDTH:  # Switch to other direction if it hits right side boundary
            self.change_x *= -1
            self.CURRENT_DIRECTION = Direction.LEFT

    # Method allowing the robber to move right
    def move_left(self):
        self.center_x += self.change_x
        if 0 >= (self.center_x - self.ROBBER_SPEED):
            self.CURRENT_DIRECTION = Direction.RIGHT  # Switch to other direction if it hits the left side boundary
            self.change_x *= -1
        # Do nothing to change if in the correct bounds

    # Method that animates a robber character
    def animate(self):
        if self.CURRENT_DIRECTION == Direction.LEFT:
            self.move_left()
        elif self.CURRENT_DIRECTION == Direction.RIGHT:
            self.move_right()


class Sheriff(arcade.Sprite):
    """
    Represents the sheriff sprite controlled by the player.
    """
    SHERIFF_SPEED = 6

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

    # Method allowing the sheriff to move right
    def move_right(self):
        if self.center_x + self.SHERIFF_SPEED <= SCREEN_WIDTH:
            self.center_x += self.SHERIFF_SPEED

    # Method allowing the sheriff to move left
    def move_left(self):
        if self.center_x - self.SHERIFF_SPEED >= 0:
            self.center_x -= self.SHERIFF_SPEED

    # Method allowing the sheriff to move up
    def move_up(self):
        if self.center_y + self.SHERIFF_SPEED <= SCREEN_HEIGHT:
            self.center_y += self.SHERIFF_SPEED

    # Method allowing the sheriff to move down
    def move_down(self):
        if self.center_y - self.SHERIFF_SPEED >= 0:
            self.center_y -= self.SHERIFF_SPEED


# This class represents the arcade window
class SimpleGame(arcade.Window):
    """
    Main game window class for Sheriff Jones Robber Roundup.
    Handles game logic, drawing, and user input.
    """

    # Initializes method calls the super constructor for arcade.Window
    def __init__(self, width, height, title):
        # Calling the parent's init method
        super().__init__(width, height, title)
        self.robber_sprites_list = None
        self.sheriff_sprite = None
        self.paused = False
        self.score = 0
        self.time_left = 60.0
        self.game_over = False

    def start_new_game(self):
        # Setting the background color
        arcade.set_background_color(arcade.color.DONKEY_BROWN)
        self.robber_sprites_list = arcade.SpriteList()
        self.score = 0
        self.time_left = 60.0
        self.game_over = False
        try:
            self.sheriff_sprite = Sheriff("./sprites/sheriff.png", SPRITE_SCALING)
            # Creating instance of robber class
            for i in range(NUMBER_ROBBERS):
                # create Robber instance
                robber_sprite = Robber("./sprites/robber.png", SPRITE_SCALING)

                # Position the sprite, ensuring no overlaps
                while True:
                    robber_sprite.center_x = random.randrange(SCREEN_WIDTH)
                    robber_sprite.center_y = 400 + random.randrange(400)
                    if not arcade.check_for_collision_with_list(robber_sprite, self.robber_sprites_list):
                        break

                # Add the robber sprite to the list of sprites
                self.robber_sprites_list.append(robber_sprite)
        except FileNotFoundError as e:
            print(f"Error: Missing sprite file - {e}")
            arcade.close_window()

    def on_draw(self):
        # Command that must be called before drawing can occur
        arcade.start_render()

        # Draw all the robbers in the list
        self.robber_sprites_list.draw()
        self.sheriff_sprite.draw()

        # Draw UI
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)
        arcade.draw_text(f"Time: {int(self.time_left)}", 10, SCREEN_HEIGHT - 60, arcade.color.WHITE, 20)

        if self.game_over:
            if len(self.robber_sprites_list) == 0:
                arcade.draw_text("YOU WIN!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.GREEN, 50, anchor_x="center")
            else:
                arcade.draw_text("TIME UP! YOU LOSE!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 50, anchor_x="center")
            arcade.draw_text("Press R to Restart", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60, arcade.color.WHITE, 30, anchor_x="center")
        elif self.paused:
            arcade.draw_text("PAUSED", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, 50, anchor_x="center")
        else:
            self.animate(1/60)  # Approximate delta_time for now

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.sheriff_sprite.move_left()
        if key == arcade.key.RIGHT:
            self.sheriff_sprite.move_right()
        if key == arcade.key.UP:
            self.sheriff_sprite.move_up()
        if key == arcade.key.DOWN:
            self.sheriff_sprite.move_down()
        if key == arcade.key.P:
            self.paused = not self.paused
        if key == arcade.key.R and self.game_over:
            self.start_new_game()
        # todo implement this when implementing the sheriff

    def animate(self, delta_time):
        if self.game_over:
            return
        # Decrement time
        self.time_left -= delta_time
        if self.time_left <= 0:
            self.time_left = 0
            self.game_over = True
            return

        # Call update on all sprites
        self.robber_sprites_list.update()
        for robber in self.robber_sprites_list:
            robber.animate()

        # Check collisions
        robbers_to_remove = []
        for robber in self.robber_sprites_list:
            if arcade.check_for_collision(self.sheriff_sprite, robber):
                robbers_to_remove.append(robber)
                self.score += 10  # Points for catching

        # Remove collided robbers
        for robber in robbers_to_remove:
            self.robber_sprites_list.remove(robber)

        # Check win condition
        if len(self.robber_sprites_list) == 0:
            self.game_over = True


# Class that represents the gui that presents the options of either playing the game or not
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'EEEEEEEEEEEHhhhhhaaaaa Welcome to Sheriff Jones Robber Roundup'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button_reply = QMessageBox.question(self, 'Game Play Message',
                                            "Do you want to play Sheriff Jones Robber Roundup?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if button_reply == QMessageBox.Yes:
            ex = Menu()
        else:
            self.close()


# Class that shows the user the directions
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)
        label1 = QLabel(self)
        label2 = QLabel("Your Controls: \n Up Arrow: Move Sheriff upward \n Left Arrow: Move Sheriff downward \n"
                        " Right Arrow: Move Sheriff Right\n Down Arrow: Move Sheriff Left\n")
        button = QPushButton('Ok', self);
        button.resize(50, 32)
        button.move(350, 380)
        button.clicked.connect(self.clickMethod)
        # Setting the image of controls
        try:
            pixmap = QPixmap('./info/movement.png')
            pixmap = pixmap.scaledToWidth(400)
            label1.setPixmap(pixmap)
        except Exception as e:
            print(f"Error loading movement.png: {e}")
            label1.setText("Movement controls image not found.")
        self.setFixedSize(450, 580)
        lay.addWidget(label1)
        lay.addWidget(label2)
        self.show()
        app.exec_()

    def clickMethod(self):
        game_window = SimpleGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Simple Game")
        game_window.start_new_game()
        arcade.run()


# What starts the game
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
