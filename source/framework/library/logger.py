"""
Class Name: Logger.py
Blue+print of:Central logging
"""
# Dependencies
import os
import datetime
import logging
import configparser

# Internal Modules
# N/A

# Class
class Logger:
    """ Centralized place for logging the data"""
    _instance = None
    _initialized = False  # Declare _initialized at the class level

    def __new__(cls):
        """ create this to have a single instance for this class"""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """ Configuring the logger """
        if not self._initialized:
            try:
                # Read the config file
                config = configparser.ConfigParser(interpolation=None)
                config_path = os.path.join(os.getcwd(), 'framework/config/log_settings.ini')
                config.read(config_path, encoding='utf-8')

                # Get log settings from the config file
                log_file_name = config.get('log_settings', 'log_file_name')
                log_file_format = config.get('log_settings', 'log_file_format')
                log_level = config.get('log_settings', 'log_level')
                log_directory = config.get('log_settings', 'log_directory')

                # Create the log directory if it doesn't exist
                if not os.path.exists(log_directory):
                    os.makedirs(log_directory)

                # Get current time to generate the log file name
                current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                log_filename = os.path.join(log_directory, f"{log_file_name}_{current_time}.log")
                print(f"Log file path: {log_filename}")

                # Set the log level
                log_level_mapping = {
                    'DEBUG': logging.DEBUG,
                    'INFO': logging.INFO,
                    'WARNING': logging.WARNING,
                    'ERROR': logging.ERROR,
                    'CRITICAL': logging.CRITICAL
                }

                level = log_level_mapping.get(log_level.upper(), logging.DEBUG)
                print(f"Log level: {log_level}")

                # Need to config logger
                # Set up logging configuration
                # Configure the logger
                logging.basicConfig(
                    level=level,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format=log_file_format,
                    handlers=[
                        logging.FileHandler(log_filename),  # Log to a file
                        logging.StreamHandler()  # Outputs logs to the console
                    ]
                )
                self._initialized = True
            except (configparser.NoSectionError, configparser.NoOptionError) as e:
                print(f"Error reading configuration file: {e}")
            except (FileNotFoundError, ValueError) as e:
                print(f"An error occurred while setting up logging: {e}")

    @staticmethod
    def __get_logger()-> logging.Logger:
        """
        Returns a logger instance.
        """
        logger = logging.getLogger("Analyser")
        return logger

    @staticmethod
    def __log(level, tag="", message="")-> None:
        """
        Custom log method that logs with a tag and message.

        :param level: The log level (e.g., logging.INFO, logging.ERROR).
        :param tag: A custom tag to categorize the log message.
        :param message: The log message.
        """
        logger = Logger.__get_logger()

        # Add the tag,
        logger.log(level, message, extra={'tag': tag})


    @staticmethod
    def debug(tag="", message="")-> None:
        """
        Debug level logging with a tag and message.
        """
        Logger.__log(logging.DEBUG, tag, message)

    @staticmethod
    def info(tag="", message="")-> None:
        """
        Info level logging with a tag and message.
        """
        Logger.__log(logging.INFO, tag, message)

    @staticmethod
    def error(tag="", message="")-> None:
        """
        Error level logging with a tag and message.
        """
        Logger.__log(logging.ERROR, tag, message)

    @staticmethod
    def critical(tag="", message="")-> None:
        """
        Critical level logging with a tag and message.
        """
        Logger.__log(logging.CRITICAL, tag, message)

    @staticmethod
    def exception(tag="", message="")-> None:
        """
        Logs an exception with a stack trace. Should be used inside an `except` block.
        """
        logger = Logger.__get_logger()
        log_message = f"{message} [EXCEPTION]"
        logger.error(log_message, exc_info=True, extra={'tag': tag})


# Initialize the logger explicitly when the application starts
LOG = Logger()
