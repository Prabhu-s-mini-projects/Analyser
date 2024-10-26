"""
Class Name: OriginalStatement.py
Purpose: Loads the bank statement and convert into pd dataframe
"""
# Dependencies

# Internal Dependencies
from source.framework.library.a_integrator import LOG, CONFIG, Tag
from source.framework.library.pandas_toolkit import PandasToolkit


# CONSTANTS

class OriginalStatement:
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
        self.__checking_accounts_statements:dict = \
            self.__load_statements(account_category = "checking_accounts")

    def __load_statements(self,account_category: str)-> dict:
        """Get the all the credit cards from the machines"""
        LOG.debug(Tag.MODEL, f"will start loading all the {account_category} statements")

        # Get all the credit cards
        accounts :list=  CONFIG.get_options(section = account_category)

        statements: dict = {}

        # Transverse all the accounts one by one
        for account in accounts:

            # Getting the path of the statement from settings
            path = self.dir_path + CONFIG.get(section = account_category, option=account)

            new_statement = {
                account: PandasToolkit.load_csv(file_path=path)
            }
            # loading the statement and adding it into a dict
            statements.update(new_statement)

            LOG.debug(Tag.MODEL,f"{account} statement "\
                                + "Loaded" if new_statement is not  None else "NOT loaded")

        LOG.info(Tag.MODEL, f"Loaded all the {account_category} statements")

        return statements

    def from_all_checking_accounts(self)-> dict:
        """returns the checking account statements """
        return self.__checking_accounts_statements

    def from_all_credit_cards(self) -> dict:
        """returns the checking account statements """
        return self.__credit_cards_statements