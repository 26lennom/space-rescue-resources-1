from GameFrame import Level
from Objects.Title import Title

#initial screen for the game
class WelcomeScreen(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks) 

        self.set_background_image("Background.png")

        self.add_room_object(Title(self, 240, 200))

        self.bg_music = self.load_sound("Music.mp3")
        
        # play background music
        self.bg_music.set_volume(0.1)
        self.bg_music.play(loops=1)