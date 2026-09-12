
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv(file_path: str) ->pd.DataFrame:

    return pd.read_csv(file_path)


def check_dtype(df: pd.DataFrame) -> None:

    dtypes = df.dtypes
    no_unique = df.nunique()
    print(pd.DataFrame({"Dtypes": dtypes, "Num. of Unique": no_unique}))


def convert_dtype(df: pd.DataFrame, cols: list, dtype:str) -> pd.DataFrame:

    df[cols] = df[cols].astype(dtype)
    return df

def check_nulls(df:pd.DataFrame) ->None:

    nulls = df.isnull().sum()
    nulls_ratio = (nulls / len(df)) * 100
    print(pd.DataFrame({"Num. of Nulls": nulls, "Ratio": nulls_ratio}))

def plot_boxplot(df: pd.DataFrame):

    num_cols = df.select_dtypes("number").columns
    plt.figure(figsize=(8,1))

    for i, col in enumerate(num_cols):
        plt.subplot(2,2,i+1)
        sns.boxplot(df[col], orient="h")
        plt.title(f"{col} Boxplot")

    plt.show()

def clip_outliers(df: pd.DataFrame) ->pd.DataFrame:

    num_cols = df.select_dtypes("number").columns

    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower_fence = Q1 - 1.5*IQR 
        upper_fence = Q3 + 1.5*IQR

        df[col] = df[col].clip(lower_fence, upper_fence)

    return df


def show_duplicates(df: pd.DataFrame) ->None:
    Duplicates = df[df.duplicated(keep= False)]
    print(f"Duplicates: {df.duplicated().sum()}")
    if not Duplicates.empty:
        print(Duplicates)


def remove_duplicates(df:pd.DataFrame, subset = None, keep_strategy = "first") ->pd.DataFrame:

    return df.drop_duplicates(subset= subset, keep= keep_strategy, ignore_index= True, inplace=True)


def draw_histogram(df: pd.DataFrame):

    num_cols = df.select_dtypes("number")
    plt.figure(figsize = (9,2))

    for i , col in enumerate(num_cols):
        plt.subplot(2,2,i+1)
        plt.hist(df[col], edgecolor = "Black")
        plt.title(f"{col} hist graph")
    plt.show()


def draw_countplot(df: pd.DataFrame):

    cat_cols = df.select_dtypes("category")
    plt.figure(figsize = (14,4))

    for i , col in enumerate(cat_cols):
        plt.subplot(2,3,i+1)
        sns.countplot(data = df, x = col)
        plt.title(f"{col} Count Plot")
    plt.subplots_adjust(hspace=0.8, wspace=0.3)
    plt.show()