import pandas as pd


def load_excel(file_path):
    """
    Load both sheets from the Online Retail II dataset.

    Parameters
    ----------
    file_path : str
        Path to Excel file.

    Returns
    -------
    tuple
        (df_2009, df_2010)
    """

    df_2009 = pd.read_excel(
        file_path,
        sheet_name="Year 2009-2010"
    )

    df_2010 = pd.read_excel(
        file_path,
        sheet_name="Year 2010-2011"
    )

    return df_2009, df_2010