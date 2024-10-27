"""
Class Name: StatementFormatter.py
Blue+print of:formatting and organizing the data into desired structure
"""
# Dependencies
import pandas as pd

# Internal Dependencies
from source.framework.library.a_integrator import LOG, TABLE_HEADER
from source.framework.library.config_manager import CONFIG
from source.framework.library.pandas_toolkit import PandasToolkit

class StatementFormatter:
    """
    Purpose: formatting and organizing the data into desired structure
    Attributes:
        statement : pd.DataFrame
        account_name: str
    Methods:
        _rename_columns : will rename columns in the data table
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            statements : OriginalStatement
        """
        self.statement: pd.DataFrame = kwargs.get("statement")
        self.account_name: str = kwargs.get("account_name")

    def get_desired_format(self)-> pd.DataFrame:
        """will combine and return all the tables"""
        self._format_amount_column()
        self._rename_columns()
        self._add_from_account_col()
        self._required_columns()
        return self.statement

    def _format_amount_column(self) -> None:
        """ To perform: will rename columns in the data table"""

        columns = self.statement.columns
        lowercase_columns = [column.lower() for column in columns]

        if 'amount' not in lowercase_columns:
            self.statement = PandasToolkit.combine_first_column(
                self.statement,col1="Debit",col2="Credit",new_column='amount'
            )
            LOG.info("Amount column added")
        else:
            LOG.debug("Amount already exists")

    def _rename_columns(self) -> None:
        """ To perform: will rename columns in the data table"""

        section = self.account_name + "_map"
        mapping_form_config = CONFIG.get_options_pair(section)

        # Interchange keys and values
        mapping = {value: key for key, value in mapping_form_config.items()}

        self.statement = PandasToolkit.rename_columns(self.statement,columns_mapping=mapping)
        LOG.debug("After renaming column the statements is")
        LOG.table(table=self.statement, header=self.statement.columns)

    def _required_columns(self)-> None:
        """selecting only required columns """
        required_columns = TABLE_HEADER

        self.statement = PandasToolkit.filter_columns(self.statement,required_columns)
        LOG.debug("After filtered with required column the statement is")
        LOG.table(table=self.statement,header=self.statement.columns)

    def _add_from_account_col(self)-> None:
        """adds a new column and fill the account name as a value"""
        self.statement = PandasToolkit.add_column(
            self.statement,column_name="from_account",value=self.account_name
        )
        LOG.debug("After adding from account column")
        LOG.table(table=self.statement, header=self.statement.columns)

    def get_account_name(self)-> str:
        """returns the account name"""
        return self.account_name
