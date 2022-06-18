import shelve


class SaveSettings:
    def __init__(self, game):
        self.game = game
        self.file_cfg = shelve.open('cfg/data')

    def save(self):
        self.file_cfg['music status'] = self.game.music
        self.file_cfg['music'] = self.game.p_music
        self.file_cfg['language'] = self.game.language
        self.file_cfg['record1'] = self.game.record

    def add(self, name_setting, info):
        self.file_cfg[name_setting] = info

    def get(self, name):
        try:
            return self.file_cfg[name]
        except:
            return None

    def __del__(self):
        self.file_cfg.close()
        
