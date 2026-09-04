
import pandas as pd

def Read_Data_File(file_path: str) -> pd.DataFrame:
    """
    This function reads a CSV file and returns a DataFrame.
    Parameters:
        file_path (str): The path to the CSV file.
    Returns:
        pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("ERROR: File is not found")
    except Exception as e:
        raise Exception(f"Could not read the file: {e}")


def Drop_unnecessary_features(df:  pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    This function drops the specified columns from the given DataFrame.
    Parameters:
        df (pd.DataFrame): The DataFrame from which to drop columns.
        cols (list[str]): The list of column names to drop.
    Returns:
        pd.DataFrame: The DataFrame with the specified columns dropped.
    """

    df.drop(columns = cols, inplace = True)


def Check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    
    dtypes = df.dtypes
    num_of_unique = df.nunique()
    print(pd.DataFrame({"Dtypes": dtypes, "Unique Values": num_of_unique}).T)
