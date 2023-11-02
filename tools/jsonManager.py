import json


# class for work with json file with settings
class JsonSettingsManager:
    def __init__(self):
        pass

    # func changes the specified attr of the json file with settings
    @staticmethod
    def change_settings_jsonFile(attr: str, newValue: str):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        try:
            if type(data[attr]) is int:
                data[attr] = int(newValue)
            elif type(data[attr]) is str:
                data[attr] = newValue
            elif type(data[attr]) is bool:
                data[attr] = bool(newValue)
            try:
                with open("appSettings.json", "w") as settingsFileWrite:
                    json.dump(data, settingsFileWrite)
                    print("Settings was changed")
            except:
                print("Cannot open json file or write changes")
        except:
            print("Change attribute was`t done!")

    # func just returns content json with file settings
    @staticmethod
    def get_settings():
        with open("appSettings.json", "r") as settingsFile:
            return json.load(settingsFile)

    # func that returns definite a specific json attribute with file settings
    @staticmethod
    def get_current_attr(attr: str):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data[attr]

    # func that returns a caption app
    @staticmethod
    def get_caption_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["caption"]

    # func that returns a width of screen app
    @staticmethod
    def get_width_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["widthScreen"]

    # func that returns a height of screen app
    @staticmethod
    def get_height_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["heightScreen"]

    # func that returns a language app
    @staticmethod
    def get_language_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["language"]

    # func that returns a status of music app
    @staticmethod
    def get_music_status_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["musicStatus"]

    # func that returns width of screen app
    @staticmethod
    def get_music_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["musicName"]

    # func that returns font app
    @staticmethod
    def get_font_settings_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["font"]

    # func that returns name of font app
    @staticmethod
    def get_font_name_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["font"]["fontName"]

    # func that returns size of lower symbols app
    @staticmethod
    def get_font_size_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["font"]["fontSize"]

    # func that returns size of upper symbols app
    @staticmethod
    def get_font_size_upper_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["font"]["fontSizeUpper"]

    # func that returns value visibility mouse app
    @staticmethod
    def get_mouse_visible_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["mouseVisible"]

    # returns volume music app
    @staticmethod
    def get_music_volume_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["musicVolume"]

    # returns volume effects app
    @staticmethod
    def get_effects_volume_application():
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

        return data["effectsVolume"]

    # sets caption app
    @staticmethod
    def set_caption_application(caption: str):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["caption"] = caption

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets width screen app
    @staticmethod
    def set_width_application(width: int):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["widthScreen"] = width

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets height screen app
    @staticmethod
    def set_height_application(height: int):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["heightScreen"] = height

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets language interface in the Game
    @staticmethod
    def set_language_application(language: str):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["language"] = language

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets the music playback status attribute
    @staticmethod
    def set_music_status_application(musicStatus: bool):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["musicStatus"] = musicStatus

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets music will play
    @staticmethod
    def set_music_application(music: str):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["musicName"] = music

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets font app
    @staticmethod
    def set_font_name_application(font_name: str):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["font"]["fontName"] = font_name

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets font size lower symbols app
    @staticmethod
    def set_font_size_application(font_size: int):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["font"]["fontSize"] = font_size

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets font size upper symbols app
    @staticmethod
    def set_font_size_upper_application(font_size_upper: int):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["font"]["fontSizeUpper"] = font_size_upper

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets visibility mouse app
    @staticmethod
    def set_mouse_visible_application(visiblity: bool):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["mouseVisible"] = visiblity

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets volume music
    @staticmethod
    def set_music_volume_application(value: int):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["musicVolume"] = value

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)

    # sets volume effects
    @staticmethod
    def set_effect_volume_application(value: int):
        with open("appSettings.json", "r") as settingsFile:
            data = json.load(settingsFile)

            data["effectsVolume"] = value

            with open("appSettings.json", "w") as settingsFileWrite:
                json.dump(data, settingsFileWrite)
