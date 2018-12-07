"""
__author__ = "Donal Melicio Moloney"
__copyright__ = "2018 2007, Simple Game"
__version__ = "1.0.0"
__maintainer__ = "Donal Melicio Moloney"
__email__ = "Moloneyda@msoe.edu"
__status__ = "Production"
__date__ = "12/7/18"
"""

import arcade

# Setting game screen size as constant
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


class SimpleGame(arcade.Window):

    def __init__(self, width, height, title):
        # Calling the parent's init method
        super().__init__(width, height, title)
        # Setting the background color
        arcade.set_background_color(arcade.color.BLUE_GRAY)

    def on_draw(self):
        arcade.start_render()


def main():
    game_window = SimpleGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Simple Game")
    arcade.run()


if __name__ == "__main__":
    main()
