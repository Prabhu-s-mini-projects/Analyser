""" Starting point of program """
from platform import processor

# Dependencies
import pandas as pd
import matplotlib
from matplotlib.table import table

from source.controller.processor import Processor

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Internal Modules
from source.framework.library.a_integrator import LOG
from source.controller.report import Report
from source.framework.library.pandas_toolkit import PandasToolkit
from source.model.statements import Statements
import json

# CONSTANTS


def main()-> None:
    """Starting point of program"""
    print("hello World")
    LOG.info(message="started")

    import logging
    # Suppress debug messages from matplotlib
    logging.getLogger('matplotlib').setLevel(logging.WARNING)


    activity = Statements()
    r_transactions = activity.transactions
    t_processor = Processor(raw_transactions=r_transactions)
    transactions = t_processor.processed_transactions
    transactions['year_month'] = transactions['transaction_date'].dt.to_period('M')

    report = Report(statement=transactions)

    earnings = report.earnings()
    LOG.table(table=earnings, header=earnings.columns)

    expenses = report.expenses()
    LOG.table(table=expenses, header=expenses.columns)


    a = earnings.pivot_table(index="category",columns="year_month",
                             values='amount',aggfunc='sum',margins=True,
                             margins_name='Total')
    LOG.table(table=a,header=a.columns)

    a = expenses.pivot_table(index="category", columns="year_month",
                             values='amount', aggfunc='sum', margins=True,
                             margins_name='Total')
    LOG.table(table=a, header=a.columns)



    LOG.info(message="Ended")

if __name__ == '__main__':
    main()
