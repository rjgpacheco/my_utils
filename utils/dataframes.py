"""
Collection of utilities I use often.

Some are just ways I like calling specific functions.
"""

import pandas as pd


def save_dataframe(filepath: str, df) -> None:
    df.to_csv(filepath, sep="\t", index=False)


def load_dataframe(filepath: str):
    return pd.read_csv(filepath, sep="\t")


def print_df(df, max_rows=None, max_cols=None):
    """
    This is used in Jupyter notebooks or IPython consoles 
    to print more of a dataframe.
    """
    with pd.option_context("display.max_rows", max_rows, "display.max_columns", max_cols):
        display(df)  # pylint: disable=E0602
