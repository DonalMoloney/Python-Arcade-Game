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
SCREEN_HEIGHT = 800


class Robber:
    robber = None

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.sprite_scale = .3
        self.robber_image = "sprites/robber.png"
        self.robber_sprite = arcade.Sprite(self.robber_image, self.sprite_scale)

    def draw(self):
        self.robber_sprite.draw()

    def animate(self):
        pass

    def get_scaling(self):
        return 1

    def get_robber_image(self):
        return "sprites/robber.png"


class SimpleGame(arcade.Window):

    def __init__(self, width, height, title):
        # Calling the parent's init method
        super().__init__(width, height, title)
        # Setting the background color
        arcade.set_background_color(arcade.color.DONKEY_BROWN)
        self.robber_list = arcade.SpriteList()
        self.robber = Robber(300, 300)

    def on_draw(self):
        arcade.start_render()
        self.robber.draw()

def main():
    game_window = SimpleGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Simple Game")
    arcade.run()


if __name__ == "__main__":
    main()
