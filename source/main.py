""" Starting point of program """

# Dependencies

# Internal Modules
from source.framework.library.a_integrator import LOG
from source.model.statements import Statements
from source.scratch import current_function_info


# CONSTANTS


def main()-> None:
    """Starting point of program"""
    print("hello World")
    LOG.info(message="started")
    activity = Statements()
    print(activity.get_credit_card_transactions())
    LOG.info(message="Ended")
    current_function_info()


if __name__ == '__main__':
    main()

