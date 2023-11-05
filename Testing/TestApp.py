import unittest
from gamefiles.ui.app import *


# test methods class Application
class TestApplicationClass(unittest.TestCase):

    # test on change width screen app
    def test_width(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.width, 800)
        app.width = 1024
        self.assertEqual(app.width, 1024)

    # test on change height screen app
    def test_height(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.height, 600)
        app.height = 768
        self.assertEqual(app.height, 768)

    # test change on language
    def test_language(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.language, "en")
        app.language = "de"
        self.assertEqual(app.language, "de")

    # test on change value record music on the app
    def test_music_status(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.music_status, True)
        app.music_status = False
        self.assertEqual(app.music_status, False)

    # test on change record music
    def test_music_name(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.music_name, "Start music.mp3")
        app.music_name = "Theme 1.mp3"
        self.assertEqual(app.music_name, "Theme 1.mp3")

    # test on change music volume
    def test_music_volume(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.music_volume, 50)
        app.music_volume = 75
        self.assertEqual(app.music_volume, 75)

    # test on change volume effects
    def test_effects_volume(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.effects_volume, 75)
        app.effects_volume = 80
        self.assertEqual(app.effects_volume, 80)

    # test on change value visibility mouse cursor on the app
    def test_mouse_visible(self):
        app = Application(800, 600, "en", True, "Start music.mp3", 50, 75, True)
        self.assertEqual(app.mouse_visible, True)
        app.mouse_visible = False
        self.assertEqual(app.mouse_visible, False)


if __name__ == '__main__':
    unittest.main()
