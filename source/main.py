""" Starting point of program """

# Dependencies

# Internal Modules
from source.framework.logger import log
from source.model.load_statement import LoadStatement

# CONSTANTS

def main()-> None:
    """Starting point of program"""
    print("hello World")
    log.info(tag="MAIN",message="Hello World")
    chase_statement = LoadStatement(file_path=None)
    chase_statement.get_transactions()
    log.info(tag="MAIN", message="Hello World")
    log.info(tag="MAIN", message="Hello World")
    log.info(tag="MAIN", message="Hello World")
    log.info(tag="MAIN", message="Hello World")
    log.info(tag="MAIN",message="Hello World")




if __name__ == '__main__':
    main()
