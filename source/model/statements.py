"""
Class Name: Statements.py
Blue+print of:contains statement from all the account
"""
# Dependencies
import pandas as pd

# Internal Dependencies
from source.framework.library.a_integrator import LOG, TABLE_HEADER
from source.framework.library.pandas_toolkit import PandasToolkit
from source.model.original_statement import OriginalStatement
from source.model.statement_formatter import StatementFormatter

class Statements:
    """
    Purpose: Blueprint of contains statement from all the account
    Attributes:
        __original_statements : OriginalStatement
    Methods:
        get_credit_card_transactions : give all credit card transactions
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            original_statements : OriginalStatement
        """
        self.__original_statements: OriginalStatement = kwargs.get(
            "original_statements",OriginalStatement()
        )
        self.__formated_statements :dict = {}
        self.transactions:pd.DataFrame = pd.DataFrame(
            columns=TABLE_HEADER
        )
        self.__format_statements()

    def get_credit_card_transactions(self) -> None:
        """ returns give all credit card transactions"""

        for statement_transactions in self.__formated_statements.values():
            self.transactions = PandasToolkit.concat_dataframes(
                self.transactions,statement_transactions, axis=0,
            )

        LOG.info("credit_card_transactions table created")

        return self.transactions

    def __format_statements(self)-> None:
        """will reformat each statement into a desired formatted structure"""

        for account, statement in self.__original_statements.from_all_credit_cards.items():
            LOG.debug(f"{account = } ")
            LOG.table(table=statement,header=statement.columns)
            statement_formatter = StatementFormatter(account_name=account, statement=statement)
            new_formatted_statement = {
                account:statement_formatter.get_desired_format()
            }
            self.__formated_statements.update(new_formatted_statement)

        LOG.info("statements are formatted to the desire format")

    def get_original_statements(self) -> None:
        """returns all original statements """
        print(f"{self.__original_statements.from_all_credit_cards}")
