import arcade
from views.game_view import GameView

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Pacman dmalovan"

def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = GameView()
    game_view.window.set_update_rate(1/4)
    game_view.setup()
    window.show_view(game_view)
    arcade.run()
