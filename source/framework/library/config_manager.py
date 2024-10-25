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
    _initialized = False  # Declare _initialized at the class level

    def __new__(cls):
        """ create this to have a single instance for this class"""
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance


    def __init__(self):
        if not self._initialized:

            ConfigManager._instance = self
            self.config = configparser.ConfigParser(interpolation=None)
            config_path = os.path.join(os.getcwd(), 'framework/config/app.ini')
            self.config.read(config_path, encoding='utf-8')

            self._initialized = True


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
CONFIG = ConfigManager()