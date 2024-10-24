""" Starting point of program """

# Dependencies

# Internal Modules
from source.framework.logger import Logger

# CONSTANTS

def main()-> None:
    """Starting point of program"""
    print("hello World")
    Logger.info(tag="_name__",message="Hello World")


if __name__ == '__main__':
    main()
