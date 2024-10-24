import logging
import datetime

# Get current time to generate the log file name
current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
log_filename = f"Analyser_{current_time}.log"  # Log file with timestamp

# Create and configure logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the minimum log level

# Create handlers
file_handler = logging.FileHandler(log_filename)  # Log to file
console_handler = logging.StreamHandler()  # Log to console (PyCharm output)

# Set log format
log_format = '%(asctime)s : %(levelname)s : [%(name)s] : %(message)s'
formatter = logging.Formatter(log_format)

# Attach the formatter to both handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)  # Log to file
logger.addHandler(console_handler)  # Log to console

# Example log messages
logger.info("This is an info message.")
logger.error("This is an error message.")
logger.debug("This is a debug message.")
