import os
import configparser


class GameSettings:
    __instance = None
    __settings_file = "settings.ini"

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(GameSettings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.settings = configparser.ConfigParser()

            if not os.path.exists(GameSettings.__settings_file):
                self.__save_settings(self.__default_settings())

            self.__load_settings()

    def __load_settings(self):
        self.settings.read(GameSettings.__settings_file)

    def __default_settings(self):
        return {
            'Window': {
                'WINDOWS_LENGTH': 640,
                'WINDOWS_WIDTH': 480
            },
            'Game': {
                'FPS': 120,
                'SCORE_TO_FINISH': 5,
                'DIFFICULTY': 'hard'
            }
        }

    def __save_settings(self, settings):
        for section, options in settings.items():
            self.settings[section] = options
        with open(GameSettings.__settings_file, 'w') as file:
            self.settings.write(file) 

    def get(self, section, key):
        return self.settings[section][key]
