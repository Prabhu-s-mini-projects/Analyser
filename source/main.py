""" Starting point of program """

# Dependencies

# Internal Modules
from source.framework.library.a_integrator import LOG
from source.model.original_statement import OriginalStatement
from source.model.statements import Statements


# CONSTANTS


def main()-> None:
    """Starting point of program"""
    print("hello World")
    LOG.info(tag="MAIN",message="started")
    activity = Statements()
    print(activity.get_credit_card_transactions())
    LOG.info(tag="MAIN", message="Ended")


if __name__ == '__main__':
    main()
