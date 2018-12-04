import arcade

# Set the size of the game screen as constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

# Setting dimensions of the window when it opens
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Python Game")
# Setting background color
arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

# Display the game board
arcade.start_render()

# Displays rendered drawings
arcade.finish_render()

# Window stays open until the user hits the close button
arcade.run()