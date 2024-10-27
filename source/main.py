""" Starting point of program """
from venv import logger

# Dependencies

# Internal Modules
from source.framework.library.a_integrator import LOG
from source.model.statements import Statements

# CONSTANTS

def main()-> None:
    """Starting point of program"""
    print("hello World")
    LOG.info(message="started")
    activity = Statements()
    credit_transactions  = activity.transactions
    LOG.table(table=credit_transactions,header=credit_transactions.columns)
    LOG.info(message="Ended")

if __name__ == '__main__':
    main()
