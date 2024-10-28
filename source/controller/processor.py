"""
Class Name: Processor.py
Blue+print of:process the statement makes it available for the report
"""
# Dependencies
import pandas as pd

# Internal Dependencies
from source.framework.library.a_integrator import LOG
from source.framework.library.json_handler import JsonHandler
from source.framework.library.pandas_toolkit import PandasToolkit


# CONSTANTS
SUB_CATEGORY_HASH_MAP_PATH = "database/mapper/description_to_sub_category.json"
CATEGORY_HASH_MAP_PATH = "database/mapper/sub_category_to_category.json"

class Processor:
    """
    Purpose: Blueprint that processes the statement makes it available for making report
    Attributes:
        __raw_transactions : pd.Dataframe
    Methods:
        process_transactions : will add additional columns based on the existing data
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            transactions : pd.Dataframe
        """
        self.__raw_transactions: pd.DataFrame = kwargs.get("raw_transactions")
        self.processed_transactions = self.process_transactions()

    def process_transactions(self) -> pd.DataFrame:
        """
        To perform: will add additional columns based on the existing data
        1. Adds subcategory column
        2. Adds category column
        3. Adds C_or_D
        """
        LOG.info("starts processing the transactions")


        self._add_category()

        self._add_c_or_d()

        LOG.info("Processed transactions available to generate report")
        return self.__raw_transactions

    def _add_sub_category(self)-> pd.DataFrame:
        """
        # Prerequisites:
            1. Needs description column
            2. JSON Mapper: description_to_sub_category_mapper
        :return:
        """
        # Reads the JSON file
        sub_category_mapper = JsonHandler(file_path=SUB_CATEGORY_HASH_MAP_PATH)


        # Adds new column category to database.
        self.__raw_transactions = PandasToolkit.add_column(
            df=self.__raw_transactions,
            column_name="sub_category",
            source_column='description',
            func=lambda description: self.mapper(description,sub_category_mapper.data)
        )

        LOG.info("sub_category added to transactions")
        return self.__raw_transactions

    def _add_category(self)-> pd.DataFrame:
        """
        # Prerequisites:
            1.needs sub_category column
            2. JSON Mapper: sub_category_to_category_mapper
        :return:
        """
        # Prerequisites:
        if "sub_category" not in self.__raw_transactions.columns:
            self._add_sub_category()

        # Reads the JSON file
        category_mapper = JsonHandler(file_path=CATEGORY_HASH_MAP_PATH)

        # Adds new column category to database.
        self.__raw_transactions = PandasToolkit.add_column(
            df=self.__raw_transactions,
            column_name="category",
            source_column='sub_category',
            func=lambda sub_category_column: self.mapper(sub_category_column,category_mapper.data)
            )

        LOG.info("category added to transactions")
        return self.__raw_transactions

    def _add_c_or_d(self)-> pd.DataFrame:
        """
        # Prerequisites: needs Amount column
        """

        # Adds new column c_or_d to database.
        self.__raw_transactions = PandasToolkit.add_column(
            df=self.__raw_transactions,
            column_name="c_or_d",
            source_column='amount',
            func=lambda amount_column: "earnings" if amount_column > 0 else "expenditures"
            )


        LOG.info("c_or_d added to transactions")
        return self.__raw_transactions

    @staticmethod
    def mapper(content:str ,hash_map: dict)-> str:
        """ Will identify which of the keyword to map the category"""
        content = content.lower()
        for category, keywords in hash_map.items():
            for keyword in keywords:
                if keyword.lower() in content:
                    return category
        return ""  # Return a default value if no match found
