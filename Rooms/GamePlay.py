from GameFrame import Level
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Hub import Score, Lives

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('background.png')

        self.add_room_object(Ship(self, 25, 50))
        self.add_room_object(Zork(self, 1120, 50))
        

        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)
        self.lives = Lives(self, Globals.SCREEN_WIDTH - 150, 20)
        self.add_room_object(self.lives)