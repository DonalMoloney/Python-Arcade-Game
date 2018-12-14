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

import arcade
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# Setting game screen size as constant
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800


# Todo abstract these classes into a character class
class Sheriff:

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.sprite_scale = .3
        self.sheriff_image = "sprites/sheriff.png"
        self.sheriff_sprite = arcade.Sprite(self.sheriff_image, self.sprite_scale)

    def draw(self):
        self.robber_sprite.draw()

    def animate(self):
        pass

    def get_scaling(self):
        return 1

    def get_sheriff_image(self):
        return "sprites/sheriff.png"


class Robber:

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.sprite_scale = .3
        self.robber_image = "sprites/robber.png"
        self.robber_sprite = arcade.Sprite(self.robber_image, self.sprite_scale)

    def draw(self):
        self.robber_sprite.draw()

    def get_direction(number):
        # Todo add other directions
        if number == 0:
            return "down"
        else:
            return "up"

    def animate(self):
        self.move_sprite(self.get_direction(random.randint(0, 1)))

    def get_scaling(self):
        return 1

    def get_robber_image(self):
        return "sprites/robber.png"

    def move_sprite(self, param):
        if (param == "left") and (self.position_x != SCREEN_WIDTH):
            self.position_x = self.position_x - 3
        else:
            self.position_x = self.position_x + 1


class SimpleGame(arcade.Window):

    def __init__(self, width, height, title):
        # Calling the parent's init method
        super().__init__(width, height, title)
        # Setting the background color
        arcade.set_background_color(arcade.color.DONKEY_BROWN)
        self.robber_list = arcade.SpriteList()
        self.robber = Robber(300, 300)
        self.sheriff = Sheriff(300, 300)

    def on_draw(self):
        arcade.start_render()
        self.robber.draw()
       # self.sheriff.draw()

    def on_key_press(self, key, modifiers):
        pass
        # todo


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
        buttonReply = QMessageBox.question(self, 'Game Play Message',
                                           "Do you want to play Sheriff Jones Robber Roundup?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            game_window = SimpleGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Simple Game")
            arcade.run()
        else:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
