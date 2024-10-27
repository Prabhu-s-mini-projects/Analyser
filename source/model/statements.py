"""
Class Name: Statements.py
Blue+print of:contains statement from all accounts
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
    Purpose: Blueprint of contains statement from all accounts
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
        self.transactions:pd.DataFrame = pd.DataFrame(
            columns=TABLE_HEADER
        )
        self.collect_transactions()

    @staticmethod
    def __format_statements( account:str, statement:pd.DataFrame ) -> pd.DataFrame:
        """
        1.
        :param statement:
        :return:
        """
        LOG.debug(f"{account = } ")
        LOG.table(table=statement, header=statement.columns)

        statement_formatter = StatementFormatter(account_name=account, statement=statement)

        formated_statement = statement_formatter.get_desired_format()

        if account in ['citi','discover']:

            # Converts expenditure to negative value and payout to positive value
            formated_statement = PandasToolkit.modify_column(
                df=formated_statement,
                column_name='amount',
                condition=lambda x: True,
                operation=lambda x: x * -1
            )

        LOG.info("statements are formatted to the desired format.")

        return formated_statement

    def collect_transactions(self) -> None:
        """
        1. Combine all statements into a single dict
        2. Traverse each statement one by one and format statement
        3. Merge the return table into transactions' table
        returns give all credit card transactions.
        """

        # Combine all statements (merging 2 dict)
        statements = \
            self.__original_statements.from_all_credit_cards\
            | self.__original_statements.from_all_checking_accounts

        # Traverse each statement one by one
        for account, statement in statements.items():

            # Formats statement into desired structure
            formatted_statement = self.__format_statements(
                account=account,statement=statement
            )

            # Adds into an existing transactions table
            self.transactions = PandasToolkit.concat_dataframes(
                self.transactions,
                formatted_statement
            )

        LOG.info("credit_card_transactions table created")
