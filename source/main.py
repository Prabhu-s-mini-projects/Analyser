""" Starting point of program """

# Dependencies

# Internal Modules
from source.framework.library.a_integrator import LOG
from source.model.load_statement import LoadStatement


# CONSTANTS


def main()-> None:
    """Starting point of program"""
    print("hello World")
    LOG.info(tag="MAIN",message="Hello World")
    statements = LoadStatement()
    print(statements.credit_cards_statements)
    LOG.info(tag="MAIN", message="Hello World")
    LOG.info(tag="MAIN", message="Hello World")
    LOG.info(tag="MAIN", message="Hello World")
    LOG.info(tag="MAIN", message="Hello World")
    LOG.info(tag="MAIN",message="Hello World")

if __name__ == '__main__':
    main()
