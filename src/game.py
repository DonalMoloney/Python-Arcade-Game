import arcade


def draw_ground(SCREEN_WIDTH,  GROUND_HEIGHT, X_CORD_ORIGIN):
    """
    This method draws the ground onto the game
    :param SCREEN_WIDTH: The width of the screen to ensure that ground takes up the whole space
    :param GROUND_HEIGHT: The height the ground will be
    :param X_CORD_ORIGIN: The location on the x-axis drawing will start from for both with and height
    :return: Nothing is returned from this method
    """
    arcade.draw_lrtb_rectangle_filled(X_CORD_ORIGIN, SCREEN_WIDTH, GROUND_HEIGHT, X_CORD_ORIGIN,
                                      arcade.color.GREEN_YELLOW)


# Set the size of the game screen as constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
GROUND_HEIGHT = 85
X_CORD_ORIGIN = 0

# Setting dimensions of the window when it opens
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Python Game")
# Setting background color
arcade.set_background_color(arcade.color.LIGHT_BLUE)

# Display the game board
arcade.start_render()

# This method  calls a method that draws the ground of the game
draw_ground(SCREEN_WIDTH, GROUND_HEIGHT, X_CORD_ORIGIN)


# Displays rendered drawings
arcade.finish_render()

# Window stays open until the user hits the close button
arcade.run()