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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


# Setting game screen size as constant
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SPRITE_SCALING = 0.3


# Todo abstract these classes into a character class
class Direction(Enum):
    LEFT = 0
    RIGHT = 1


class Robber(arcade.Sprite):
    ROBBER_SPEED = 50
    CURRENT_DIRECTION = Direction.LEFT

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = self.ROBBER_SPEED

    def move_left(self):
        if (self.center_x + self.ROBBER_SPEED) >= SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
            self.CURRENT_DIRECTION = Direction.RIGHT  # Switch to other direction once you have hit the boundary
        else:
            self.center_x = self.center_x + self.ROBBER_SPEED

    def move_right(self):
        if 0 >= (self.center_x - self.ROBBER_SPEED):
            self.center_x = SCREEN_WIDTH
            self.CURRENT_DIRECTION = Direction.LEFT  # Switch to other direction once you have hit the boundary
        else:
            self.center_x = self.center_x - self.ROBBER_SPEED

    def update(self):
        print("UPDATE ENTERED")
        if self.CURRENT_DIRECTION == Direction.LEFT:
            self.move_left()
        elif self.CURRENT_DIRECTION == Direction.RIGHT:
            self.move_right()


class SimpleGame(arcade.Window):

    def __init__(self, width, height, title):
        # Calling the parent's init method
        super().__init__(width, height, title)
        self.robber_sprites_list = None

    def start_new_game(self):
        # Setting the background color
        arcade.set_background_color(arcade.color.DONKEY_BROWN)
        self.robber_sprites_list = arcade.SpriteList()
        # Creating instance of robber class
        for i in range(3):
            # create Robber instance
            robber_sprite = Robber("./sprites/robber.png", SPRITE_SCALING)

            # Position the sprite
            robber_sprite.center_x = random.randrange(SCREEN_WIDTH)
            robber_sprite.center_y = 400 + random.randrange(400)  # TODO comment this

            # Add the robber sprite to the list of sprites
            self.robber_sprites_list.append(robber_sprite)
            self.robber_sprites_list.update_animation(2)

    def on_draw(self):
        # Command that must be called before drawing can occur
        arcade.start_render()

        # Draw all the robbers in the list
        self.robber_sprites_list.draw()

    def on_key_press(self, key, modifiers):
        pass
        # todo implement this when implementing the sheriff

    def animate(self, delta_time):
        # Call update on all sprites (The sprites don't do much in this #
        print("Entererd")
        self.robber_sprites_list.update()


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
            game_window = SimpleGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Simple Game")
            game_window.start_new_game()
            arcade.run()
        else:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
