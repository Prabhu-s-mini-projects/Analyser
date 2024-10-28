"""
Class Name: PandasToolkit.py
Blue+print of:contains various methods for Dataframe operations
"""
# Dependencies
import pandas as pd

# Internal Dependencies
from source.framework.library.a_integrator import LOG

# [class]
class PandasToolkit:
    """
    Purpose: Blueprint of contains various methods for Dataframe operations
    """

    @staticmethod
    def load_csv(file_path,**kwargs) -> pd.DataFrame | None:
        """ To perform: loads the csv file and returns the data"""
        try:
            LOG.debug(
                     message=f"Trying to reading the csv file from {file_path = }"
                     )
            return  pd.read_csv(file_path,**kwargs)

        except (FileNotFoundError, ValueError) as e:
            LOG.debug(message=f"csv_file_path = {file_path= }")
            LOG.exception(message=f"{e = }")
            return None

    @staticmethod
    def combine_first_column(df :pd.DataFrame,col1 :str, col2 :str, new_column :str) -> pd.DataFrame:
        """
        Merge two columns in a DataFrame into a new column with an optional separator.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the columns.
        - col1 (str): The first column to merge.
        - col2 (str): The second column to merge.
        - new_column (str): The name of the new column that will store the merged values.
        - separator (str): The separator to use between values from col1 and col2.

        Returns:
        - pd.DataFrame: The DataFrame with the new merged column.
        """
        df[new_column] = df[col1].combine_first(df[col2])
        return df

    @staticmethod
    def concat_dataframes(df1, df2, axis=0, ignore_index=True) -> pd.DataFrame:
        """
        Concatenate two DataFrames along rows or columns with column validation.

        Parameters:
        - df1 (pd.DataFrame): The first DataFrame.
        - df2 (pd.DataFrame): The second DataFrame.
        - axis (int): The axis to concatenate along (0 for rows, 1 for columns).
        - ignore_index (bool): Whether to ignore index and reindex in the concatenated DataFrame.

        Returns:
        - pd.DataFrame: The concatenated DataFrame.

        Raises:
        - ValueError: If the columns of df1 and df2
        do not match when axis=0 (row-wise concatenation).
        """
        if axis == 0:
            # Check if columns match for row-wise concatenation
            if set(df1.columns) != set(df2.columns):
                missing_in_df1 = set(df2.columns) - set(df1.columns)
                missing_in_df2 = set(df1.columns) - set(df2.columns)
                LOG.error(f"\n {missing_in_df1 = } \n {missing_in_df1 = }")
                raise ValueError(
                    f"Concatenation failed: Columns missing in df1: {missing_in_df1}, "
                    f"Columns missing in df2: {missing_in_df2}"
                )

        # Concatenate the DataFrames
        return pd.concat([df1, df2], axis=axis, ignore_index=ignore_index)

    @staticmethod
    def rename_columns(df, columns_mapping:dict) -> pd.DataFrame:
        """
        Rename columns in the DataFrame based on a dictionary mapping.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the columns to rename.
        - columns_mapping (dict): A dictionary where keys are current column names,
                                  and values are the new column names.

        Returns:
        - pd.DataFrame: The DataFrame with renamed columns.

        Raises:
        - ValueError: If any of the specified columns to rename do not exist in the DataFrame.
        """
        # Check if all specified columns to rename exist in the DataFrame
        missing_columns = [col for col in columns_mapping if col not in df.columns]
        if missing_columns:
            LOG.error(f"\n {missing_columns = } ")
            raise ValueError(f"Columns not found in DataFrame: {missing_columns}")

        # Rename the columns based on the mapping dictionary
        return df.rename(columns=columns_mapping)

    @staticmethod
    def filter_columns(df, columns:list) -> pd.DataFrame:
        """
        Filter the DataFrame to only include specified columns.

        Parameters:
        - df (pd.DataFrame): The DataFrame to filter.
        - columns (list): List of column names to keep.

        Returns:
        - pd.DataFrame: The filtered DataFrame containing only the specified columns.

        Raises:
        - ValueError: If any of the specified columns are not in the DataFrame.
        """
        # Check if all specified columns exist in the DataFrame
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            LOG.error(f"\n {missing_columns = } ")
            raise ValueError(f"Columns not found in DataFrame: {missing_columns}")

        # Filter the DataFrame to include only the specified columns
        return df[columns]

    @staticmethod
    def add_column(df, column_name, value=None, func=None,source_column=None) -> pd.DataFrame:
        """
        Add a new column to the DataFrame with a constant value or using a function.

        Parameters:
        - df (pd.DataFrame): The DataFrame to add the column to.
        - column_name (str): The name of the new column to add.
        - value (optional): A constant value to assign to the new column for all rows.
        - func (callable, optional): A function to generate values for the new column.
                                     If provided, it overrides `value`.
                                     The function will be applied row-wise.
        - source_column (str, optional): The name of an existing column in the DataFrame.
                                          If provided, the new column values will be derived
                                          from this existing column using the function `func`.

        Returns:
        - pd.DataFrame: The DataFrame with the new column added.

        Raises:
        - ValueError: If neither `value` nor `func` is provided.
        """
        if source_column is not None and source_column in df.columns:
            # Derive values from an existing column using the provided function
            df[column_name] = df[source_column].apply(func)
        elif func is not None:
            # Apply a function row-wise to generate the column values
            df[column_name] = df.apply(func, axis=1)
        elif value is not None:
            # Add a column with a constant value
            df[column_name] = value
        else:
            LOG.error("You must provide either a 'value' or a 'func' parameter")
            raise ValueError("You must provide either a 'value' or a 'func' parameter.")

        return df

    @staticmethod
    def filter_rows(df, column_name, condition) -> pd.DataFrame | None:
        """
        Filter rows in the DataFrame based on a condition applied to a specified column.

        Parameters:
        - df (pd.DataFrame): The DataFrame to filter.
        - column_name (str): The name of the column to apply the condition to.
        - condition (callable): A function that takes a single value and returns True if the row
                                should be included in the filtered DataFrame.

        Returns:
        - pd.DataFrame: The filtered DataFrame containing only rows where the condition is True.

        Raises:
        - ValueError: If the specified column does not exist in the DataFrame.
        """
        if column_name not in df.columns:
            LOG.error(f"Column '{column_name}' not found in the DataFrame.")
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

        # Apply the condition to the specified column
        return df[df[column_name].apply(condition)]

    @staticmethod
    def modify_column(df, column_name, condition, operation):
        """
        Modify the values of a specified column based on a condition.

        Parameters:
        - df (pd.DataFrame): The DataFrame to modify.
        - column_name (str): The name of the column to apply the condition and operation to.
        - condition (callable): A function that takes a single value and returns True if
                                the value should be modified.
        - operation (callable): A function that takes a value and returns the modified value.

        Returns:
        - pd.DataFrame: The DataFrame with the modified column.

        Raises:
        - ValueError: If the specified column does not exist in the DataFrame.
        """
        if column_name not in df.columns:
            LOG.error(f"Column '{column_name}' not found in the DataFrame.")
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

        # Apply the condition and modify the column values using the operation
        df.loc[df[column_name].apply(condition), column_name] = df[column_name].apply(operation)

        return df
