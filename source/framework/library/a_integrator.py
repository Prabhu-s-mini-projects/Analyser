""" Contains ENUMs and CONSTANTS """
# Dependencies
from enum import Enum
from source.framework.library import logger, config_manager


# [CONSTANTS]
CONFIG = config_manager.CONFIG
LOG = logger.LOG

# [Enums]
class Tag(Enum):
    """To use it as part of tag"""
    MODEL = "MODEL"
    VIEW = "VIEW"
    CONTROLLER = "CONTROLLER"
    CONFIG = "SETTINGS"

    def __str__(self):
        return self.value  # Return the value directly when str() is called
