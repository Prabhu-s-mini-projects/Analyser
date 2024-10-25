"""
Class Name: ConfigManager.py
Blue+print of:will read the config file and get the variable params
"""
# Dependencies
import os
import configparser

# Internal Modules Dependencies
from source.framework.library.logger import LOG


# [Config parser]
class ConfigManager:
    """ Manages and responsible for parsing the config file """
    _instance = None

    @staticmethod
    def get_instance():
        """Make it as a singleton class"""
        if ConfigManager._instance is None:
            ConfigManager()
        return ConfigManager._instance

    def __init__(self):
        if ConfigManager._instance is not None:
            raise Exception("This class is a singleton!")

        ConfigManager._instance = self
        self.config = configparser.ConfigParser(interpolation=None)
        config_path = os.path.join(os.getcwd(), 'framework/config/app.ini')
        self.config.read(config_path, encoding='utf-8')

    def get(self, section:str, option:str, fallback:str =None) -> str:
        """ Will read the config file and send the value of a param"""
        try:
            return self.config.get(section, option, fallback=fallback)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            LOG.error("SETTINGS",f"{e = } ")
            LOG.exception("SETTINGS",f"Warning: Section '{section}' not found in config file.")
            return fallback
        except (FileNotFoundError, ValueError) as e:
            LOG.error("SETTINGS", f"{e = } ")
            LOG.exception("SETTINGS",f"An error occurred while setting up logging: {e}")
            return fallback

    def options(self,section:str)-> list | None:
        """ returns all the option under a list"""
        try:
            return self.config.options(section)
        except configparser.NoSectionError as e:
            LOG.error("SETTINGS", f"{e = } ")
            LOG.exception("SETTINGS", f"Warning: Section '{section}' not found in config file.")
            return None

# [CONSTANTS]
CONFIG = ConfigManager.get_instance()
