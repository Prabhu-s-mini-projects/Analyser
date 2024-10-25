"""
Class Name: LoadStatement.py
Purpose: Loads the bank statement and convert into pd dataframe
"""
# Dependencies
import pandas as pd

# Internal Dependencies
from source.framework.library.a_integrator import LOG, CONFIG, Tag

# CONSTANTS

class LoadStatement:
    """
    Purpose: Loads the bank statement and convert into pd dataframe
    Methods:
        __load_csv :loads the csv file and returns the data
        __load_statements : Get all the account statements from the location
    """

    def __init__(self):
        """
        Attributes: all the attributes are fetched from a config file
            credit_cards_statements : dict
            checking_account_statements: dict
            dir_path : str
        """
        self.dir_path = \
            CONFIG.get(section="statement_settings",option="location")
        self.__credit_cards_statements: dict = \
            self.__load_statements(account_category = "credit_cards")
        self.__checking_account_statements:dict = \
            self.__load_statements(account_category = "checking_accounts")

    @staticmethod
    def __load_csv(file_path) -> pd.DataFrame | None:
        """ To perform: loads the csv file and returns the data"""
        try:
            LOG.debug(Tag.MODEL,
                     message=f"Trying to reading the csv file from {file_path = }"
                     )
            return  pd.read_csv(file_path)

        except (FileNotFoundError, ValueError) as e:
            LOG.debug(tag=Tag.MODEL, message=f"csv_file_path = {file_path= }")
            LOG.exception(tag=Tag.MODEL,message=f"{e = }")
            return None

    def __load_statements(self,account_category: str)-> dict:
        """Get the all the credit cards from the machines"""
        LOG.debug(Tag.MODEL, f"will start loading all the {account_category} statements")

        # Get all the credit cards
        accounts :list=  CONFIG.options(section = account_category)

        statements: dict = {}

        # Transverse all the accounts one by one
        for account in accounts:

            # Getting the path of the statement from settings
            path = self.dir_path + CONFIG.get(section = account_category, option=account)

            # loading the statement and adding it into a dict
            statements.update({account:LoadStatement.__load_csv(file_path=path)})

            LOG.debug(Tag.MODEL,f"Load the {account} statement")

        LOG.info(Tag.MODEL, f"Loaded all the {account_category} statements")

        return statements

    @property
    def get_checking_accounts_statements(self)-> dict:
        """returns the checking account statements """
        return self.__checking_account_statements

    @property
    def get_credit_cards_statements(self) -> dict:
        """returns the checking account statements """
        return self.__credit_cards_statements