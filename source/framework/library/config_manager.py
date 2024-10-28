"""
Class Name: ConfigManager.py
Blue+print of:will read the settings file and get the variable params
"""
# Dependencies
import os
import configparser

# Internal Modules Dependencies
from source.framework.library.logger import LOG

# [CONSTANTS]
CONFIG_FILE_PATH = 'framework/settings/config.ini'

# [Config parser]
class ConfigManager:
    """ Manages and responsible for parsing the settings file """
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
            config_path = os.path.join(os.getcwd(),CONFIG_FILE_PATH)
            self.config.read(config_path, encoding='utf-8')

            self._initialized = True


    def get(self, section:str, option:str, fallback:str =None) -> str:
        """ Will read the settings file and send the value of a param"""
        try:
            return self.config.get(section, option, fallback=fallback)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            LOG.error(f"{e = } ")
            LOG.exception(f"Warning: Section '{section}' not found in settings file.")
            return fallback
        except (FileNotFoundError, ValueError) as e:
            LOG.error(f"{e = } ")
            LOG.exception(f"An error occurred while setting up logging: {e}")
            return fallback

    def get_options(self, section:str)-> list | None:
        """ returns all the option under a list"""
        try:
            return self.config.options(section)
        except configparser.NoSectionError as e:
            LOG.error(f"{e = } ")
            LOG.exception(f"Warning: Section '{section}' not found in settings file.")
            return None

    def get_options_pair(self,section:str)-> dict| None:
        """:returns: the options in key value pair """
        try:
            return dict(self.config.items(section))
        except configparser.NoSectionError as e:
            LOG.error(f"{e = } ")
            LOG.exception(f"Warning: Section '{section}' not found in settings file.")
            return None


# [CONSTANTS]
CONFIG = ConfigManager()
