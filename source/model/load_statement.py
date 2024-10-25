"""
Class Name: LoadStatement.py
Blue+print of:Loads the bank statement and share the results
"""
# Dependencies
import os
from datetime import datetime as dt
import pandas as pd

# Internal Dependencies
from source.framework.logger import log
from source.framework.constants import Tag


# CONSTANTS

class LoadStatement:
    """
    Purpose: Blueprint of Loads the bank statement and share the results
    Attributes:
        file_path : str
        __column_mapping: dict
        __
    Methods:
        load_csv : loads the csv file and returns the data
        validate_columns: Validates that required columns are present after mapping.
        rename_columns: Renames columns using user-provided mapping.
        clean_data: Cleans up text fields, converts date and amount fields.
        get_dataframe: Returns the cleaned and validated DataFrame.
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            file_path : str
        """
        self.file_path: str = kwargs.get("file_path")
        self.__column_mapping: dict = kwargs.get("column_mapping")
        self.__transaction_table: pd.DataFrame = None


    def __load_csv(self) -> pd.DataFrame | None:
        """ To perform: loads the csv file and returns the data"""
        try:
            log.info(Tag.MODEL,
                     message=f"Trying to reading the csv file from {self.file_path = }"
                     )
            return  pd.read_csv(self.file_path)

        except (FileNotFoundError, ValueError) as e:
            log.debug(tag=Tag.MODEL, message=f"csv_file_path = {self.file_path = }")
            log.exception(tag=Tag.MODEL,message=f"{e = }")

    def get_transactions(self)-> pd.DataFrame:
        """returns the final validation table that contains the transactions """
        return self.__load_csv()
