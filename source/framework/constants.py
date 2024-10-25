""" Contains ENUMs and CONSTANTS """
# Dependencies
from enum import Enum

# [CONSTANTS]
LOGGER_CONFIG_FILE_PATH = "/Users/prabhusiva/Projects/PycharmProjects/Analyser/source/framework/config/logger.ini"

# [Enums]
class Tag(Enum):
    """To use it as part of tag"""
    MODEL = "MODEL"
    VIEW = "VIEW"
    CONTROLLER = "CONTROLLER"
    OTHERS = "MISC"

    def __str__(self):
        return self.value  # Return the value directly when str() is called
